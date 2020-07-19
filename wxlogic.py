import wx 
from wxui import MyFrame1 
import cv2
import threading
import time
import numpy as np
import os
import pickle
import copy
class Stage:
    def __init__(self, folder):
        self.path = os.path.join(folder,'stage.txt')
        self.append('starting')
    def append(self, text):
        with open(self.path,'a') as f:
            f.write(text+'\n')
    def lastest(self):
        with open(self.path,'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
        if last_line == 'starting':
            try:
                last_line = lines[-2]
            except:
                pass
        if last_line == 'starting': 
            last_line = 0
        return int(last_line)
class MyTracker():
    def __init__(self, cvimg, point, tracker_size=10):
        offset = tracker_size
        # roi = (left, top, width, height)
        self.center = point
        cx, cy = point[0], point[1]
        self.roi = cx-offset/2, cy-offset/2, offset, offset
        self.tracker = cv2.TrackerCSRT_create()
        self.tracker.init(cvimg, self.roi)

    def update(self, cvimg):
        success, self.roi = self.tracker.update(cvimg)
        left, top, width, height = self.roi
        self.center = left+width/2, top+height/2

class myframe(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.saving_img_swap = False
        self.finish_setimg_temp = False
        self.init_cam = False
        self.currentpath = os.path.dirname(__file__)
        self.init_tracker_ = False
        self.init_open_imgfolder = False
        wx.Log.EnableLogging(False)
        self.color_hand = [wx.GREEN, wx.Colour(125, 60, 152), wx.GREEN, wx.BLUE,wx.BLUE]
        self.links = [[0,1] ,[0,3] ,[0,5] ,[0,7] ,[0,9], [1,2], [3,4], [5,6], [7,8], [9,10]]
        self.roi_show_ = False
        self.keypoint_show_ = True
        self.link_show_ = True
        self.left_swap = False
        self.move_point = False
        self.covered_point = [False for i in range(11)]
        self.real_img = []
        self.keypoint_size = 3
        self.tracking_roi_size = 50



    def save_mp4( self, event ):
        event.Skip()

    def exit_program( self, event ):
        self.stop_cam = True
        self.cap_release(event)

    def opencam( self, event ):
        self.startcap()
        self.log('croped image from camera (1280,720)=>(720,720)')
        self.create_thread(self.show_img)
    def create_thread(self, target):
        thread = threading.Thread(target=target)
        #thread.daemon = True
        thread.start()
    def startcap(self):
        self.log('init video capture...')
        self.cap_ = cv2.VideoCapture(0)
        self.log('set video size to (1280, 720) ...')
        self.cap_.set(3, 1280)
        self.cap_.set(4, 720)
        
        
    def log(self, text):
        self.m_statusBar1.SetStatusText(text)
    def init_sav_vid(self):
        self.init_cam = True
        self.stop_cam = False
        self.imi = 0
        self.vid_saving = False
        self.take_video_on = False
        self.cnt = 'init'
        self.vid_saving_end = False
  
    def show_img(self):
        self.init_sav_vid()
        cnt = 'init'
        swap3 = self.vid_saving_end
        while not self.stop_cam:
            if swap3 != self.vid_saving_end:
                swap3 = self.vid_saving_end
                cnt = 'init'
                
            _, frame = self.cap_.read()
            w, h = 720, 720
            x, y = 1280/2-w/2, 720/2-h/2
            x, y, w, h = int(x), int(y), int(w), int(h)
            frame = frame[y:y+h, x:x+w]
            frame = cv2.flip(frame, 1)
            if self.take_video_on:
                if cnt == 'init':
                    t0 = time.time()
                    cnt = 3
                elif time.time()-t0 > 1 and cnt > 0:
                    t0 = time.time()
                    cnt -= 1
                elif cnt < 1:
                    self.take_video_on = False
                    self.vid_saving = True
            # if self.vid_saving:
            #     wx.CallAfter(self.after_show_img, 2, frame=frame)
            
                font = cv2.FONT_HERSHEY_SIMPLEX 
                org = int(720/2), int(720/2)
                fontScale = 3
                color = (255,0,255)
                thickness = 5
                frame = cv2.putText(frame, str(cnt), org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)

            # write to save
            if self.vid_saving:
                swap2 = self.saving_img_swap
                wx.CallAfter(self.saving_img, frame)
                while self.saving_img_swap == swap2:
                    time.sleep(0.01)
        
            # resize and write to show
            frame = self.resize_cv2(frame, (500-2)/720)
            dir_temp = os.path.join(os.path.dirname(__file__)
                    ,'cv2_temp.bmp')
            swap = self.finish_setimg_temp

            # put on showing img
            if self.vid_saving:
                font = cv2.FONT_HERSHEY_SIMPLEX 
                org = 15,29
                fontScale = 1
                color = (0,255,0)
                thickness = 2
                frame = cv2.putText(frame, 'recording...', org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)
            if self.take_video_on:
                font = cv2.FONT_HERSHEY_SIMPLEX 
                org = 15,29
                fontScale = 1
                color = (255,10,255)
                thickness = 2
                frame = cv2.putText(frame, 'record in', org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)

            cv2.imwrite(dir_temp, frame)
            wx.CallAfter(self.add_static_img, dir_temp)
            
            while self.finish_setimg_temp == swap :
                time.sleep(0.01)
     
    def saving_img(self, frame):
        self.log('start saving...')
        self.imi += 1
        dir_imi = 'video_temp/'+str(self.fol).zfill(2)+'/'+str(self.imi).zfill(10)+'.bmp'
        cv2.imwrite(dir_imi,frame)
        self.log('saved %s'%dir_imi)
        self.saving_img_swap = not self.saving_img_swap
        self.vid_saving_end = True

    def resize_cv2(self, img, scale):
        scale_percent = scale*100
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return resized
    def add_static_img(self, frame_location):
        wximg = wx.Bitmap(frame_location, wx.BITMAP_TYPE_ANY)
        self.m_bitmap5.SetBitmap(wximg)
        self.m_mgr.Update()
        self.finish_setimg_temp = not self.finish_setimg_temp

    def take_video( self, event ):
        if self.init_cam:
            self.mkfolder('video_temp')
            stage = Stage('video_temp')
            self.fol = stage.lastest() + 1
            stage.append(str(self.fol))
            self.mkfolder('video_temp/'+str(self.fol).zfill(2))
            self.take_video_on = True
            self.log('count down to take image...')
        else:
            wx.MessageBox('You have to init camera first.', 'Cannot record !',wx.OK )
    def stop_recording(self, event):
        if self.init_cam and self.vid_saving:
            self.init_sav_vid()
            self.log('remanage (.bmp) image file')

            # renew image due to some bugs of Thread.
            dir_temp = os.path.join('video_temp',str(self.fol).zfill(2))
            for _,_,fname in os.walk(dir_temp):
                pass 
            
            # remove 1, 2, 3, 4
            # rename 2->1, 4->2, 6->3
            for i in range(int(len(fname)/2)):
                newi = (i+1)*2
                oldi = newi - 1
                ci = i+1

                name_newi = str(newi).zfill(10)+'.bmp'
                dir_name_newi = os.path.join(dir_temp, name_newi)
                
                name_oldi = str(oldi).zfill(10)+'.bmp'
                dir_name_oldi = os.path.join(dir_temp, name_oldi)

                name_ci = str(ci).zfill(10)+'.bmp'
                dir_name_ci = os.path.join(dir_temp, name_ci)
                
                os.remove(dir_name_oldi)
                os.rename(dir_name_newi, dir_name_ci)
            try: 
                i = len(fname)
                namei = str(i).zfill(10)+'.bmp'
                dir_namei = os.path.join(dir_temp, namei)
                os.remove(dir_namei)
            except :pass
            self.log('done %d images in %s'%(int(len(fname)/2),dir_temp))
        else: 
            wx.MessageBox('There are no recording videos.', 'Cannot stop !',wx.OK )
    def mkfolder(self, name):
        if name not in os.listdir():
            os.mkdir(name)
            self.log('make___ (%s) ___folder'%name)
        else:
            self.log('found___ (%s) ___before make'%name)

    def open_imgfolder(self, event):
        self.init_open_imgfolder = True
        fdir = ""  

        try:
            dir_temp = os.path.join(self.currentpath, 'video_temp')
            dlg = wx.DirDialog(self, defaultPath = dir_temp)
        except:        
            dlg = wx.DirDialog(self, defaultPath = self.currentpath)
        
        if dlg.ShowModal() == wx.ID_OK:
            fdir = dlg.GetPath()
            dlg.SetPath(fdir)
        dlg.Destroy()

        self.img_folder = fdir
        self.imi = 1
        try:
            self.cap_.release()
        except :pass
        self.stop_cam = True # stop showing camera
        self.show_imi(self.imi)
        self.init_tracker(event)
    def show_imi(self, i):
        self.imi_path = os.path.join(self.img_folder
                    , str(i).zfill(10)+'.bmp')
        wximg = wx.Bitmap(self.imi_path, wx.BITMAP_TYPE_ANY)
        self.real_im = cv2.imread(self.imi_path)
        width = wximg.GetWidth()
        self.wximg = self.scale_bitmap(wximg, 500/width)
        self.m_bitmap5.SetBitmap(self.wximg)
        self.m_mgr.Update()
        self.log(str(self.imi_path))
    def scale_bitmap(self, bitmap, scale):
        image = bitmap.ConvertToImage()
        width = image.GetWidth() * scale
        height = image.GetHeight() * scale
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image, wx.BITMAP_TYPE_ANY)
        return result
    def Next(self, event):
        self.Clear(event)
        self.imi += 1
        try : self.show_imi(self.imi)
        except : 
            self.imi -= 1
            wx.MessageBox('This is the last image of this folder', 'Cannot go next !',wx.OK )
    
    def Previous(self, event):
        self.Clear(event)
        self.imi -= 1
        try: self.show_imi(self.imi)
        except: 
            self.imi += 1
            wx.MessageBox('This is the first image of this folder', 'Cannot go previous !',wx.OK )
    def init_tracker(self, event):
        self.log('pick the keypoint to init tracker...')
        self.mytracks = [str(i) for i in range(11)]
        self.init_tracker_ = True
        # turn on get mouse
        self.m_bitmap5.Bind(wx.EVT_MOUSE_EVENTS, self.getmousepos)
        self.point_name = [str(i).zfill(2) for i in range(10)]
        self.point_temp = []
    def draw(self):
        thres = 500/720
        rois, cens = [], []
        for i in range(len(self.point_temp)):
            ra, rb, rc, rd = self.mytracks[i].roi
            ca, cb = self.mytracks[i].center
            rois.append([ra*thres, rb*thres, rc*thres, rd*thres])
            cens.append([ca*thres, cb*thres])
        
        # draw rect
        if self.roi_show_ :
            self.dc.SetPen(wx.Pen("red"))
            self.dc.SetBrush(wx.Brush("grey",style=wx.TRANSPARENT))
            for roi in rois:
                left, top, width, height = roi 
                pos = int(left), int(top)
                size = int(width), int(height)
                rect = wx.Rect(wx.Point(pos), wx.Size(size))
                self.dc.DrawRectangle(rect)

        # draw links
        if self.link_show_:
            lines, pens = [], []
            for i,(start, end) in enumerate(self.links):
                try:
                    x1, y1 = cens[start]
                    x2, y2 = cens[end]
                    lines.append([x1, y1, x2, y2])
                    pens.append(wx.Pen(self.color_hand[int((i+1)%5)], 2))
                except :pass
            self.dc.DrawLineList(lines, pens)

        # draw centers
        if self.keypoint_show_ :
            for i,cen in enumerate(cens):
                self.dc.SetPen(wx.Pen("black"))
                self.dc.SetBrush(wx.Brush(wx.Colour(0,255,0), wx.SOLID))
                size = self.keypoint_size
                
                if self.covered_point[i]:
                    self.dc.SetPen(wx.Pen("red"))
                    self.dc.SetBrush(wx.Brush(wx.Colour(255,0,0), wx.SOLID))
                    size = self.keypoint_size-1 if self.keypoint_size > 1 else 1
                self.dc.DrawCircle(cen,size)

    def draw_bitmap(self):
        self.dc = wx.MemoryDC(self.wximg)
        self.draw()
        self.dc.SelectObject(wx.NullBitmap)
        self.m_bitmap5.SetBitmap(self.wximg)
        self.m_mgr.Update()
    def manage_point(self, event):
    
        if len(self.point_temp) < 11 and len(self.point_temp) != -1 :
            self.point_temp.append(self.click)
            self.log('point(%d,%d) was added to be point[%d]'%(self.click[0],self.click[1],len(self.point_temp)-1))
            i = len(self.point_temp) - 1 # the last index
            self.mytracks[i] = MyTracker(self.real_im, self.click, self.tracking_roi_size)
            self.draw_bitmap()
        elif len(self.point_temp) == 11:
            # manage point mode

            # check nearest point
            dist = np.array(self.point_temp)-np.array(self.click)
            nearest_index = np.argmin(dist[:,0]**2 + dist[:,1]**2)

            # check in_area
            dist = self.point_temp[nearest_index] - np.array(self.click)
            dist = dist[0]**2 + dist[1]**2

            # if in_area
            if dist < 600:
                #move point
                self.move_point = True
                self.nearest_index = nearest_index

    def draw_move(self,event):
        #reset img
        self.imi_path = os.path.join(self.img_folder
                    , str(self.imi).zfill(10)+'.bmp')
        wximg = wx.Bitmap(self.imi_path, wx.BITMAP_TYPE_ANY)
        width = wximg.GetWidth()
        self.wximg = self.scale_bitmap(wximg, 500/width)

        
        self.dc = wx.MemoryDC(self.wximg)

        # re init nearest_point
        rm = self.point_temp[self.nearest_index]
        self.point_temp.insert(self.nearest_index,self.click)
        self.point_temp.remove(rm)
        self.mytracks[self.nearest_index] = MyTracker(self.real_im, self.click, self.tracking_roi_size)
        self.draw()
        self.dc.SelectObject(wx.NullBitmap)
        self.m_bitmap5.SetBitmap(self.wximg)

        self.m_mgr.Update()
    def set_covered_point(self):
        # check nearest point
        dist = np.array(self.point_temp)-np.array(self.click)
        nearest_index = np.argmin(dist[:,0]**2 + dist[:,1]**2)

        # check in_area
        dist = self.point_temp[nearest_index] - np.array(self.click)
        dist = dist[0]**2 + dist[1]**2

        # if in_area
        if dist < 100:
            # set to covered_point
            self.covered_point[nearest_index] = not self.covered_point[nearest_index]
            self.log('set coverd point of index_%d to %s'%(nearest_index,self.covered_point[nearest_index]))
                
    def Clear(self,event):
        self.show_imi(self.imi)
        self.point_temp = []
    def Redraw(self,event):
        #reset img
        self.imi_path = os.path.join(self.img_folder
                    , str(self.imi).zfill(10)+'.bmp')
        wximg = wx.Bitmap(self.imi_path, wx.BITMAP_TYPE_ANY)
        width = wximg.GetWidth()
        self.wximg = self.scale_bitmap(wximg, 500/width)
        #redraw
        self.draw_bitmap()
                
    def Back(self, event):
        #reset img
        self.imi_path = os.path.join(self.img_folder
                    , str(self.imi).zfill(10)+'.bmp')
        wximg = wx.Bitmap(self.imi_path, wx.BITMAP_TYPE_ANY)
        width = wximg.GetWidth()
        self.wximg = self.scale_bitmap(wximg, 500/width)

        #remove point
        self.point_temp.remove(self.point_temp[-1])
        self.draw_bitmap()
      
    def getmousepos(self, event):
        thres = 720/500
        x, y = event.GetPosition()
        self.click = int(x*thres), int(y*thres)
        self.left_down = event.LeftDown()
        self.left_up = event.LeftUp()
        self.right_up = event.RightUp()
  
        if self.left_down:
            self.manage_point(event)
        if self.left_up:
            self.move_point = False
        if self.right_up:
            self.set_covered_point()
            self.Redraw(event)
        if self.move_point:
            self.draw_move(event)
            self.log('point[%d] is relocating to (%d, %d)'%(self.nearest_index,self.click[0],self.click[1]))
        
    def open_a_data( self, event ):
        stage = Stage()
        lastline = stage.lastest()

    def open_a_folder( self, event ):
        event.Skip()

    def goto_img(self,event):
        a = self.m_textCtrl3.GetValue()
        
        if a == 'go... .bmp':
            wx.MessageBox('please input a number of .bmp file.','Warning',wx.OK )
        else:
            try: 
                a = int(a)
                try:
                    self.show_imi(a)
                except :
                    wx.MessageBox('Cannot go to the file you want.\ncheck in the folder.','Cannot open .bmp',wx.OK )
            
            except:
                wx.MessageBox('This is not a number\nplease input a number of .bmp file.','Cannot go to ...',wx.OK )
            
    def key_on_go_bmp(self,event):
        key = event.GetKeyCode()
        if key==13: # enter
            self.goto_img(event)
    def click_on_go_bmp(self,event):
        self.m_textCtrl3.SetValue('')
        event.Skip()
    def roi_show(self,event):
        self.roi_show_ = True 
        self.Redraw(event)
        self.m_menuItem17.Check(True)
        self.m_menuItem18.Check(False)
    def roi_hide(self,event):
        self.roi_show_ = False 
        self.Redraw(event)
        self.m_menuItem17.Check(False)
        self.m_menuItem18.Check(True)
    def keypoint_show(self,event):
        self.keypoint_show_ = True
        self.Redraw(event)
        self.m_menuItem171.Check(True)
        self.m_menuItem181.Check(False)
    def keypoint_hide(self,event):
        self.keypoint_show_ = False
        self.Redraw(event)
        self.m_menuItem171.Check(False)
        self.m_menuItem181.Check(True)
    def link_show(self,event):
        self.link_show_ = True
        self.Redraw(event)
        self.m_menuItem172.Check(True)
        self.m_menuItem182.Check(False)
    def link_hide(self,event):
        self.link_show_ = False
        self.Redraw(event)
        self.m_menuItem172.Check(False)
        self.m_menuItem182.Check(True)
    def Save(self,event):
        # if len(self.point_temp) == 11:
        # output = [img_name, [11_points], [confirm]]
        img_name = str(self.imi).zfill(10)
        # print(self.point_temp)
        # print(self.covered_point)
        dictionary_data = {"keypoint": self.point_temp
                , 'covered_point': self.covered_point}
        dir_temp = os.path.join(self.img_folder ,img_name + ".pkl")
        with open(dir_temp, "wb") as f:
            pickle.dump(dictionary_data, f)
        self.real_im = []
        self.Next(event)

        # update all trackers
        for i in range(11):
            self.mytracks[i].update(self.real_im)
            p = self.mytracks[i].center
            self.point_temp.append(p)
        self.Redraw(event)
      

        # else:
        #     print('not equaa 11')
        
    
    def testmode(self, event):
        self.img_folder = 'video_temp/70'
        self.imi = 3
        self.stop_cam = True # stop showing camera
        self.roi_show_ = True
        self.show_imi(self.imi)
        
        self.init_tracker(event)
        self.point_temp = [(241, 531), (184, 348), (148, 239), (228, 318), (240, 175), (277, 315), (315, 159), (325, 329), (365, 192), (360, 442), (429, 339)]
        for i,point in enumerate(self.point_temp):
            self.mytracks[i] = MyTracker(self.real_im, point, self.tracking_roi_size)
        self.Redraw(event)
    

    