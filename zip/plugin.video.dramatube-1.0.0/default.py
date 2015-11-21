# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Drama Tube by Ehab Albizri
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

addonID = 'plugin.video.dramatube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCy2CIDKYZqqbeJ0NHNcJ9sQ"
YOUTUBE_CHANNEL_ID_2 = "UCOhiubMBr7ELL20N7y6vfjQ"
YOUTUBE_CHANNEL_ID_3 = "UCI8LNtTNWaggPYKKZ2aatTg"
YOUTUBE_CHANNEL_ID_4 = "UCv3hC03xMryr4tQR5o9SGSA"
YOUTUBE_CHANNEL_ID_5 = "UCXmisxq7GT04oaXmF2Lg7OA"
YOUTUBE_CHANNEL_ID_6 = "UCVljfgnv629CtChzdI7JUFw"
YOUTUBE_CHANNEL_ID_7 = "UCAHEsq5opZ9uKUNMWSrxwBA"


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
        title="MBC GROUP",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/drama/mbcgroup.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dubai Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/dubai/dubaidrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Abu Dhabi Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/abu%20dhabi/abudhabi.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Melody Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/drama/melodydrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Play Hekayat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/drama/playhekayat.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlNahar Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/drama/alnahardrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="مسلسلات خليجية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/drama/khalijiseries.png",
        folder=True )
        
run()
