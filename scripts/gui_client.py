#!/usr/bin/env python

import sys
import wx
import wx.html
#import rospy
from beginner_tutorials.srv import *

projectName = "3D Copy"

# --- ROS FUNCTIONS ---


def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def usage():
    return "%s [x y]" % sys.argv[0]

# --- END OF ROS FUNCTIONS ---

# --- GUI FUNCTIONS ---


class Frame(wx.Frame):

    def __init__(self, title):

        wx.Frame.__init__(self, None, title=title, pos=(150, 150), size=(500, 400))
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Initialize the top menu bar
        menu_bar = wx.MenuBar()

        # Setup file menu
        file_menu = wx.Menu()
        file_menu_quit = file_menu.Append(wx.ID_EXIT, "\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.on_close, file_menu_quit)
        menu_bar.Append(file_menu, "&File")

        # Setup help menu
        help_menu = wx.Menu()
        help_menu_about = help_menu.Append(wx.ID_ABOUT, "&About", "Information about 3D Copy")
        self.Bind(wx.EVT_MENU, self.on_about, help_menu_about)
        menu_bar.Append(help_menu, "&Help")

        self.SetMenuBar(menu_bar)

        self.status_bar = self.CreateStatusBar()

        panel = wx.Panel(self)

        box = wx.BoxSizer(wx.VERTICAL)

        # Label for input 1
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label="First Number:")
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        # Input 1
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=0.5)
        box.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        box.Add((-1, 10))

        # Label for input 2
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label="Second number:")
        hbox2.Add(st2, flag=wx.RIGHT, border=8)

        # Input 2
        tc2 = wx.TextCtrl(panel)
        hbox2.Add(tc2, proportion=1)
        box.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        box.Add((-1, 10))

        # Buttons
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        scan_button = wx.Button(panel, label='Scan', size=(70, 30))
        scan_button.Bind(wx.EVT_BUTTON, self.Calc)
        hbox3.Add(scan_button)

        cancel_scan_button = wx.Button(panel, label='Cancel Scan', size=(100, 30))
        cancel_scan_button.Bind(wx.EVT_BUTTON, self.Calc)
        hbox3.Add(cancel_scan_button)

        reset_button = wx.Button(panel, label='Reset Hardware', size=(130, 30))
        reset_button.Bind(wx.EVT_BUTTON, self.Calc)
        hbox3.Add(reset_button)

        mesh_button = wx.Button(panel, label='Mesh', size=(70, 30))
        mesh_button.Bind(wx.EVT_BUTTON, self.Calc)
        hbox3.Add(mesh_button)
        box.Add(hbox3, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # Progress bar (NOT WORKING)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        progress_bar = wx.Gauge(panel, range=20, size=(250, 25), style=wx.GA_HORIZONTAL)
        hbox4.add(progress_bar, proportion=1, flag=wx.ALIGN_CENTRE)
        box.add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        panel.SetSizer(box)
        panel.Layout()

    def on_close(self, event):
        dlg = wx.MessageDialog(self,
                               "Do you really want to close this application?",
                               "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def on_about(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()

    def Calc(self, event):
        return
        #x = add_two_ints_client(1,2)

# --- END OF GUI FUNCTIONS ---

if __name__ == "__main__":

    app = wx.App(redirect=True)  # Error messages go to popup window
    top = Frame(projectName)
    top.Show()
    app.MainLoop()

    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
