import wx
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

class winMain(wx.Frame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(1200, 800))
                
        self.Show()

    def mnuHandle(self, event: wx.Event):
        idEvent = event.GetId()
        if idEvent == self.MAIN_MENU_DBSETTINGS :
            frameSetupDB = frmDbSetup( self )            
            frameSetupDB.ShowModal()
        else:
            idAnswer = wx.MessageBox(
                message="Ustawienia programu " + str(idEvent),
                caption="Pytanie",
                style=wx.OK,        
            )
