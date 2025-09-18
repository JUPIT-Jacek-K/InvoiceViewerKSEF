import gettext
import os

import wx

from Modules.misc import calculate_path
from Modules.wxExtention import TranslateWindowMenu
from Settings.global_var import varGlobals
from UI_Windows.winAbout import winAbout
from UI_Windows.winDialogs import winMessageBox, wxdlg_const
from UI_Windows.winInvoiceView import winInvoiceView

_ = gettext.gettext


class winMain(wx.MDIParentFrame):
    childs = []
    
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=wx.Size(1200, 800))

        self.menuBar = wx.MenuBar()
        self.menuProgram = wx.Menu()

        self.menuOpen = self.menuProgram.Append(
            wx.ID_OPEN, "Otwórz plik faktury", "Otwórz plik faktury"
        )
        self.menuExit = self.menuProgram.Append(
            wx.ID_EXIT, "Zamknij\tAlt-F4", "Zamknij aplikację"
        )
        self.menuBar.Append(self.menuProgram, "&Program")

        self.menuHelp = wx.Menu()
        self.menuAbout = self.menuHelp.Append(
            wx.ID_ABOUT, "O programie\tF1", "Informacje o programie"
        )
        self.menuBar.Append(self.menuHelp, "&Pomoc")

        '''
        self.menuWidows = wx.Menu()
        self.menuCascade = self.menuWidows.Append(
            wx.ID_MDI_WINDOW_CASCADE, "Kaskadowo", "Okna kaskadowo"
        )
        self.menuTileH = self.menuWidows.Append(
            wx.ID_MDI_WINDOW_TILE_HORZ, "Ułóż poziomo", "Okna ułóż poziomo"
        )
        self.menuTileV = self.menuWidows.Append(
            wx.ID_MDI_WINDOW_TILE_VERT, "Ułóż pionowo", "Okna ułóż pionowo"
        )
        self.menuArrangeIcons = self.menuWidows.Append(
            wx.ID_MDI_WINDOW_ARRANGE_ICONS, "Ułóż ikony", "Ułóż ikony"
        )

        self.windowsListMenu = wx.Menu()
        self.menuBar.Append(self.menuWidows, "&Okna")
        self.menuBar.Append(self.windowsListMenu, "&Lista Okien")
        self.SetWindowMenu(self.windowsListMenu)
        '''

        self.SetMenuBar(self.menuBar)
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
            wx.ID_OPEN,
            _("Otwórz plik faktury"),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(
                        varGlobals.path_icons_16 + "/Document-Open-16x16.png"
                    ),
                    wx.BITMAP_TYPE_ANY,
                )
            ),
            wx.BitmapBundle.FromBitmap(
                wx.Bitmap(
                    calculate_path(
                        varGlobals.path_icons_16 + "/Disabled/Document-16x16.png"
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
            wx.ID_EXIT,
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
            _("Zamknij program"),
            wx.EmptyString,
            None,
        )
        self.m_toolBar1.Realize()

        self.m_StatusBar = self.CreateStatusBar(1)

        self.Show()
        self.Bind(wx.EVT_MENU, self.menusEvents)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Bind(wx.EVT_TOOL, self.onClose, id=wx.ID_EXIT)
        self.Bind(wx.EVT_TOOL, self.onOpen, id=wx.ID_OPEN)

    def RegisterChild(self, child ):
        child.Bind(wx.EVT_CLOSE, self.onChildClose)
        self.childs.append( child)
        if len(self.childs) > 0:
            TranslateWindowMenu( self )


    def onChildClose(self, event : wx.CloseEvent):
        child = event.GetEventObject()
        # print("Usuwam Okno")
        if child in self.childs:
            self.childs.remove(child)
            child.Destroy()
        event.Skip()

    def onOpen(self, event):
        self.OpenInvoice()

    def menusEvents(self, event):
        id = event.GetId()
        if id == wx.ID_EXIT:
            self.onClose(event)
        elif id == wx.ID_OPEN:
            self.OpenInvoice()
        elif id == wx.ID_ABOUT:
            dlgAbout = winAbout()
            dlgAbout.ShowModal()
            dlgAbout.Destroy()

    def OpenInvoice(self):
        openFileDialog = wx.FileDialog(
            self,
            "Otwórz plik faktury",
            "",
            "",
            "Pliki faktur XML (*.xml)|*.xml",
            wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        )
        id_op = openFileDialog.ShowModal()
        if id_op == wx.ID_OK:
            path = openFileDialog.GetPath()
            for xchild in self.childs:
                if xchild.InvoiceFilename == os.path.basename(path):
                    xchild.Raise()
                    return
            
            mdiWinInvoice = winInvoiceView(
                self, f"Podgląd faktury - {os.path.basename(path)}"
            )
            if mdiWinInvoice.load_invoice(path):
                self.RegisterChild(mdiWinInvoice)
                mdiWinInvoice.Show()
                mdiWinInvoice.htmlWinFa.SetFocus()
            else:
                mdiWinInvoice.Destroy()
                mgg = winMessageBox(
                    "błąd xml",
                    "fa",
                    wxdlg_const.ID_OK | wxdlg_const.ICON_STOP,
                    self,
                )
                mgg.ShowModal()

        openFileDialog.Destroy()

    def onClose(self, event):
        msgMox = winMessageBox(
            "Czy zamknąć aplikację?",
            "Zamknięcie aplikacji",
            wxdlg_const.ID_YES_NO | wxdlg_const.ICON_ASK,
            self,
        )
        ii = msgMox.ShowModal()
        if ii == wxdlg_const.ID_YES:
            self.Destroy()
