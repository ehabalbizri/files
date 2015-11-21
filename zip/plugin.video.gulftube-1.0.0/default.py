# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Gulf Tube by Ehab Albizri
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

addonID = 'plugin.video.gulftube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC0oB4PeCZ6QH-V80H9E49dA"
YOUTUBE_CHANNEL_ID_2 = "UC2mWeEHv9IY6i74okFMkGPw"
YOUTUBE_CHANNEL_ID_3 = "UCjocA1MAKoxMvQi2k0cPYTA"
YOUTUBE_CHANNEL_ID_4 = "UC2EJXBsWR_5BTCy6R4kIO3A"
YOUTUBE_CHANNEL_ID_5 = "UCsVQJ4sjopcYEQHxWnS2Spg"
YOUTUBE_CHANNEL_ID_6 = "UCqFCFEIqqh35HXvkl58CERw"
YOUTUBE_CHANNEL_ID_7 = "UC8dLSrg_yTi1ScdH0wsyPpQ"


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
        title="Funoon TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/funoontv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="السعودية الأولى",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/ksa1.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="السعودية الثانية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/ksa2.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Qatar TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/qatartv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="روتانا خليجية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/rotanakhalijia.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlAan TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/alaan.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="AlAan Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/gulf/alaanenter.png",
        folder=True )
        
run()
