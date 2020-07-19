import wx 
from wxlogic import myframe

if __name__ =='__main__':
    app = wx.App() 
    frame = myframe(None)
    frame.Show(True)
    app.MainLoop()