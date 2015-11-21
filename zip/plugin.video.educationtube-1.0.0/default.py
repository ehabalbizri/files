# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Education Tube by Ehab Albizri
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

addonID = 'plugin.video.educationtube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCpv1WLMnYx7clFId7bEJAZg"
YOUTUBE_CHANNEL_ID_2 = "UC5ls68cohdcyGx10e1TV9XA"
YOUTUBE_CHANNEL_ID_3 = "UCMUGHz7B-LYLLhtb6WPuoZg"
YOUTUBE_CHANNEL_ID_4 = "UCa7lQu3RM6p88h4KOfTpqWA"
YOUTUBE_CHANNEL_ID_5 = "UCC_hFSIv9at-ieZ_yS-M9mA"
YOUTUBE_CHANNEL_ID_6 = "UCDfaUfDk7R_GYUFaiLPsitw"
YOUTUBE_CHANNEL_ID_7 = "UCZ8a0llFkEC-F7QyogdvpDQ"


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
        title="عالم عجيب",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/3ajeeb.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="متع عقلك",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/brainfun.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="A3riF | اعرف",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/a3rif.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="هل تعلم؟",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/doyouknow.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="M.A TUBE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/matube.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Medtana / ميدتانا",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/medtana.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="TOP10 ARAB",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/educational/top10.png",
        folder=True )
		
run()
