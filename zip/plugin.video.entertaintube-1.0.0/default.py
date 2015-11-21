# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Entertain Tube by Ehab Albizri
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

addonID = 'plugin.video.entertaintube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCpsSadsgX_Qk9i6i_bJoUwQ"
YOUTUBE_CHANNEL_ID_2 = "UC1r4VtVE__5K6c_L_3Vlxxg"
YOUTUBE_CHANNEL_ID_3 = "UC1N_Yuz6eHkX39hb1qtrtkQ"
YOUTUBE_CHANNEL_ID_4 = "UCo86JCZ5cg-m6v7DQ48Qh_Q"
YOUTUBE_CHANNEL_ID_5 = "UCwgURKfUA7e0Z7_qE3TvBFQ"
YOUTUBE_CHANNEL_ID_6 = "UC05Q60rJEkO0zZpCU7jw3-A"
YOUTUBE_CHANNEL_ID_7 = "UCUvufBZoieEr1YOFhOMnzHw"
YOUTUBE_CHANNEL_ID_8 = "UCOKsFInOx-GzAEZvjloIj6g"


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
        title="Just For Laughs Gags",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/justforlaugh.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="fousey TUBE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/fousey.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shady Srour",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/shady.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Reaction",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/reaction.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Devin Super Tramp",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/devinsupertramp.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="أمريكا بالعربي",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/americabelarabi.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Albernameg",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/albernameg.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joe Tube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/entertainment/joetube.png",
        folder=True )
		
run()
