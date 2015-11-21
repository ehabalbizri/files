# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Egypt Tube by Ehab Albizri
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

addonID = 'plugin.video.egypttube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCWuj6cpZL_T1U508Y082u3g"
YOUTUBE_CHANNEL_ID_2 = "UC-Xq1_0e6ZTx7bxQTyGY0Hg"
YOUTUBE_CHANNEL_ID_3 = "UCKNzUrCVUCVXCUc3GT3diqQ"
YOUTUBE_CHANNEL_ID_4 = "UChu383qonIV-qHhYQpeeNGw"
YOUTUBE_CHANNEL_ID_5 = "UCfM85hxqqKrgGHgFDwcwOpg"
YOUTUBE_CHANNEL_ID_6 = "UCtpL6HyBK-z16GbJguHf3JQ"
YOUTUBE_CHANNEL_ID_7 = "UCHlQaF84dw_McA5NIB0Qm7A"
YOUTUBE_CHANNEL_ID_8 = "UCx97T9ko1xT0iLtUqEbCZXw"
YOUTUBE_CHANNEL_ID_9 = "UCVljfgnv629CtChzdI7JUFw"
YOUTUBE_CHANNEL_ID_10 = "UCB6sc84dcg6VQGB_d89sx2g"
YOUTUBE_CHANNEL_ID_11 = "UCFGwPWQEXEcYWAtJ_KSbf6g"
YOUTUBE_CHANNEL_ID_12 = "UC2yUJDR8MbigZ6JGxNi_rJA"
YOUTUBE_CHANNEL_ID_13 = "UC3Dci3BzZXDo4jw4dU8KqWg"
YOUTUBE_CHANNEL_ID_14 = "UCCdCsHQRURiTXwDwwW6fx0w"
YOUTUBE_CHANNEL_ID_15 = "UCVTcEg96476pQibXX7IMdJw"
YOUTUBE_CHANNEL_ID_16 = "UCYoo3rvwB24q9_kRCgR897Q"
YOUTUBE_CHANNEL_ID_17 = "UCDcELbJyLRuWx9rSFMKOo5Q"
YOUTUBE_CHANNEL_ID_18 = "UCIt3SC3X_6DPGsBa-9_KffA"


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
        title="AlHayah TV Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alhayatenter.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlHayah Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alhayatenter.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlHayah TV Group",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alhayatenter.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlHayah Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alhayattv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlHayah Series TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alhayatseries.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlNahar TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alnahartv.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="AlNahar TV Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alnaharnetwork.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlNahar AlYoum",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alnaharalyoum.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="AlNahar Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/alnahardrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBC Egypt",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/cbc.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBC two",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/tw.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBC eXtra",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/cbcextra.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBC Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/cbcdrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBC Sofra",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/cbcsofra.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dream TV Egypt",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/dreamtv.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Mehwar TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/mehwar.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mehwar Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/mehwardr.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TEN TV Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/egypt/ten.png",
        folder=True )
        
run()
