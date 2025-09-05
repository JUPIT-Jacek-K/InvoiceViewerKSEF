import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    app_title = "Przeglądarka faktur KSEF"
    app_v
    frame = winMain(None, app_title)
    frame.Show()
    app.MainLoop()