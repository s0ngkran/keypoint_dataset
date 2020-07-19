# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"keypoint generator", pos = wx.Point( 0,0 ), size = wx.Size( 680,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 600,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menuItem_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open ImgFolder", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_open.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_MENU ) )
		self.menu_file.Append( self.menuItem_open )

		self.menuItem_save = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_save.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE_AS, wx.ART_MENU ) )
		self.menu_file.Append( self.menuItem_save )

		self.menu_file.AppendSeparator()

		self.menuItem_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Exit program", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_exit.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_ERROR, wx.ART_MENU ) )
		self.menu_file.Append( self.menuItem_exit )

		self.m_menubar1.Append( self.menu_file, u"File" )

		self.menu_camera = wx.Menu()
		self.m_menu1 = wx.Menu()
		self.m_menuItem17 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Show", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem17.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu1.Append( self.m_menuItem17 )

		self.m_menuItem18 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Hide", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem18.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu1.Append( self.m_menuItem18 )
		self.m_menuItem18.Check( True )

		self.menu_camera.AppendSubMenu( self.m_menu1, u"Tracking ROI" )

		self.m_menu11 = wx.Menu()
		self.m_menuItem171 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Show", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem171.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem171 )
		self.m_menuItem171.Check( True )

		self.m_menuItem181 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Hide", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem181.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem181 )

		self.m_menu11.AppendSeparator()

		self.m_menuItem173 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"size 1", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem173.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem173 )

		self.m_menuItem19 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"size 2", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem19.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem19 )

		self.m_menuItem20 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"size 3", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem20.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem20 )
		self.m_menuItem20.Check( True )

		self.m_menuItem21 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"size 5", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem21.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem21 )

		self.m_menuItem22 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"size 10", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem22.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu11.Append( self.m_menuItem22 )

		self.menu_camera.AppendSubMenu( self.m_menu11, u"Keypoint" )

		self.m_menu12 = wx.Menu()
		self.m_menuItem172 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"Show", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem172.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu12.Append( self.m_menuItem172 )
		self.m_menuItem172.Check( True )

		self.m_menuItem182 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"Hide", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem182.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu12.Append( self.m_menuItem182 )

		self.menu_camera.AppendSubMenu( self.m_menu12, u"Links of Keypoint" )

		self.m_menubar1.Append( self.menu_camera, u"Views" )

		self.menu_camera1 = wx.Menu()
		self.menuItem_opencam2 = wx.MenuItem( self.menu_camera1, wx.ID_ANY, u"init camera", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_opencam2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND, wx.ART_MENU ) )
		self.menu_camera1.Append( self.menuItem_opencam2 )

		self.menuItem_opencam12 = wx.MenuItem( self.menu_camera1, wx.ID_ANY, u"record...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_opencam12.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_MENU ) )
		self.menu_camera1.Append( self.menuItem_opencam12 )

		self.menuItem_opencam111 = wx.MenuItem( self.menu_camera1, wx.ID_ANY, u"stop recording", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_opencam111.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_MENU ) )
		self.menu_camera1.Append( self.menuItem_opencam111 )

		self.m_menubar1.Append( self.menu_camera1, u"Camera" )

		self.menu_track = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.menu_track, wx.ID_ANY, u"init tracker", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem6.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_MENU ) )
		self.menu_track.Append( self.m_menuItem6 )

		self.m_menu4_size = wx.Menu()
		self.m_menuItem17311 = wx.MenuItem( self.m_menu4_size, wx.ID_ANY, u"size 30", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem17311.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu4_size.Append( self.m_menuItem17311 )

		self.m_menuItem17312 = wx.MenuItem( self.m_menu4_size, wx.ID_ANY, u"size 40", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem17312.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu4_size.Append( self.m_menuItem17312 )

		self.m_menuItem17313 = wx.MenuItem( self.m_menu4_size, wx.ID_ANY, u"size 50", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem17313.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu4_size.Append( self.m_menuItem17313 )
		self.m_menuItem17313.Check( True )

		self.m_menuItem17314 = wx.MenuItem( self.m_menu4_size, wx.ID_ANY, u"size 60", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem17314.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_MENU ) )
		self.m_menu4_size.Append( self.m_menuItem17314 )

		self.m_menuItem35 = wx.MenuItem( self.m_menu4_size, wx.ID_ANY, u"size 100", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4_size.Append( self.m_menuItem35 )

		self.menu_track.AppendSubMenu( self.m_menu4_size, u"size" )

		self.m_menuItem61 = wx.MenuItem( self.menu_track, wx.ID_ANY, u"reserve...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem61.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_MENU ) )
		self.menu_track.Append( self.m_menuItem61 )

		self.m_menubar1.Append( self.menu_track, u"Tracker" )

		self.menu_check = wx.Menu()
		self.menuItem_open_a_data = wx.MenuItem( self.menu_check, wx.ID_ANY, u"open a data", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_open_a_data.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_MENU ) )
		self.menu_check.Append( self.menuItem_open_a_data )

		self.menuItem_open_a_folder = wx.MenuItem( self.menu_check, wx.ID_ANY, u"open a folder", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_open_a_folder.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR ) )
		self.menu_check.Append( self.menuItem_open_a_folder )

		self.m_menubar1.Append( self.menu_check, u"Check" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_bitmap5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_DEFAULT|wx.BORDER_SIMPLE )
		self.m_bitmap5.SetMinSize( wx.Size( 500,500 ) )
		self.m_bitmap5.SetMaxSize( wx.Size( 500,500 ) )

		self.m_mgr.AddPane( self.m_bitmap5, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Fixed().DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ).MinSize( wx.Size( 500,500 ) ).MaxSize( wx.Size( 500,500 ) ).Layer( 1 ) )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"go... .bmp", wx.Point( -1,0 ), wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMaxLength( 10 )
		self.m_textCtrl3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		self.m_mgr.AddPane( self.m_textCtrl3, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Dock().Fixed().DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ).Row( 0 ).BestSize( wx.Size( 120,30 ) ) )

		self.m_button11 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		self.m_button11.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_LAST, wx.ART_BUTTON ) )
		self.m_button11.SetBitmapPosition( wx.LEFT )
		self.m_button11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_mgr.AddPane( self.m_button11, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Movable( False ).Dock().Fixed() )

		self.m_button111 = wx.Button( self, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button111.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		self.m_button111.SetBitmapPosition( wx.LEFT )
		self.m_button111.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button111.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button111, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_BUTTON ) )
		self.m_button1.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button1.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button1, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button12.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_BUTTON ) )
		self.m_button12.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button12.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button12, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button13.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_CUT, wx.ART_BUTTON ) )
		self.m_button13.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button13.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button13, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button14.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		self.m_button14.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button14.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button14, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button141 = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button141.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		self.m_button141.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button141.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button141, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_button142 = wx.Button( self, wx.ID_ANY, u"reserve...", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )

		self.m_button142.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		self.m_button142.SetMinSize( wx.Size( 700,-1 ) )
		self.m_button142.SetMaxSize( wx.Size( 700,-1 ) )

		self.m_mgr.AddPane( self.m_button142, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )


		self.m_mgr.Update()
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_imgfolder, id = self.menuItem_open.GetId() )
		self.Bind( wx.EVT_MENU, self.save_mp4, id = self.menuItem_save.GetId() )
		self.Bind( wx.EVT_MENU, self.exit_program, id = self.menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.roi_show, id = self.m_menuItem17.GetId() )
		self.Bind( wx.EVT_MENU, self.roi_hide, id = self.m_menuItem18.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_show, id = self.m_menuItem171.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_hide, id = self.m_menuItem181.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_size1, id = self.m_menuItem173.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_size2, id = self.m_menuItem19.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_size3, id = self.m_menuItem20.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_size5, id = self.m_menuItem21.GetId() )
		self.Bind( wx.EVT_MENU, self.keypoint_size10, id = self.m_menuItem22.GetId() )
		self.Bind( wx.EVT_MENU, self.link_show, id = self.m_menuItem172.GetId() )
		self.Bind( wx.EVT_MENU, self.link_hide, id = self.m_menuItem182.GetId() )
		self.Bind( wx.EVT_MENU, self.opencam, id = self.menuItem_opencam2.GetId() )
		self.Bind( wx.EVT_MENU, self.take_video, id = self.menuItem_opencam12.GetId() )
		self.Bind( wx.EVT_MENU, self.stop_recording, id = self.menuItem_opencam111.GetId() )
		self.Bind( wx.EVT_MENU, self.init_tracker, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.tracking_size_30, id = self.m_menuItem17311.GetId() )
		self.Bind( wx.EVT_MENU, self.tracking_size_40, id = self.m_menuItem17312.GetId() )
		self.Bind( wx.EVT_MENU, self.tracking_size_50, id = self.m_menuItem17313.GetId() )
		self.Bind( wx.EVT_MENU, self.tracking_size_60, id = self.m_menuItem17314.GetId() )
		self.Bind( wx.EVT_MENU, self.tracking_size_100, id = self.m_menuItem35.GetId() )
		self.Bind( wx.EVT_MENU, self.start_track, id = self.m_menuItem61.GetId() )
		self.Bind( wx.EVT_MENU, self.open_a_data, id = self.menuItem_open_a_data.GetId() )
		self.Bind( wx.EVT_MENU, self.open_a_folder, id = self.menuItem_open_a_folder.GetId() )
		self.m_textCtrl3.Bind( wx.EVT_KEY_UP, self.key_on_go_bmp )
		self.m_textCtrl3.Bind( wx.EVT_LEFT_DOWN, self.click_on_go_bmp )
		self.m_button11.Bind( wx.EVT_BUTTON, self.goto_img )
		self.m_button111.Bind( wx.EVT_BUTTON, self.Previous )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Next )
		self.m_button12.Bind( wx.EVT_BUTTON, self.Back )
		self.m_button13.Bind( wx.EVT_BUTTON, self.Clear )
		self.m_button14.Bind( wx.EVT_BUTTON, self.Save )
		self.m_button141.Bind( wx.EVT_BUTTON, self.Reset )
		self.m_button142.Bind( wx.EVT_BUTTON, self.testmode )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, overide them in your derived class
	def open_imgfolder( self, event ):
		event.Skip()

	def save_mp4( self, event ):
		event.Skip()

	def exit_program( self, event ):
		event.Skip()

	def roi_show( self, event ):
		event.Skip()

	def roi_hide( self, event ):
		event.Skip()

	def keypoint_show( self, event ):
		event.Skip()

	def keypoint_hide( self, event ):
		event.Skip()

	def keypoint_size1( self, event ):
		event.Skip()

	def keypoint_size2( self, event ):
		event.Skip()

	def keypoint_size3( self, event ):
		event.Skip()

	def keypoint_size5( self, event ):
		event.Skip()

	def keypoint_size10( self, event ):
		event.Skip()

	def link_show( self, event ):
		event.Skip()

	def link_hide( self, event ):
		event.Skip()

	def opencam( self, event ):
		event.Skip()

	def take_video( self, event ):
		event.Skip()

	def stop_recording( self, event ):
		event.Skip()

	def init_tracker( self, event ):
		event.Skip()

	def tracking_size_30( self, event ):
		event.Skip()

	def tracking_size_40( self, event ):
		event.Skip()

	def tracking_size_50( self, event ):
		event.Skip()

	def tracking_size_60( self, event ):
		event.Skip()

	def tracking_size_100( self, event ):
		event.Skip()

	def start_track( self, event ):
		event.Skip()

	def open_a_data( self, event ):
		event.Skip()

	def open_a_folder( self, event ):
		event.Skip()

	def key_on_go_bmp( self, event ):
		event.Skip()

	def click_on_go_bmp( self, event ):
		event.Skip()

	def goto_img( self, event ):
		event.Skip()

	def Previous( self, event ):
		event.Skip()

	def Next( self, event ):
		event.Skip()

	def Back( self, event ):
		event.Skip()

	def Clear( self, event ):
		event.Skip()

	def Save( self, event ):
		event.Skip()

	def Reset( self, event ):
		event.Skip()

	def testmode( self, event ):
		event.Skip()


