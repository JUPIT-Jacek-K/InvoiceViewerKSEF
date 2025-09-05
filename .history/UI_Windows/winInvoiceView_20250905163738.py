import os
import sys

import lxml.etree as ET
import wx

from Modules.misc import FileResolver
from UI_Windows.winDialogs import winMessageBox, wxdlg_const


class winInvoiceView(wx.MDIChildFrame):
    def __init__(self, parent, title, xml_invoice_filename):
        super(winInvoiceView, self).__init__(parent, title=title, size=(800, 600))
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
        self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_PRINT, _(u"tool"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_IN, _(u"tool"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

        self.m_toolBar1.Realize()

        self.htmlWinFa = wx.html2.WebView.New(self)
        self.panel = wx.Panel(self)
        self.textCtrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textCtrl, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)
        if self.load_invoice(xml_invoice_filename):
            self.SetTitle(f"Podgląd faktury - {os.path.basename(xml_invoice_filename)}")
            self.Show()
        else:
            self.Destroy()

    def load_invoice(self, xml_filename):
        xsl_fa1_filename = "KSEF_Wzory/FA_1/styl.xsl"
        xsl_fa2_filename = "KSEF_Wzory/FA_2/styl.xsl"
        xsl_fa3_filename = "KSEF_Wzory/FA_2/styl.xsl"
        file_fa_full = os.path.basename(xml_filename)
        file_fa_base, file_fa_ext = os.path.splitext(file_fa_full)
        folder_name = "BUFOR"
        parsing_ok = False
        try:
            parser = ET.XMLParser()
            parser.resolvers.add(FileResolver())
            dom = ET.parse(xml_filename, parser)
            xslt = ET.parse(xsl_fa2_filename, parser)
            transform = ET.XSLT(xslt)
            newdom = transform(dom)
            html_body = ET.tostring(newdom, pretty_print=True, encoding="unicode")
            parsing_ok = True
        except FileNotFoundError as e:
            # Błąd: jeden z plików nie został znaleziony.
            msg = f"Nie znaleziono pliku: {e.filename}"
            msgBox = winMessageBox(
                msg, "Podgląd faktury", wxdlg_const.ICON_STOP | wxdlg_const.ID_OK, self
            )
            msgBox.ShowModal()

        except ET.XMLSyntaxError as e:
            # Błąd składniowy w pliku XML.
            msg = f"Błąd formatu pliku XML. Sprawdź, czy plik jest poprawnie sformułowany. Szczegóły: {e}"
            msgBox = winMessageBox(
                msg, "Podgląd faktury", wxdlg_const.ICON_STOP | wxdlg_const.ID_OK, self
            )
            msgBox.ShowModal()

        except ET.XSLTParseError as e:
            # Błąd składniowy w pliku XSLT.
            msg = f"Błąd w pliku XSLT. Sprawdź, czy plik jest poprawny. Szczegóły: {e}"
            msgBox = winMessageBox(
                msg, "Podgląd faktury", wxdlg_const.ICON_STOP | wxdlg_const.ID_OK, self
            )
            msgBox.ShowModal()

        except Exception as e:
            # Obsługa wszelkich innych, nieprzewidzianych błędów.
            msg = f"Wystąpił nieoczekiwany błąd: {e}"
            msgBox = winMessageBox(
                msg, "Podgląd faktury", wxdlg_const.ICON_ERROR | wxdlg_const.ID_OK, self
            )
            msgBox.ShowModal()

        if parsing_ok:
            self.htmlWinFa.SetPage(html=html_body, baseUrl="")
