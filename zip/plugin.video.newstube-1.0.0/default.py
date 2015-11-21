# -*- coding: utf-8 -*-
#------------------------------------------------------------
# News Tube by Ehab Albizri
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

addonID = 'plugin.video.newstube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCahpxixMCwoANAftn6IxkTg"
YOUTUBE_CHANNEL_ID_2 = "UCfiwzLy-8yKzIbsmZTzxDgw"
YOUTUBE_CHANNEL_ID_3 = "UCIJXOvggjKtCagMfxvcCzAA"
YOUTUBE_CHANNEL_ID_4 = "UCsP3Clx2qtH2mNZ6KolVoZQ"
YOUTUBE_CHANNEL_ID_5 = "UCZCFHCU-2eGF7V5ciMkoPHw"
YOUTUBE_CHANNEL_ID_6 = "UC30ditU5JI16o5NbFsHde_Q"
YOUTUBE_CHANNEL_ID_7 = "UCelk6aHijZq-GJBBB9YpReA"
YOUTUBE_CHANNEL_ID_8 = "UCzyAonkXMAIi8bp7_05PV-Q"
YOUTUBE_CHANNEL_ID_9 = "UC5GvVahlgulCyo4cshSmbcg"
YOUTUBE_CHANNEL_ID_10 = "UCFNbWX5JH4byrgUhjlaiYWw"
YOUTUBE_CHANNEL_ID_11 = "UC9_XmAwE5szLHF76FjMylaw"
YOUTUBE_CHANNEL_ID_12 = "UCiQf3iuooJRMi3Rm3jZZajw"
YOUTUBE_CHANNEL_ID_13 = "UCZslGytOwaEEZPkiE4X47FA"
YOUTUBE_CHANNEL_ID_14 = "UCqr_xxiCUdqkDS1e4IIb0KA"


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
        title="AlArabiya",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/alarabiya.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlJazeera",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/aljazeera.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="سكاي نيوز عربية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/skynewsarabia.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RT Arabic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/rtarabic.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlMayadeen",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/myad.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DW عربية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/dw.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="BBC Arabic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/bbc.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monte Carlo Doualiya",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/mcd.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="TRT العربية",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/trtarabic.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AlJadeed",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/aljadeed.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MTV Lebanon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/mtvnews.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Future TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/futuretv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Orient News",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/orient.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="euronews (عربي)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/news/euro.png",
        folder=True )
        
run()
