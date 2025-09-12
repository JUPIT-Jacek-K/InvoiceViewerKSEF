"""
Functions reading, veryfing, tranforming XML file
"""

import os
import tempfile

import lxml.etree as etree

from Modules.misc import calculate_path
from Settings.global_var import fa_versions, varGlobals
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

invoice_debug = True


class file_html_tmp:
    _tmp_fd = 0
    _tmp_name = ""
    _tmp_opened = False

    def __init__(self) -> None:
        self._tmp_fd, self._tmp_name = tempfile.mkstemp(".html", "FA_", "tmp")
        self._tmp_opened = True

    def __del__( self ):
        self.remove()

    @property
    def fd(self) -> int:
        return self._tmp_fd

    @property
    def name(self) -> str:
        return self._tmp_name

    def file_object(self):
        return os.fdopen(self._tmp_fd)

    def close(self):
        if self._tmp_opened:
            os.close(self._tmp_fd)
            self._tmp_opened = False

    def remove(self):
        if self._tmp_opened:
            os.close(self._tmp_fd)
        if os.path.isfile(self._tmp_name):
            os.remove(self._tmp_name)


def invoice_print_debug(msg):
    if invoice_debug:
        print(msg)


class FileResolver(etree.Resolver):
    def resolve(self, url, pubid, context):
        return self.resolve_filename(url, context)


def fa_x_validate(
    fa_file: str,
    fa_ver: str,
    silent: bool = True,
    title_mgsbox: str = "Weryfikacja struktury eFaktura",
):
    lCont = True
    if fa_ver in fa_versions:
        xsd_file = fa_versions[fa_ver]["xsd"]
        if os.path.isfile(calculate_path(fa_file)):
            try:
                xml_parser = etree.XMLParser()
                xmlschema_doc = etree.parse(calculate_path(xsd_file), xml_parser)
                xsd_schema = etree.XMLSchema(xmlschema_doc)

                xml_doc = etree.parse(calculate_path(fa_file), xml_parser)
                lCont = xsd_schema.validate(xml_doc)
                # msg = f"Błąd validacji: {fa_file}"
                # invoice_print_debug(msg)

            except FileNotFoundError as e:
                # Błąd: jeden z plików nie został znaleziony.
                msg = f"Nie znaleziono pliku: {e.filename}"
                invoice_print_debug(msg)
                if not silent:
                    msgBox = winMessageBox(
                        msg, title_mgsbox, wxdlg_const.ICON_STOP | wxdlg_const.ID_OK
                    )
                    msgBox.ShowModal()
                lCont = False
            except etree.XMLSyntaxError as e:
                # Błąd składniowy w pliku XML.
                msg = f"Błąd formatu pliku XML. Sprawdź, czy plik jest poprawnie sformułowany. Szczegóły: {e}"
                if not silent:
                    msgBox = winMessageBox(
                        msg, title_mgsbox, wxdlg_const.ICON_STOP | wxdlg_const.ID_OK
                    )
                    msgBox.ShowModal()
                lCont = False
            except Exception as e:
                # Obsługa wszelkich innych, nieprzewidzianych błędów.
                msg = f"fa_x_validate Wystąpił nieoczekiwany błąd: {e}"
                invoice_print_debug(msg)
                if not silent:
                    msgBox = winMessageBox(
                        msg, title_mgsbox, wxdlg_const.ICON_STOP | wxdlg_const.ID_OK
                    )
                    msgBox.ShowModal()
                lCont = False
        else:
            xfile = calculate_path(fa_file)
            msg = f"Nie znaleziono pliku: {xfile}"
            invoice_print_debug(msg)
            if not silent:
                msgBox = winMessageBox(
                    msg, title_mgsbox, wxdlg_const.ICON_STOP | wxdlg_const.ID_OK
                )
                msgBox.ShowModal()
            lCont = False

    else:
        msg = f"Błedny numer wersji eFaktury w systemie KSeF: {fa_ver}"
        invoice_print_debug(msg)
        if not silent:
            msgBox = winMessageBox(
                msg, title_mgsbox, wxdlg_const.ICON_STOP | wxdlg_const.ID_OK
            )
            msgBox.ShowModal()
        lCont = False

    return lCont


