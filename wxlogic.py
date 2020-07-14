import wx 
from wxui import MyFrame1 
import cv2
import threading
import time
import numpy as np
import os
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
    def __init__(self, wximg, point):
        offset = 30
        # roi = (left, top, right, bottom)
        cx, cy = point[0], point[1]
        self.roi = cx-offset, cy-offset, cx+offset, cy+offset
        self.tracker = cv2.TrackerCSRT_create()
        cvimg = self.convert(wximg)
        self.tracker.init(cvimg, self.roi)
    def convert(self, wximg):
        wximg.SaveFile('wxbit_temp.bmp', wx.BITMAP_TYPE_BMP)
        cvimg = cv2.imread('wxbit_temp.bmp')
        return cvimg
    def update(self, new_wximg):
        cvimg = self.convert(new_wximg)
        success, self.roi = self.tracker.update(cvimg)

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
        self.imi += 1
        try : self.show_imi(self.imi)
        except : 
            self.imi -= 1
            wx.MessageBox('This is the last image of this folder', 'Cannot go next !',wx.OK )
    def Previous(self, event):
        self.imi -= 1
        try: self.show_imi(self.imi)
        except: 
            self.imi += 1
            wx.MessageBox('This is the first image of this folder', 'Cannot go previous !',wx.OK )
    def init_tracker(self, event):
        self.log('pick the keypoint to init tracker...')
        self.init_tracker_ = True
        # turn on get mouse
        self.m_bitmap5.Bind(wx.EVT_LEFT_UP, self.getmousepos)
        self.point_name = [str(i).zfill(2) for i in range(10)]
        self.point_temp = []
    def draw_bitmap(self, roi):
        self.log('drawing...')
        self.dc = wx.MemoryDC(self.wximg)
       
        self.dc.SetPen(wx.Pen("red"))
        self.dc.SetBrush(wx.Brush("grey",style=wx.TRANSPARENT))
        
        left, top, right, bottom = roi 
        pos = int(left), int(top)
        size = int(right-left), int(bottom-top)
        rect = wx.Rect(wx.Point(pos), wx.Size(size))
        self.dc.DrawRectangle(rect)

        self.dc.SetBrush(wx.Brush(wx.Colour(255,0,0), wx.SOLID))
        center = int((left+right)/2), int((bottom+top)/2)
        self.dc.DrawCircle(center,3)
        print('click=',self.click)
        print('center=',center)
        
        self.dc.SelectObject(wx.NullBitmap)
        self.m_bitmap5.SetBitmap(self.wximg)

        self.m_mgr.Update()
        self.log('drawed')
    def manage_point(self, event):
        on = False
        if not self.init_cam:
            on = True
        else:
            wx.MessageBox('please select a image folder.','Cannot track',wx.OK )
        if on == True:
            if len(self.point_temp) <= 10:
                self.point_temp.append(self.click)
                mytrack = MyTracker(self.wximg, self.click)
                self.draw_bitmap(mytrack.roi)
            
    def getmousepos(self, event):
        x, y = event.GetPosition()
        
        self.click = int(x), int(y)
        self.manage_point(event)
    def testmode(self, event):
        self.img_folder = 'video_temp/01'
        self.imi = 1
        self.stop_cam = True # stop showing camera
        self.show_imi(self.imi)
        self.init_tracker(event)
    def open_a_data( self, event ):
        stage = Stage()
        lastline = stage.lastest()
        print(lastline)

    def open_a_folder( self, event ):
        event.Skip()
