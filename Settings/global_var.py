from datetime import datetime


class _varGlobals:
    invoice_debug: bool = False

    @property
    def app_title(self):
        return "Przeglądarka faktur KSEF"

    @property
    def app_version(self):
        return "v. 1.0.0"

    @property
    def app_year_from(self):
        return "2025.09.01"

    @property
    def app_year_to(self):
        return datetime.today().strftime("%Y.%m.%d")

    @property
    def path_tmp(self):
        return "tmp"

    @property
    def path_icons_16(self):
        return "Graphics/CreativeFreedomIcon/16x16"

    @property
    def path_icons_24(self):
        return "Graphics/CreativeFreedomIcon/24x24"

    @property
    def path_icons_34(self):
        return "Graphics/CreativeFreedomIcon/32x32"

    @property
    def path_icons_48(self):
        return "Graphics/CreativeFreedomIcon/48x48"

    @property
    def path_icons_ico(self):
        return "Graphics/CreativeFreedomIcon/ico"

    @property
    def path_glyph(self):
        return "Graphics/CreativeFreedomIcon/glyphs"

    @property
    def fa_versions(self):
        tabOut = {
            "1": {
                "xsd": "KSEF_Wzory/FA_1/schemat.xsd",
                "xsl_mf": "KSEF_Wzory/FA_1/styl.xsl",
                "xsl_app": "KSEF_Wzory/FA_1/styl.xsl",
            },
            "2": {
                "xsd": "KSEF_Wzory/FA_2/schemat.xsd",
                "xsl_mf": "KSEF_Wzory/FA_2/styl.xsl",
                "xsl_app": "KSEF_Wzory/FA_2/styl.xsl",
            },
            "3": {
                "xsd": "KSEF_Wzory/FA_2/schemat.xsd",
                "xsl_mf": "KSEF_Wzory/FA_2/styl.xsl",
                "xsl_app": "KSEF_Wzory/FA_2/styl.xsl",
            },
        }
        return tabOut


varGlobals = _varGlobals()
