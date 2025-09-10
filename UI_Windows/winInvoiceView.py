import gettext
import os
import sys

import lxml.etree as ET
import wx
import wx.html2

from Modules.invoice_fncs import fa_generate_html
from Modules.misc import calculate_path
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

_ = gettext.gettext


class winInvoiceView(wx.MDIChildFrame):
    html_file = ""

    def __init__(self, parent, title):
        super(winInvoiceView, self).__init__(
            parent, title=title, size=wx.Size(800, 600)
        )
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        # self.m_toolPrint = self.m_toolBar1.AddTool( wx.ID_PRINT, _(u"Drukuj"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        # self.m_toolInfo  = self.m_toolBar1.AddTool( wx.ID_INFO, _(u"Informacja"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        # self.m_toolClose = self.m_toolBar1.AddTool( wx.ID_CLOSE, _(u"Zamknij"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_toolBar1.Realize()

        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_statusBar1.SetStatusText(_("Gotowy"), 0)
        self.vieSizer = wx.BoxSizer(
            wx.VERTICAL
        )  # wx.StaticBox(self, wx.ID_ANY, _("label"), wx.DefaultPosition, wx.DefaultSize, wx.ALL | wx.EXPAND, 5)

        self.htmlWinFa = wx.html2.WebView.New(
            self,
            wx.ID_ANY,
            "",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.html2.WebViewBackendDefault,
            wx.ALL | wx.EXPAND,
        )

        self.htmlWinFa.SetMinSize(wx.Size(-1, -1))
        self.vieSizer.Add(self.htmlWinFa, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.vieSizer)
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, e: wx.Event):
        self.htmlWinFa.Close()
        if len(self.html_file) > 0 and os.path.isfile(self.html_file):
            base_file = calculate_path( self.html_file )
            print(base_file)
            os.remove(base_file )
            self.html_file = ""
        self.Destroy()

    def load_invoice(self, xml_filename):
        parsing_ok = False
        self.html_file = fa_generate_html(
            fa_file=xml_filename, type_xsl="MF", silent=False
        )
        # print(html_body)

        if len(self.html_file) > 0 and os.path.isfile(self.html_file):
            print("ok")
            absolute_path = os.path.abspath( calculate_path( self.html_file) )
            self.htmlWinFa.LoadURL(f"file:///{absolute_path}")
            parsing_ok = True
        return parsing_ok
