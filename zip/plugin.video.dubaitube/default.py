# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Dubai Tube by Ehab Albizri
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

addonID = 'plugin.video.dubaitube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCuyiRRgNobUdBqKBJ-ItyTw"
YOUTUBE_CHANNEL_ID_2 = "UCnxcG6CqTO85dBXlyjPKInA"
YOUTUBE_CHANNEL_ID_3 = "UCpTncbkcIjS0v51sJz2jhsg"
YOUTUBE_CHANNEL_ID_4 = "UCFk_TvqG1qQ72fl4mDI23Lw"
YOUTUBE_CHANNEL_ID_5 = "UCOhiubMBr7ELL20N7y6vfjQ"
YOUTUBE_CHANNEL_ID_6 = "UCy3mHETEqjU9wtwiLHfg16A"
YOUTUBE_CHANNEL_ID_7 = "UCEmayGKQnuysygWru7lCAmQ"
YOUTUBE_CHANNEL_ID_8 = "UCru1hvc78Zv6inOREROqWGg"
YOUTUBE_CHANNEL_ID_9 = "UCmJr9VRnC8Q1TCIrf2G8bcg"
YOUTUBE_CHANNEL_ID_10 = "UCFNbWX5JH4byrgUhjlaiYWw"
YOUTUBE_CHANNEL_ID_11 = "UCPKxTu9dnQS_7RWgIPxv_6w"
YOUTUBE_CHANNEL_ID_12 = "UCK_o6DhHeXy1Q1ik6leYHPg"
YOUTUBE_CHANNEL_ID_13 = "UCBzBlMg9Z0drk5tG8uo3dVg"
YOUTUBE_CHANNEL_ID_14 = "UCBYZ1ufNQtPVBx6fBEiDN7g"


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
        title="Dubai Channels Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dcn.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dubai TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaitv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sama Dubai",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/samadubai.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Noor Dubai",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/noordubai.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dubai Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaidrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dubai Zaman",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaizaman.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Dubai ’one",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaione.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dubai Racing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubairacing.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Dubai Sports",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaisport.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DCN Cooking",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dcncooking.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DCN Digital",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dcndigital.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Golden Mic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/goldenmic.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Victorious",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/thevictorious.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="@Diala",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/aldiyala.png",
        folder=True )
        
run()
