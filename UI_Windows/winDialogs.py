import wx

from Modules.misc import calculate_path


class class_wxdlg_const(object):
    _YES = 0x0001
    _OK = 0x0002
    _SAVE = 0x0003
    _APPLY = 0x0004
    _SAVEAS = 0x0005
    _CLOSE = 0x0006
    _HELP = 0x0007
    _NO = 0x0010
    _CANCEL = 0x0020
    _ABORT = 0x0030
    _ICON_ASK = 0x0100
    _ICON_WARNING = 0x0200
    _ICON_STOP = 0x0300
    _ICON_ERROR = 0x0300
    _ICON_INFO = 0x0400
    _ICON_AUTH = 0x0500
    _ICON_NONE = 0xFF00
    _GRAPHICS_PATH = "Graphics/Icons/"

    def __init__(self):
        #
        self._Icons = {
            0x0100: self._GRAPHICS_PATH + "Ask_48x48.png",
            0x0200: self._GRAPHICS_PATH + "Warning_48x48.png",
            0x0300: self._GRAPHICS_PATH + "Error_48x48.png",
            0x0400: self._GRAPHICS_PATH + "Info_Circle_48x48.png",
            0x0500: self._GRAPHICS_PATH + "Padlock_close_48x48.png.png",
        }

        self._Options = {
            self._YES: {
                "caption": "Tak",
                "wxId": wx.ID_YES,
                "icon": self._GRAPHICS_PATH + "Yes_24x24.png",
            },
            self._OK: {
                "caption": "OK",
                "wxId": wx.ID_OK,
                "icon": self._GRAPHICS_PATH + "Yes_24x24.png",
            },
            self._SAVE: {
                "caption": "Zapisz",
                "wxId": wx.ID_SAVE,
                "icon": self._GRAPHICS_PATH + "Save_24x24.png",
            },
            self._APPLY: {
                "caption": "Zastosuj",
                "wxId": wx.ID_APPLY,
                "icon": self._GRAPHICS_PATH + "Apply_24x24.png",
            },
            self._SAVEAS: {
                "caption": "Zapisz jako",
                "wxId": wx.ID_SAVEAS,
                "icon": self._GRAPHICS_PATH + "SaveAs_24x24.png",
            },
            self._CLOSE: {
                "caption": "Zamknij",
                "wxId": wx.ID_CLOSE,
                "icon": self._GRAPHICS_PATH + "Close_24x24.png",
            },
            self._HELP: {
                "caption": "Pomoc",
                "wxId": wx.ID_HELP,
                "icon": self._GRAPHICS_PATH + "Help_24x24.png",
            },
            self._NO: {
                "caption": "Nie",
                "wxId": wx.ID_NO,
                "icon": self._GRAPHICS_PATH + "No_24x24.png",
            },
            self._CANCEL: {
                "caption": "Anuluj",
                "wxId": wx.ID_CANCEL,
                "icon": self._GRAPHICS_PATH + "No_24x24.png",
            },
            self._ABORT: {
                "caption": "Porzuć",
                "wxId": wx.ID_ABORT,
                "icon": self._GRAPHICS_PATH + "No_Circle_24x24.png",
            },
        }

    # simple

    @property
    def ID_YES(self):
        return self._YES

    @property
    def ID_OK(self):
        return self._OK

    @property
    def ID_SAVE(self):
        return self._SAVE

    @property
    def ID_SAVEAS(self):
        return self._SAVEAS

    @property
    def ID_APPLY(self):
        return self._APPLY

    @property
    def ID_CLOSE(self):
        return self._CLOSE

    @property
    def ID_HELP(self):
        return self._HELP

    @property
    def ID_NO(self):
        return self._NO

    @property
    def ID_CANCEL(self):
        return self._CANCEL

    # combinations
    @property
    def ID_YES_NO(self):
        return self._YES | self._NO

    @property
    def ID_OK_CANCEL(self):
        return self._OK | self._CANCEL

    @property
    def ID_SAVE_CANCEL(self):
        return self._SAVE | self._CANCEL

    @property
    def ID_SAVEAS_CANCEL(self):
        return self._SAVEAS | self._CANCEL

    @property
    def ID_SAVE2_CANCEL(self):
        return self._SAVE | self._SAVEAS | self._CANCEL

    @property
    def ID_SAVE_NO(self):
        return self._SAVE | self._NO

    @property
    def ID_SAVEAS_NO(self):
        return self._SAVEAS | self._NO

    @property
    def ID_SAVE_SAVEAS_NO(self):
        return self._SAVE | self._SAVEAS | self._NO

    @property
    def ID_SAVE_ABORT(self):
        return self._SAVE | self._ABORT

    @property
    def ID_SAVEAS_ABORT(self):
        return self._SAVEAS | self._ABORT

    @property
    def ID_SAVE_SAVEAS_ABORT(self):
        return self._SAVE | self._SAVEAS | self._ABORT

    @property
    def ID_APPLY_CANCEL(self):
        return self._APPLY | self._CANCEL

    @property
    def ID_APPLY_NO(self):
        return self._APPLY | self._NO

    @property
    def ID_APPLY_ABORT(self):
        return self._APPLY | self._ABORT

    @property
    def ICON_ASK(self):
        return self._ICON_ASK

    @property
    def ICON_WARNING(self):
        return self._ICON_WARNING

    @property
    def ICON_STOP(self):
        return self._ICON_STOP

    @property
    def ICON_ERROR(self):
        return self._ICON_ERROR

    @property
    def ICON_INFO(self):
        return self._ICON_INFO

    @property
    def ICON_AUTH(self):
        return self._ICON_AUTH

    @property
    def ICON_NONE(self):
        return self._ICON_NONE

    @property
    def GRAPHICS_PATH(self):
        return self._GRAPHICS_PATH

    def IconMessage(self, xwin, status: int):
        xIcon = None
        if (
            status == self._ICON_ASK
            or status == self._ICON_WARNING
            or status == self._ICON_ERROR
            or status == self._ICON_INFO
            or status == self._ICON_AUTH
        ):
            xIcon = wx.StaticBitmap(
                xwin,
                wx.ID_ANY,
                wx.Bitmap(calculate_path(self._Icons[status]), wx.BITMAP_TYPE_ANY),
                wx.DefaultPosition,
                wx.DefaultSize,
                0,
            )

        return xIcon

    def Button(self, parent, status: int):
        if (
            status == self._YES
            or status == self._OK
            or status == self._SAVE
            or status == self._APPLY
            or status == self._SAVEAS
            or status == self._HELP
            or status == self._NO
            or status == self._CANCEL
            or status == self._CLOSE
            or status == self._ABORT
        ):
            xButton = wx.Button(
                parent, self._Options[status]["wxId"], self._Options[status]["caption"]
            )
            xButton.SetBitmapLabel(
                wx.Bitmap(
                    calculate_path(self._Options[status]["icon"]), wx.BITMAP_TYPE_ANY
                )
            )

        else:
            xButton = wx.Button(
                parent,
                self._Options[self._CLOSE]["wxId"],
                self._Options[self._CLOSE]["caption"],
            )
        return xButton


