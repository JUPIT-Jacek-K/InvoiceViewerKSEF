import gettext
import os

import lxml.etree as ET
import wx
import wx.html2

from Modules.invoice_fncs import fa_generate_html, file_html_tmp
from Modules.misc import calculate_path
from Settings.global_var import varGlobals
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

_ = gettext.gettext


class winInvoiceView(wx.MDIChildFrame):
    tmp_html_file: file_html_tmp | None = None
    InvoiceFilename: str = ""

    def __init__(self, parent, title):
        super(winInvoiceView, self).__init__(
            parent, title=title, size=wx.Size(800, 600)
        )
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_toolBar1 = self.CreateToolBar(
            wx.TB_HORIZONTAL | wx.TB_HORZ_TEXT, wx.ID_ANY
        )
        self.m_toolBar1.SetToolBitmapSize(wx.Size(16, 16))
        self.m_toolBar1.SetMinSize(wx.Size(-1, -1))
        self.m_toolBar1.SetMaxSize(wx.Size(-1, -1))
        self.m_toolBar1.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)
        )
        self.m_toolBar1.SetMargins(wx.Size(2, 2))

        self.m_toolPrint = self.m_toolBar1.AddTool(
            wx.ID_PRINT,
            _("Drukuj"),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(varGlobals.path_icons_16 + "/Print-16x16.png"),
                    wx.BITMAP_TYPE_ANY,
                )
            ),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(
                        varGlobals.path_icons_16 + "/Disabled/Print-16x16.png"
                    ),
                    wx.BITMAP_TYPE_ANY,
                )
            ),
            wx.ITEM_NORMAL,
            _("Drukuj fakturę"),
            wx.EmptyString,
            None,
        )
        # self.m_toolInfo  = self.m_toolBar1.AddTool( wx.ID_INFO, _(u"Informacja"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_toolBar1.AddStretchableSpace()
        self.m_toolClose = self.m_toolBar1.AddTool(
            wx.ID_CLOSE,
            _("Zamknij"),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(varGlobals.path_icons_16 + "/Close-16x16.png"),
                    wx.BITMAP_TYPE_ANY,
                )
            ),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(
                        varGlobals.path_icons_16 + "/Disabled/Close-16x16.png"
                    ),
                    wx.BITMAP_TYPE_ANY,
                )
            ),
            wx.ITEM_NORMAL,
            _("Zamknij okno podglądu faktury"),
            wx.EmptyString,
            None,
        )
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
        self.Bind(wx.EVT_TOOL, self.onClose, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_TOOL, self.onPrint, id=wx.ID_PRINT)

    def onClose(self, e: wx.Event):
        self.htmlWinFa.Close()
        if self.tmp_html_file is not None:
            self.tmp_html_file.remove()
        self.Destroy()
        e.Skip()

    def onPrint(self, e: wx.Event):
        if self.htmlWinFa.IsBusy():
            winMessageBox(
                _("Proszę czekać, trwa ładowanie faktury..."),
                _("Drukowanie faktury"),
                wxdlg_const.ID_OK | wxdlg_const.ICON_INFO,
                self,
            )
            return

        self.htmlWinFa.Print()

    def load_invoice(self, xml_filename):
        parsing_ok = False
        self.tmp_html_file = fa_generate_html(
            fa_file=xml_filename, type_xsl="MF", silent=False
        )
        # print(html_body)

        if self.tmp_html_file is not None:
            absolute_path = (
                self.tmp_html_file.name
            )  # os.path.abspath(calculate_path(self.tmp_html_file.name))
            self.htmlWinFa.LoadURL(f"file:///{absolute_path}")
            self.InvoiceFilename = os.path.basename(xml_filename)
            parsing_ok = True

        return parsing_ok
