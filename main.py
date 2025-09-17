from Settings.global_var import varGlobals
from datetime import datetime
import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    app.SetAppName(varGlobals.app_title)
    app.SetVendorName("JUPIT Jacek Kruszniewski Usługi Programistyczne i Informatyczne")
    frame = winMain(None, varGlobals.app_title)
    frame.Show()
    app.MainLoop()