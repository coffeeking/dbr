###This file is part of dbr
#### This program is free software you may modify and distribute it under the terms of the Gnu General Public License, either version 3 or, at your option, any later version
###This program is distributed in the hope that it will be useful, but without any warranty of any kind, including, but not limited to, merchantability or fitness for a particular purpose

#config.py
#describes and implements an xdg compliant config scheme for dbr, storing #your bookmarks, list of books, and preferences inside of a folder named #after dbr
#import the xdg module
import xdg, os

class config:
    def get_settings_directory(self):
        #check for the presence
        #of xdg-user-home, and if so, respect it. If not, default to ~/.config
        #try getting the xdg-user-home variable. If it isn't set, default #to ~/.config
        if os.environ.get('XDG_CONFIG_HOME') == "":
            settingsDir = os.path.join(xdg_home, 'dbr')
        else:
            #get the path of ~/.config and set the settingsDir to that location
            settingsDir = os.path.join(os.environ.get('HOME'), '.config/dbr')
        return settingsDir

folder = config()
print folder.get_settings_directory()
