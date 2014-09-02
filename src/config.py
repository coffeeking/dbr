###This file is part of dbr
#### This program is free software you may modify and distribute it under the terms of the Gnu General Public License, either version 3 or, at your option, any later version
###This program is distributed in the hope that it will be useful, but without any warranty of any kind, including, but not limited to, merchantability or fitness for a particular purpose

#config.py
#describes and implements an xdg compliant config scheme for dbr, storing #your bookmarks, list of books, and preferences inside of a folder named #after dbr
#import the xdg module
import xdg, os
print("we have xdg imported.")
class config:
        def __init__(self, folder):
        #check for the presence
#of xdg-user-home, and if so, respect it. If not, default to ~/.config
                settingsDir=""
        #try getting the xdg-user-home variable. If it isn't set, default #to ~/.config
        xdg-home=os.environ.get('XDG_CONFIG_HOME')
if xdg-home=="":
        print("we have xdg home.")
        #apparently the xdg-home variable isn't set, default to ~/.config
        settingsDir=os.path.join(_home, '.config'/dbr)
else:
        #get the path of xdg-home and set the settingsDir to that location
        print("oops, no xdg home.")
        settingsDir=os.environ.get('XDG_CONFIG_HOME'/dbr)
        return config

