import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    app_title = "Przeglądarka faktur KSEF"
    frame = winMain(None, )
    frame.Show()
    app.MainLoop()