# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Abu Dhabi Tube by Ehab Albizri
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

addonID = 'plugin.video.abudhabitube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC_p5qypAZQAUkgtjoJk5_Bg"
YOUTUBE_CHANNEL_ID_2 = "UCZ33NIO6rgl291T88-9jreQ"
YOUTUBE_CHANNEL_ID_3 = "UCI8LNtTNWaggPYKKZ2aatTg"
YOUTUBE_CHANNEL_ID_4 = "UC9XP3cPW39kXPKFvwxUtDAQ"
YOUTUBE_CHANNEL_ID_5 = "UCNCt4FU30rGh-1dYwkw2pGQ"
YOUTUBE_CHANNEL_ID_6 = "UCj0Ee0pnl7ZV3sRf87rnBYg"
YOUTUBE_CHANNEL_ID_7 = "UCNFJZCrrl1tVvWpKtNyZ90Q"
YOUTUBE_CHANNEL_ID_8 = "UCGLgxQPgvzpVZPUQS5MxY1w"
YOUTUBE_CHANNEL_ID_9 = "UCFBJ6wV3-XohkF_FPiertVQ"
YOUTUBE_CHANNEL_ID_10 = "UCbK0W6npCY5Zlv2nJoTagVw"
YOUTUBE_CHANNEL_ID_11 = "UChNXs3nnxHlqUYJBwjRV6-g"


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
        title="Emarat TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/alemarat.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi Comedy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi Social",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi Islamic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="National Geographic Abu Dhabi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/nationalgeographicabudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AD Sports TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabisport.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Arab Casting",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/arabcasting.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Rating Ramadan",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/ratingramadan.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="AlShara",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/alshara.png",
        folder=True )
		
run()
