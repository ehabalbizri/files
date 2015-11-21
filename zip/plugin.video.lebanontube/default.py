# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Lebanon Tube by Ehab Albizri
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

addonID = 'plugin.video.lebanontube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCnkTo_wMqGtLiA4xX7roORg"
YOUTUBE_CHANNEL_ID_2 = "UCpE6gpKewomi17XDyPfpFjA"
YOUTUBE_CHANNEL_ID_3 = "UC5f_fxJa5G9AR9L3J5Z2I4A"
YOUTUBE_CHANNEL_ID_4 = "UCJu-0vnWt0wFMQuLsjzwjRQ"
YOUTUBE_CHANNEL_ID_5 = "UCBrIvQGxLdxfpeAKXy5wALA"
YOUTUBE_CHANNEL_ID_6 = "UCJJd_N_m0WBkqIX-BFTI7Iw"
YOUTUBE_CHANNEL_ID_7 = "UC22W9D8YHMYd8-Is7SoUFag"
YOUTUBE_CHANNEL_ID_8 = "UCU8vqcbu1R04Wt9_sz8Fh3g"


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
        title="MTV Lebanon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/mtvlebanon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LBCI Lebanon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/lbclebanon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aljadeed TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/aljadeed.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="OTV Lebanon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/otv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FutureTV Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/futuretv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FutureTV Society & Lifestyle",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/futuretv.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="FutureTV La Youmal",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/layomal.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fatafeat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/lebanon/fatafeat.png",
        folder=True )
		
run()
