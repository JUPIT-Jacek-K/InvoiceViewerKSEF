
from datetime import datetime


class varGlobals:
    app_title = "Przeglądarka faktur KSEF"
    app_version = "v. 1.0.0"
    app_year_from ="2025.09.01"
    app_year_to = datetime.today().strftime('%Y.%m.%d')
    app_tmp = './TMP/'


fa_versions = {
    '1' : {
        "xsd": "KSEF_Wzory/FA_1/schemat.xsd",
        "xsl_mf": "KSEF_Wzory/FA_1/styl.xsl",
        "xsl_app": "KSEF_Wzory/FA_1/styl.xsl",
    },
    '2' : {
        "xsd": "KSEF_Wzory/FA_2/schemat.xsd",
        "xsl_mf": "KSEF_Wzory/FA_2/styl.xsl",
        "xsl_app": "KSEF_Wzory/FA_2/styl.xsl",
    },
    '3' : {
        "xsd": "KSEF_Wzory/FA_2/schemat.xsd",
        "xsl_mf": "KSEF_Wzory/FA_2/styl.xsl",
        "xsl_app": "KSEF_Wzory/FA_2/styl.xsl",
    },
}
