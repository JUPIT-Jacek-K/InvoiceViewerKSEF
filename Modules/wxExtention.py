import wx


def TranslateWindowMenu(xMdiParent: wx.MDIParentFrame):
    menuOkno = xMdiParent.GetWindowMenu()  # Pobieramy menu okien
    if menuOkno is not None:
        items = menuOkno.GetMenuItems()
        for item in items:
            # print(f"Item ID: {item.GetId()}, Label: {item.GetItemLabel()}")
            if item.GetId() == wx.ID_MDI_WINDOW_CASCADE:
                item.SetItemLabel("&Kaskadowo")
            if item.GetId() == wx.ID_MDI_WINDOW_TILE_HORZ:
                item.SetItemLabel("Ułóż poziomo")
            if item.GetId() == wx.ID_MDI_WINDOW_TILE_VERT:
                item.SetItemLabel("Ułóż pionowo")
            if item.GetId() == wx.ID_MDI_WINDOW_ARRANGE_ICONS:
                item.SetItemLabel("Ułóż &ikony")
            if item.GetId() == wx.ID_MDI_WINDOW_NEXT:
                item.SetItemLabel("Okno &następne")
            if item.GetId() == wx.ID_MDI_WINDOW_PREV:
                item.SetItemLabel("Okno &poprzednie")
