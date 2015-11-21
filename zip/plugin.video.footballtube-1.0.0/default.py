# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Football Tube by Ehab Albizri
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

addonID = 'plugin.video.footballtube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCFIdU1RkuRd26YDA7lerfEQ"
YOUTUBE_CHANNEL_ID_2 = "UCEPKlFeUjRY_1mpZP8GnkVg"
YOUTUBE_CHANNEL_ID_3 = "UCooTLkxcpnTNx6vfOovfBFA"
YOUTUBE_CHANNEL_ID_4 = "UCbWUEnTRHb3bRdrnovq8iuA"
YOUTUBE_CHANNEL_ID_5 = "UCYG6DQUw79szmnuNux_S8pg"
YOUTUBE_CHANNEL_ID_6 = "UCoNoB5_bbbmvVrlOoePltSA"
YOUTUBE_CHANNEL_ID_7 = "UCcGc0XcPGfU3ayD7LZhrk5g"
YOUTUBE_CHANNEL_ID_8 = "UC-KQIG4-dyR1kIHCQFOJ-hQ"
YOUTUBE_CHANNEL_ID_9 = "UCleo0cLOSiib0W62-GK1KdQ"
YOUTUBE_CHANNEL_ID_10 = "UC740ilqsaYlnp0CFdYQoowA"
YOUTUBE_CHANNEL_ID_11 = "UClvgyQvIplPQU8N73vPlFUA"
YOUTUBE_CHANNEL_ID_12 = "UCv-Or279OlKoOTvbUPkcWTg"
YOUTUBE_CHANNEL_ID_13 = "UCEOfOaZ49f0WaTAom8f97Jw"
YOUTUBE_CHANNEL_ID_14 = "UCLXLBPbpCncvBL52JJbgT0Q"
YOUTUBE_CHANNEL_ID_15 = "UCC9h3H-sGrvqd2otknZntsQ"
YOUTUBE_CHANNEL_ID_16 = "UCtSDTfD7RZhbsyxKZL9Wifw"


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
        title="Copa 90",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/copa90.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="KICK TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/kicktv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FOX Soccer",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/foxsoccer.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Football Daily",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/footballdaily.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FEEL MY STYLE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/fms.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Peradze",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/pep.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="ram7ooo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/ram7ooo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HeilRJ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/heilrj.jpeg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Javier Nathaniel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/jnfootball.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Teo CRi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/teocri.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ash Studio 7",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/ash.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scout Nation HD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/scout.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MNX HD 2",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/x.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sport Videos MM",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/svmm.jpeg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="free kickerz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/fk.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RM4Arab TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/football/realmadrid.png",
        folder=True )
        
run()