def fa_version(
    file_fa: str,
    silent: bool = True,
    title_mgsbox: str = "Weryfikacja struktury eFaktura",
):
    version = "?"
    ver_keys_list = fa_versions.keys()
    for ver_key in ver_keys_list:
        if fa_x_validate(file_fa, ver_key, True):
            version = ver_key
            break
    return version


def fa_generate_html(fa_file: str, type_xsl: str = "MF", silent: bool = True):
    html_tmp = None
    version = fa_version(fa_file, silent)
    invoice_print_debug(f"Wykryta wersja {version}")
    if version != "?":
        if type_xsl == "MF":
            xsl_fa2_filename = fa_versions[version]["xsl_mf"]
        else:
            xsl_fa2_filename = fa_versions[version]["xsl_app"]

        try:
            xml_parser = etree.XMLParser()
            xml_parser.resolvers.add(FileResolver())
            # file_fa_full = os.path.basename(fa_file)

            invoice_print_debug(f"Wykryta wersja {version} 1")
            xml_invoice = etree.parse(calculate_path(fa_file), xml_parser)
            invoice_print_debug(f"Wykryta wersja {version} 2")
            xsl_invoice = etree.parse(calculate_path(xsl_fa2_filename), xml_parser)
            invoice_print_debug(f"Wykryta wersja {version} 3")
            transform = etree.XSLT(xsl_invoice)
            dom_invoice = transform(xml_invoice)
            invoice_print_debug(f"Wykryta wersja {version} 4")
            html_body = etree.tostring(
                dom_invoice, pretty_print=True, encoding="unicode"
            )

            # invoice_print_debug(f"Wykryta wersja {version} 4 -> {varGlobals.app_tmp}")
            html_tmp = file_html_tmp()

            # invoice_print_debug(f"Plik TMP -> {file_fa_mame}")

            # html_tmp_file = file_fa_mame # varGlobals.app_tmp + "/" +
            fhtml = open( html_tmp.name, "w+")
            if fhtml.writable():
                fhtml.write(html_body)
            html_tmp.close()

        except FileNotFoundError as e:
            # Błąd: jeden z plików nie został znaleziony.
            msg = f"Nie znaleziono pliku: {e.filename}"
            invoice_print_debug(msg)
            if not silent:
                msgBox = winMessageBox(
                    msg,
                    "Podgląd faktury",
                    wxdlg_const.ICON_STOP | wxdlg_const.ID_OK,
                )
                msgBox.ShowModal()

        except etree.XMLSyntaxError as e:
            # Błąd składniowy w pliku XML.
            msg = f"Błąd formatu pliku XML. Sprawdź, czy plik jest poprawnie sformułowany. Szczegóły: {e}"
            invoice_print_debug(msg)
            if not silent:
                msgBox = winMessageBox(
                    msg,
                    "Podgląd faktury",
                    wxdlg_const.ICON_STOP | wxdlg_const.ID_OK,
                )
                msgBox.ShowModal()

        except etree.XSLTParseError as e:
            # Błąd składniowy w pliku XSLT.
            msg = f"Błąd w pliku XSLT. Sprawdź, czy plik jest poprawny. Szczegóły: {e}"
            invoice_print_debug(msg)
            if not silent:
                msgBox = winMessageBox(
                    msg,
                    "Podgląd faktury",
                    wxdlg_const.ICON_STOP | wxdlg_const.ID_OK,
                )
                msgBox.ShowModal()

        except Exception as e:
            # Obsługa wszelkich innych, nieprzewidzianych błędów.
            msg = f"fa_generate_html Wystąpił nieoczekiwany błąd: {e}"
            invoice_print_debug(msg)
            if not silent:
                msgBox = winMessageBox(
                    msg,
                    "Podgląd faktury",
                    wxdlg_const.ICON_ERROR | wxdlg_const.ID_OK,
                )
                msgBox.ShowModal()

    return html_tmp
