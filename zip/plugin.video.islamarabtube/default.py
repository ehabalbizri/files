# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Islam-Arab Tube by Ehab Albizri
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

addonID = 'plugin.video.islamarabtube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC_Ds7nedV3NqYf0zhpYti4A"
YOUTUBE_CHANNEL_ID_2 = "UCVh-JDC_VX0b15Hke0bvpGg"
YOUTUBE_CHANNEL_ID_3 = "UCFAR9NrKzW8OWzgRscdGXxA"
YOUTUBE_CHANNEL_ID_4 = "UCq4BX3C9XzeKy0WbOKgL5iA"
YOUTUBE_CHANNEL_ID_5 = "UCiC_h4iC9s7Ddr3CT82_EpA"
YOUTUBE_CHANNEL_ID_6 = "UChum7AwFulXsbI6-RmQDXzg"
YOUTUBE_CHANNEL_ID_7 = "UCTRGcT1KQVoQA1vdNLlbjhw"
YOUTUBE_CHANNEL_ID_8 = "UCYpOQtU7UgnMPBAIY-bdHdw"
YOUTUBE_CHANNEL_ID_9 = "UCjxcF4A7pCyWsuJcZOymF_g"
YOUTUBE_CHANNEL_ID_10 = "UCwttCEi9Fq1DgTd5Anil6rQ"
YOUTUBE_CHANNEL_ID_11 = "UCKUOmGXE9Ytlc2EzpGqimtw"
YOUTUBE_CHANNEL_ID_12 = "UCfpli4VHoS12syPkPxHl7XA"
YOUTUBE_CHANNEL_ID_13 = "UCxp3WZtu8R1o6fS_a9UIrZQ"
YOUTUBE_CHANNEL_ID_14 = "UCGPYTE-X0sid2e4VXZMEU6g"


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
        title="ARAM TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/aramtv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Axeer TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/axeertv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Islamophobia TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/islamophobia.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="مؤسسة جسور",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/josour.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="قناة اقرأ الفضائية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/iqra.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fattabiouni فاتبعوني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/fattabiouni.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Fahad Alkandari",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/fahd.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="EOTW & Beyond",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/eotw.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Amr Khaled",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/amrkhaled.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mustafa Hosny",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/mostafa.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="عمر عبد الكافي",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/omar.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="صالح المغامسي",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/saleh.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mohammad Nouh Qudah",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/mahnouh.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Deedat 4 Arabs",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamicarab/deedat4arab.png",
        folder=True )
        
run()
