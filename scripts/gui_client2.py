#!/usr/bin/env python

import sys
import wx
#import rospy
#from beginner_tutorials.srv import *

width = 800
height = 300

class Window(wx.Frame):

    def __init__(self, parent, title):
        super(Window, self).__init__(parent, title=title, size=(width, height))
        self.init_ui()

    def init_ui(self):

        self.count = 0

        panel = wx.Panel(self)

        visualizer_box = wx.BoxSizer(wx.VERTICAL)
        menu_box = wx.BoxSizer(wx.VERTICAL)
        progress_box = wx.BoxSizer(wx.HORIZONTAL)



        #hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        #self.gauge = wx.Gauge(panel, range=100, size=(350, 25), style=wx.GA_HORIZONTAL)
        visualizer_button = wx.Button(panel, label="Viz")
        menu_button = wx.Button(panel, label="Menu")
        progress_button = wx.Button(panel, label="Prog")

        #self.Bind(wx.EVT_BUTTON, self.progress, visualizer_button)

        #hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        #hbox2.Add(visualizer_button, proportion=1, flag=wx.ALIGN_CENTRE, border=10)

        visualizer_box.Add(visualizer_button, proportion=1, flag=wx.ALIGN_CENTRE, border=10)
        menu_box.Add(menu_button, proportion=1, flag=wx.ALIGN_CENTRE, border=10)
        progress_box.Add(progress_button, proportion=1, flag=wx.ALIGN_CENTRE, border=10)

        #vbox1.Add((0, 30))
        #vbox1.Add(hbox1, flag=wx.ALIGN_CENTRE)
        #vbox1.Add((0, 20))
        #vbox1.Add(hbox2, flag=wx.ALIGN_CENTRE)
        #panel.SetSizer(vbox1)

        self.SetSize((width, height))
        self.Centre()
        self.Show(True)

    def progress(self, e):
        if self.count < 100:
            self.count += 1
        self.gauge.SetValue(self.count)
        print(self.count)

if __name__ == "__main__":
    app = wx.App()
    Window(None, "3D Copy")
    app.MainLoop()
