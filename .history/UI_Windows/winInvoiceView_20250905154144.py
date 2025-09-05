import wx
import lxml.etree as tree
import os
import sys  

class winInvoiceView(wx.MDIChildFrame):
    def __init__(self, parent, title):
        super(winInvoiceView, self).__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self)
        self.textCtrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textCtrl, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)
        self.Show()

    def load_invoice(self, xml_filename):
        xsl_fa1_filename = "KSEF_Wzory/FA_1/styl.xsl"
        xsl_fa2_filename = "KSEF_Wzory/FA_2/styl.xsl"
        xsl_fa3_filename = "KSEF_Wzory/FA_2/styl.xsl"
        file_fa_full = os.path.basename(xml_filename)
        file_fa_base, file_fa_ext = os.path.splitext(file_fa_full)
        folder_name="BUFOR"
        parsing_ok = False
        try:
            tree = xltree.parse(file_path)
            root = tree.getroot()
            pretty_xml = xltree.tostring(root, pretty_print=True, encoding='unicode')
            self.textCtrl.SetValue(pretty_xml)
        except Exception as e:
            wx.MessageBox(f"Error loading invoice: {e}", "Error", wx.OK | wx.ICON_ERROR)