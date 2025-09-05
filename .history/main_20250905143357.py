import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    app_title = "Przeglądarka faktur KSEF"
    app_version = "v. 1.0.0"
    app.SetAppName(app_title)
    app.SetVe
    frame = winMain(None, app_title)
    frame.Show()
    app.MainLoop()