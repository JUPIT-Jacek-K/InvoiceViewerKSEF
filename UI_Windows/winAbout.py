import wx
import wx.html
import webbrowser

from Modules.misc import calculate_path
from Settings.global_var import varGlobals
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

class custonHtmlWindow( wx.html.HtmlWindow):
    def __init__( parent: wx.Window | None, id: int = wx.ID_ANY, pos: wx.Point = wx.DefaultPosition, size: wx.Size = wx.DefaultSize, style: int = wx.html.HW_DEFAULT_STYLE, name: str = "htmlWindow" ):
        wx.html.HtmlWindow.__init__( parent, id, pos, size, style, name)

    def OnHTMLLinkClicked(self, link: wx.html.HtmlLinkInfo):
        winWAsk = winMessageBox("Kliknąłęś na odnośnik do projektyna GitHub.\nCzy otworzyć projekt w preglądarce?","Otwarcie strony GitHub", wxdlg_const.ICON_ASK | wxdlg_const.ID_YES_NO)
        idAsk = winWAsk.ShowModal()
        if idAsk == wxdlg_const.ID_YES:
            webbrowser.open_new_tab( link.GetHref() )
        winWAsk.Destroy()


class winAbout(wx.Dialog):
    htnlInfo = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>O programie</title>
    </head>
        <h1 align="center">Program "{varGlobals.app_title}"</h1>
        <p align="center">
            Wersja: <b>{varGlobals.app_version}</b>
        </p>
        <hr>
        <p>Program do przeglądanie zawartości eleftronicznych faktur w formacie KSeF (Krajowy System eFaktur) w wersjach FA(1), FA(2), FA(3)<br>    
        Program te jest programem utworzonym w ramach nauki języka pythom</p>
        <h2>Autor:</h2>
        <p><b>Jacekk Kruszniewski (JUPIT Jacek Kruszniewsk Usługi Programistyczne i Informatyczne)</b><br>
        {varGlobals.app_year_from} – {varGlobals.app_year_to}</p>
        <p>Projekt jest dostępny na serwerze GitHub <a href="https://github.com/JUPIT-Jacek-K/InvoiceViewerKSEF" target="_blank">JUPIT-Jacek-K/InvoiceViewerKSEF</a></p>
        <p><br>
        </p>
    </body>
</html>
"""

    def __init__(self):
        wx.Dialog.__init__(
            self,
            None,
            id=wx.ID_ANY,
            title="O programie",
            pos=wx.DefaultPosition,
            size=wx.Size(600, 600),
            style=wx.CAPTION | wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.infoPanel = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )

        messageSizer = wx.FlexGridSizer(1, 2, 5, 0)
        messageSizer.SetFlexibleDirection(wx.BOTH)
        messageSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.aboutImage = wx.StaticBitmap(
            self.infoPanel,
            wx.ID_ANY,
            wx.Bitmap(
                calculate_path("Graphics/About/aboutImage.png"), wx.BITMAP_TYPE_ANY
            ),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )

        messageSizer.Add(self.aboutImage, 0, 0, 5)

        self.m_htmlWinAbout = custonHtmlWindow( # wx.html.HtmlWindow
            self.infoPanel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.Size(400, 400),
            wx.html.HW_NO_SELECTION | wx.html.HW_SCROLLBAR_NEVER,
        )
        self.infoPanel.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT)
        )
        messageSizer.Add(self.m_htmlWinAbout, 0, wx.ALL | wx.EXPAND, 5)
        self.m_htmlWinAbout.SetPage(self.htnlInfo)
        self.m_htmlWinAbout.SetStandardFonts(
            size=9, normal_face="helvetica", fixed_face="Sans Serif"
        )
        self.m_htmlWinAbout.SetHTMLBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT)
        )

        self.infoPanel.SetSizer(messageSizer)

        buttonsSizer = wx.StdDialogButtonSizer()
        self.buttonsSizerClose = wxdlg_const.Button(self, wxdlg_const.ID_CLOSE)
        buttonsSizer.AddButton(self.buttonsSizerClose)
        self.buttonsSizerClose.Bind(wx.EVT_BUTTON, self.onClickClose)
        buttonsSizer.Realize()
        self.infoPanel.Layout()

        mainSizer.Add(self.infoPanel)
        buttonsSizer.SetMinSize(-1, 50)
        mainSizer.Add(buttonsSizer, 0, wx.EXPAND, 5)

        self.SetSizer(mainSizer)
        self.Layout()
        mainSizer.Fit(self)

        self.Centre(wx.BOTH)

    def onClickClose(self, event: wx.Event):
        self.EndModal(wxdlg_const.ID_CLOSE)
