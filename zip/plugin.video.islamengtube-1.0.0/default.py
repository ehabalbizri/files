# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Islam-Eng Tube by Ehab Albizri
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

addonID = 'plugin.video.islamengtube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCWYCGN5KEsXpdE_hnSAH1Jw"
YOUTUBE_CHANNEL_ID_2 = "UCn2qB6okVotIM0kW7tu3m4g"
YOUTUBE_CHANNEL_ID_3 = "UCxBR44IXdJY0gsfHcIDMQuQ"
YOUTUBE_CHANNEL_ID_4 = "UC4KC9OS3dZZcoNhY__KFSog"
YOUTUBE_CHANNEL_ID_5 = "UCpGityBvHU20RxfhO7nl-qw"
YOUTUBE_CHANNEL_ID_6 = "UCqpYSlCBv2MNTVMyxwxu9iQ"
YOUTUBE_CHANNEL_ID_7 = "UCPqbO2X4vtuq8oDy6AAyCvQ"
YOUTUBE_CHANNEL_ID_8 = "UCTNXrKBJsadNAeaGH43dOfg"


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
        title="Bridges Foundation",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/bridges.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tariq Ramadan",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/tariq.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Talk Islam",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/talkislam.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Suhaib Webb",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/webb.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Yusuf Estes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/estes.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AbdurRaheem Green",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/green.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Channel Deedat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/deedat.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Islam",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/islamiceng/islam.png",
        folder=True )
		
run()
