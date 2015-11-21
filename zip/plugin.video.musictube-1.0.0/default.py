# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Music Tube by Ehab Albizri
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Ehab Albizri
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.musictube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCBq5hp6DvwWam2XOXw6lYJA"
YOUTUBE_CHANNEL_ID_2 = "UCYmjRHj3JhpWvrBjClZLnDw"
YOUTUBE_CHANNEL_ID_3 = "UCAmuBPgmOEeQ2B9MEW5k92w"
YOUTUBE_CHANNEL_ID_4 = "UCvLCV22s6F1047xVMilHuCw"
YOUTUBE_CHANNEL_ID_5 = "UCNhqvQMXIgRfjAGmxQqdNRw"
YOUTUBE_CHANNEL_ID_6 = "UC_BtcxLDvTCoNlm0zqc_vzw"
YOUTUBE_CHANNEL_ID_7 = "UCxIoihijwX4BvHjPGjKrovg"


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Awakening Records",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/awakening.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Axeer Studio",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/axeerstudio.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Coke Studio",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/cokestudio.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="iMedia Music Records",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/imedia.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rotana",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/rotana.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Melody",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/melody.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Mazzika",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/music/mazzika.png",
        folder=True )
		
run()
