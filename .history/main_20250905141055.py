import wx
from Frames.frmViewer import frmSetupApp

if __name__ == "__main__":
    app = wx.App()
    frame = frmSetupApp(None, "Instalacja systemu XYZ")
    frame.Show()
    app.MainLoop()