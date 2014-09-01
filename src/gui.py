#!/usr/bin/python2

#gui for dbr
#Heavily based on code from storm dragon's daisy storm project, http://www.stormdragon.tk
#This file is part of dbr.
#This program is free software you may distribute and/or modify it under the terms of the Gnu General Public License, either version 3, or, at your option, any later version

import wx

class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs) 

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_OPEN, '&Open a book')
        fileMenu.AppendSeparator()

        exitProgram = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(exitProgram)

        self.Bind(wx.EVT_MENU, self.OnQuit, exitProgram)

        editMenu = wx.Menu()
        editMenu.Append(wx.ID_PREFERENCES, '&Preferences')
        BookmarksMenu=wx.Menu()
        BookmarksMenu.Append(100,'&add a bookmark')
        BookmarksMenu.AppendSeparator()
        BookmarksMenu.Append(101, '&list bookmarks for this book')
        playbackMenu=wx.Menu()
        playbackMenu.Append(100,'&play')
        playbackMenu.AppendSeparator()
        playbackMenu.Append(101, '&stop playback')
        playbackMenu.AppendSeparator()
        playbackMenu.Append(102, '&rewind')
        playbackMenu.AppendSeparator()
        playbackMenu.Append(103, '&fast forward')
        helpMenu=wx.Menu()
        helpMenu.Append(100, '&view user manual')
        helpMenu.AppendSeparator()
        helpMenu.Append(101, '&ask for help on irc')
        menubar.Append(fileMenu, '&File')
        menubar.Append(editMenu, '&Edit')
        menubar.Append(BookmarksMenu, '&bookmarks')
        menubar.Append(playbackMenu, '&playback')
        menubar.Append(helpMenu, '&help')
        self.SetMenuBar(menubar)
        ListBox=wx.ListBox(self)
        self.SetTitle('books list')
        txtBox = wx.TextCtrl(self)
        txtBox.SetEditable(False)
        self.SetSize((350, 250))
        self.SetTitle('Daisy Book Reader')
        self.Centre()
        self.Show(True)
    def OnQuit(self, e):
        self.Close()

def main():
    ds = wx.App()
    MainWindow(None)
    ds.MainLoop()    
if __name__ == '__main__':
    main()