wxdlg_const = class_wxdlg_const()


class winMessageBox(wx.Dialog):
    def __init__(
        self, message: str, caption: str, style: int, parent: wx.Window | None = None
    ):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=caption,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=0 | wx.CAPTION,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.panelMessage = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        self.panelMessage.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        )
        self.panelMessage.SetMinSize(size=(-1, -1))

        s_hGap = 5
        s_bMarg = 5
        s_MaxWWText = 500

        messageSizer = wx.FlexGridSizer(1, 2, 5, s_hGap)
        messageSizer.SetFlexibleDirection(wx.BOTH)
        messageSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        if not ((style & wxdlg_const.ICON_NONE) == wxdlg_const.ICON_NONE):
            self.m_bitmap1 = wxdlg_const.IconMessage(
                self.panelMessage, style & wxdlg_const.ICON_NONE
            )
            if self.m_bitmap1 is not None:
                messageSizer.Add(self.m_bitmap1, 0, wx.ALL, s_bMarg)

        self.m_staticText5 = wx.StaticText(
            self.panelMessage, wx.ID_ANY, message, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText5.Wrap(s_MaxWWText)

        text_size = self.m_staticText5.GetSize()
        if text_size.GetWidth() < 200:
            self.m_staticText5.SetMinSize((200, -1))

        messageSizer.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.panelMessage.SetSizer(messageSizer)
        self.panelMessage.Layout()
        messageSizer.Fit(self.panelMessage)

        mainSizer.Add(self.panelMessage, 1, wx.EXPAND | wx.ALL, 5)

        buttonsSizer = wx.StdDialogButtonSizer()

        if (style & wxdlg_const.ID_OK) == wxdlg_const.ID_OK:
            self.buttonsSizerOK = wxdlg_const.Button(self, wxdlg_const.ID_OK)
            buttonsSizer.AddButton(self.buttonsSizerOK)
            self.buttonsSizerOK.Bind(wx.EVT_BUTTON, self.onClickOK)

        if (style & wxdlg_const.ID_YES) == wxdlg_const.ID_YES:
            self.buttonsSizerYes = wxdlg_const.Button(self, wxdlg_const.ID_YES)
            buttonsSizer.AddButton(self.buttonsSizerYes)
            self.buttonsSizerYes.Bind(wx.EVT_BUTTON, self.onClickkYes)

        if (style & wxdlg_const.ID_SAVE) == wxdlg_const.ID_SAVE:
            self.buttonsSizerSave = wxdlg_const.Button(self, wxdlg_const.ID_SAVE)
            buttonsSizer.AddButton(self.buttonsSizerSave)
            self.buttonsSizerSave.Bind(wx.EVT_BUTTON, self.onClickSave)

        if (style & wxdlg_const.ID_APPLY) == wxdlg_const.ID_APPLY:
            self.buttonsSizerApply = wxdlg_const.Button(self, wxdlg_const.ID_APPLY)
            buttonsSizer.AddButton(self.buttonsSizerSave)
            self.buttonsSizerApply.Bind(wx.EVT_BUTTON, self.onClickApply)

        if (style & wxdlg_const.ID_CLOSE) == wxdlg_const.ID_CLOSE:
            self.buttonsSizerClose = wxdlg_const.Button(self, wxdlg_const.ID_CLOSE)
            buttonsSizer.AddButton(self.buttonsSizerClose)
            self.buttonsSizerClose.Bind(wx.EVT_BUTTON, self.onClickClose)

        if (style & wxdlg_const.ID_NO) == wxdlg_const.ID_NO:
            self.buttonsSizerNo = wxdlg_const.Button(self, wxdlg_const.ID_NO)
            buttonsSizer.AddButton(self.buttonsSizerNo)
            self.buttonsSizerNo.Bind(wx.EVT_BUTTON, self.onClickNo)

        if (style & wxdlg_const.ID_CANCEL) == wxdlg_const.ID_CANCEL:
            self.buttonsSizerCancel = wxdlg_const.Button(self, wxdlg_const.ID_CANCEL)
            buttonsSizer.AddButton(self.buttonsSizerCancel)
            self.buttonsSizerCancel.Bind(wx.EVT_BUTTON, self.onClickCancel)

        if (style & wxdlg_const.ID_HELP) == wxdlg_const.ID_HELP:
            self.buttonsSizerHelp = wxdlg_const.Button(self, wxdlg_const.ID_HELP)
            buttonsSizer.AddButton(self.buttonsSizerCancel)
            self.buttonsSizerHelp.Bind(wx.EVT_BUTTON, self.onClickHelp)

        buttonsSizer.Realize()
        buttonsSizer.SetMinSize(-1, 50)
        mainSizer.Add(buttonsSizer, 0, wx.EXPAND, 5)

        self.SetSizer(mainSizer)
        self.Layout()
        mainSizer.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def onClickOK(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_OK)

    def onClickkYes(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_YES)

    def onClickSave(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_SAVE)

    def onClickApply(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_APPLY)

    def onClickClose(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_CLOSE)

    def onClickNo(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_NO)

    def onClickCancel(self, xEvent: wx.Event):
        self.EndModal(wxdlg_const.ID_CANCEL)

    def onClickHelp(self, xEvent: wx.Event):
        pass


def MyMessageBox():
    pass
