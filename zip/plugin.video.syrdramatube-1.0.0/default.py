# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Syr-Drama Tube by Ehab Albizri
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

addonID = 'plugin.video.syrdramatube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCCL-or5GRs9EMs5LGz7RFaQ"
YOUTUBE_CHANNEL_ID_2 = "UC3LGwTaBCu9EE4wwxqtLVXQ"
YOUTUBE_CHANNEL_ID_3 = "UCET-WX1ZZDKrXY4_LSUp6RA"
YOUTUBE_CHANNEL_ID_4 = "UCyaYjMo5HeeTygGrKvLZssw"
YOUTUBE_CHANNEL_ID_5 = "UCeuEvvfHa4BFK21xB6RXJXA"
YOUTUBE_CHANNEL_ID_6 = "UCIjLm-9nDTlhlPK5cZ8VBwg"
YOUTUBE_CHANNEL_ID_7 = "UCdY_HKUGiA6dUdFzEpEnq0A"
YOUTUBE_CHANNEL_ID_8 = "UCEI1VCoGnfs4wVCHc-sG9ew"
YOUTUBE_CHANNEL_ID_9 = "UCxCS1Mosb9M1VWTflUckJFA"
YOUTUBE_CHANNEL_ID_10 = "UCwsDLukKpKVJyFQgpO-Vt7w"
YOUTUBE_CHANNEL_ID_11 = "UCM3ZDdbvu5Hjw4czms6V8cQ"
YOUTUBE_CHANNEL_ID_12 = "UCs9W74OxD5fGK4_DKGtkzxA"
YOUTUBE_CHANNEL_ID_13 = "UCJVACZtKkKlj9HcX11we41g"
YOUTUBE_CHANNEL_ID_14 = "UCU9uA0sZK1liuHbOo1kN1XA"
YOUTUBE_CHANNEL_ID_15 = "UCz7DhlIryFjP92mdsiiegxA"
YOUTUBE_CHANNEL_ID_16 = "UCf0OczBVeGQLAlI8xAYHuhQ"
YOUTUBE_CHANNEL_ID_17 = "UCKQqjN19Gpf9Dk76QTYtgeA"
YOUTUBE_CHANNEL_ID_18 = "UCB0FUX7CTM7_HKAdO8N9JCQ"


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
        title="شركة غزال للإنتاج والتوزيع الفني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/ghazalwatan.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Clacket Media Productions",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/clacket.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="قبنض للإنتاج والتوزيع الفني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/kaband.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Golden Line for TV Production and Distribution",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/goldenline.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="شركة عاج للانتاج الفني والتوزيع",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/aj.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="EBLA International for Cinema and TV Production",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/ebla.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="شيخاني للإنتاج المرئي",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/sheikhani.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="الشرق للإنتاج والتوزيع الفني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/orient.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="لين للإنتاج والتوزيع الفني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/leen.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Moon and Stars Production",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/moonstars.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SAPITV بقعة ضوء",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/sapitv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="شركة الشام الدولية للإنتاج السينمائي والتلفزيوني",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/shamdrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Syrian Drama",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/syraindrama.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Drama TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/dramatv.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="INSOMNIA TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/insomniatv.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ImediaSeries | أى ميديا مسلسلات",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/imedia.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="مسلسلات عربية كاملة",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/fullseries.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="iSinan Series",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://raw.githubusercontent.com/ehabalbizri/files/master/icons/syrian%20drama/fullseries.png",
        folder=True )
        
run()
