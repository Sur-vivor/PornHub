""" Sing a song... 
    Command .sing(finished)
            .singhi(pending)
            .singpu(pending)
    By @PhycoNinja13b """




from telethon import events

import asyncio

import os

import sys

import random

from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"sing", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Singing...")

    await asyncio.sleep(2)

    x=(random.randrange(1,33))

    if x==1:

        await event.edit("馃幎 ഇടഞ്ഞെന്തേ നിന്നു പൊന്നേ ഇടഞ്ഞെന്നെ കൊല്ലും കണ്ണേ....എല്ലാരും ചൊല്ലുന്നേ പൊല്ലാപ്പ് ആണെന്ന്.. 馃幎")

    if x==2:

        await event.edit("馃幎താമരപ്പൂവിൽ വാഴും ദേവിയല്ലോ നീ... പൂനിലാക്കടവിൽ പൂക്കും പുണ്യമല്ലോ നീ... 馃幎")

    if x==3:

        await event.edit("馃幎പറയുവാൻ ഇതാദ്യമായി വരികൾ മായയെ മിഴികളിൽ ഒരാരായിരം മഴവിൽ പോലെ...馃幎")

    if x==4:

        await event.edit("馃幎പൊടിമീശ മുളയ്ക്കണ കാലം ഇടനെഞ്ചിലു് ബാന്റടി മേളം....പെരുനാളിനു് പള്ളിയിലെത്തിയതെന്തുകൊതിച്ചാണു്..馃幎")

    if x==5:

        await event.edit("馃幎പൂമുത്തോളേ നീയെരിഞ്ഞ വഴിയിൽ ഞാൻ മഴയായി പെയ്തെടീ…馃幎")

    if x==6:

        await event.edit("馃幎അരികത്തായാരോ പാടുന്നുണ്ടോ അത് എന്റെ മനസ്സാണോ… ആരാരോ എന്തോ പറയുന്നുണ്ടോ അനുരാഗവചസ്സോ പാഴ് സ്വരമോ....9�2")

    if x==7:

        await event.edit("馃幎തെളിമാനം മഴവില്ലിന്‍ നിറമണിയും നേരം....നിറമാര്‍ന്നൊരു കനവെന്നില്‍ തെളിയുന്ന പോലെ.....馃幎")    

    if x==8:

        await event.edit("馃幎ആരാധികേ…മഞ്ഞുതിരും വഴിയരികേനാളേറെയായി…കാത്തുനിന്നു മിഴി നിറയേ...馃幎")

    if x==9:

        await event.edit("馃幎പവിഴ മഴയേ… നീ പെയ്യുമോ..ഇന്നിവളേ… നീ മൂടുമോ...വെൻ പനിമതിയിവളിലെ മലരൊളിയഴകിലെ നാളങ്ങളിൽ എൻ കനവുകൾ വിതറിയ താരകങ്ങളെ കാണുവാൻ കാത്തു ഞാൻ....馃幎")

    if x==10:

        await event.edit("馃幎അഴലിന്റെ ആഴങ്ങളിൽ അവൾ മാഞ്ഞുപോയ്... നോവിന്റെ തീരങ്ങളിൽ ഞാൻ മാത്രമായ....馃幎")
     
    if x==11:

        await event.edit("馃幎എത്രയോ ജന്മമായ് നിന്നെഞാൻ തേടുന്നു... അത്രമേൽ ഇഷ്ടമായ് നിന്നെയെൻ പുണ്യമേ..馃幎")

    if x==12:

        await event.edit("馃幎ശ്യാമാംബരം പുൽകുന്നൊരാ വെൺചന്ദ്രനായ് നിൻ പൂമുഖം...馃幎")
    
    if x==13:

        await event.edit("馃幎ഉയിരിൽ തൊടും തളിർ വിരലാവണേ നീ. അരികേ നടക്കണേ. അലയും ചുടുകാറ്റിനു കൂട്ടിണയായ്നാ മൊരു നാൾ കിനാക്കുടിലിൽ ചെന്നണയുമിരുനിലാവലയായ്...馃幎")

    if x==14:

        await event.edit("馃幎കരിമിഴി കുരുവിയെ കണ്ടീല്ല ,നീ,ചിലമ്പൊലി ചാറ്റോളി  കണ്ടീല്ല, നീ,പണ്ടേ എന്നോടൊന്നും മിണ്ടീല ...馃幎")
        
    if x==15:

        await event.edit("馃幎എന്റ്റെനെഞ്ചാകെ നീയല്ലേ ,എന്റ്റെ ഉന്മാദം നീയല്ലേ  ,നിന്നെയറിയാൻ ഉള്ളുനിറയാൻ, ഒഴുകിയൊഴുകി ഞാൻ എന്നുമെന്നുമൊരു  പുഴയായ്  ..馃幎")

    if x==16:

        await event.edit("馃幎മഞ്ഞു മഴ കാറ്റിൽ ,കുഞ്ഞു മുളംകൂട്ടിൽ രണ്ടിളം പൈങ്കിളികൾ ഓഹോഹോ ...鈥檛")
     
    if x==17:

        await event.edit("馃幎ഞാൻ കനവിൽ കണ്ടൊരു കണ്മണിയാൽ ഇവളാണല്ലോ ,എന്നുള്ളു തുടിച്ചതുമിവളെ കാണാനാണല്ലോ ,ചെറു പൂക്കുല പൊലിവളാ ടുമ്പോൾ മോഹം  ഋതു മൗനം പോലും സംഗീതം .馃幎")

    if x==18:

        await event.edit("馃幎 ഈറൻ കാറ്റിൻ ഈണം പോലെ ,തോര  മഞ്ഞിൻ തൂവൽ പോലെ നോവും നെഞ്ചിൻ രാ കൂട്ടിൽ  വാവാ  മെല്ലെ മെല്ലെ .....馃幎")

    if x==19:

        await event.edit("馃幎 പേരില്ല ..രാജ്യത്തെ ..രാജകുമാരി , അതിരില്ല ..രാജ്യത്തെ രാജകുമാരാ, ആരോരും കാണാതെന്നരികിൽ വരാമോ അരികിൽ ഞാൻ വന്നാൽഇന്നെന്തു തരും നീ.馃幎")

    if x==20:

        await event.edit("馃幎നീ...കണ്ണോട് കണ്ണോട് കണ്ണോരമായി , കാതോട് കാതോട് ,കാതോരമായി ,നെഞ്ചോട് നെഞ്ചോട് ,നെഞ്ചോരമായി ,നിറയ് .....🎵")

    if x==21:
        
        await event.edit("馃幎ചെമ്പനീർ പൂവേ നീ ,അന്നേതോ ഒരുരാവിൽ,നീല മഞ്ഞിൽ വിരിഞ്ഞെൻ കൺമുമ്പിൽ മിഴി ചിമ്മി ,അത്ഭുതം അടങ്ങാത്തന്നു  ഞാൻ  അങ്ങനെ നിശബ്‌ദം നിൽകവേ ,യെങ്ങുപോയ് പ്രകാശം നൽകിനീ ,നില്കയായ്  നിന്നെയോർത്തിന്നു ഞാൻ .....馃幎")
        
    if x==22:
        
        await event.edit("馃幎നീ മറന്നോ പോയൊരുനാൾ ഈയിര പോലെ നാമിരുപേർ ഓത്തു പള്ളീൽ ഒത്തു ചേർന്നു ഏറിയ നാളു പോയതല്ലേ,അന്നു നീ ചിരിച്ചു പാതി വച്ചു കുഞ്ഞു കിനാവിൻ കണ്ണി മാങ്ങാ ,ഓർത്തിരുന്നു കാത്തിരുന്നു ജീവിതമാകെ നീറിടുമ്പോൾ നീ പച്ച തുരുത്തായ് ,സ്വപ്നതുരുമ്പായ് കതിരിടുന്നു,കിളിച്ചുണ്ടൻ മാമ്പഴമേ  കിളി കൊത്താ തേൻ പഴമെ തളിർ ചുണ്ടിൽ പൂത്തിരി മുത്തായ് ചിപ്പിയിൽ എന്നെ കാത്തു വച്ചോ  ....馃幎")
       
    if x==23:

        await event.edit("馃幎കിലുകിൽ പമ്പരം ,തിരിയുംമാനസം ,അറിയാതമ്പിളി,മയങ്ങു  വാവാവോ..馃幎")

    if x==24:

        await event.edit("馃幎കസവിന്റെ തട്ടമിട്ട് ,വെള്ളിയരഞ്ഞാണമിട്ട് ,പൊന്നിന്റെ കൊലുസ്സുമിട്ടൊരു മൊഞ്ചത്തി ,കൂന്താലി പുഴയൊരുവമ്പത്തി ,കൂന്താലി പുഴയൊരു വമ്പത്തി ..馃幎")

    if x==25:
        
        await event.edit("馃幎വെറുതെ വെറുതെ ,പരത്തും മിഴികൾ , വേഴാമ്പലായ് നിൻ നടകാത്തു, ചന്ദന കുറിനീയണിഞ്ഞതിലെന്റെ പേരു പതിഞ്ഞില്ലെ മന്ദഹാസ പാൽനിലാ പുഴ എന്റെ മാറിലലിഞ്ഞില്ലേ....馃幎")
        
    if x==26:
        
        await event.edit("馃幎നിലാ പക്ഷികൾ ഒരേയാത്രയിൽ തണൽ തേടിയോ ...മുളംകുട്ടിലെ ..ഇളം ,പായയിൽ ,ഇടം തേടിയോ ..ഇതിലെ ,വരും കിനാതെന്നലിൽ,താരിളം..മലർ മണം പൂത്തുവോ തൂവൽ തൊടാ തുലാ തൂ മഴചാറ്റുകൾ കുളിർ കണം തന്നുവോ ..ആദ്യമായ് .....നിറം ചൂടിയോ ...നിൻ യാമങ്ങളും....馃幎")
        
    if x==27:
        
        await event.edit("馃幎 വാൽക്കിങ് ഇൻ ദി  മൂൺ ലൈറ്റ്  ഐആം തിങ്കിങ് ഓഫ് യു ....ലിസനിംഗ്  ടു   ദി  റൈൻ  ഡ്രോപ്‌സ് .. ഐആം ..തിങ്കിങ് ..യു  ...ഇളമാൻ കണ്ണിലൂടെ ... ഐആം ...തിങ്കിങ്  ഓഫ്‌ .. യു ...ഇളനീർ കനവിലൂടെ..ഐആം തിങ്കിങ് ..ഓഫ് ..യു ....馃幎")
        
    if x==28:
        
        await event.edit("馃幎കണ്ണോണ്ടാകണേ നോക്കല്ലേ പെണ്ണെ ..നിന്നു ചിരിക്കല്ലേ ..നിന്നോടെനികെന്തോ ..തോന്നുനെടി .....馃幎")

    if x==29:
        
        await event.edit("馃幎 എന്തിനെന്നറിയില്ല എപ്പോഴെന്നറിയില്ല....എന്തിനോ നിന്നെനിക്കിഷ്ട്ടമായി....馃幎")
        
    if x==30:
        
        await event.edit("馃幎തട്ടത്തിൻ  മറയത്തെ  പെണ്ണെ നിന്ന്  കണ്ണിൽ എന്നെ ഞാൻ  കണ്ടേ തട്ടത്തിൻ മറയത്തെ പെണ്ണെ നിന്ന്  കണ്ണിൽ എന്നെ ഞാൻ  കണ്ടേ  അരികിലായി വന്നു  നിന്ന് മൃദുലമാം കൈ  തൊട്ടാൽ അരുമയായി നീ  പാടുമൊ  അലസമാം നിന്ന് കൂന്തൽ  ചുരുളുകൾ മോഹത്തിന് മന്ദ്രം ചുടുന്നുണ്ടോ മഴയിൽ മാറിൽ  ചേരും കണം  പോലെ  എന്നും  ഞാൻ .....馃幎")
    
    if x==31:
        
        await event.edit("馃幎 ഞാൻ  ജാക്ക്സൺ  അല്ലേടാ . ന്യൂട്ടൺ അല്ലേടാ  ജോക്കർ അല്ലേടാ .. മൂൺ  വാക്  മില്ലെടാ  സ്റ്റാറുമില്ലടാ ഒന്നുമല്ലെടാ 馃幎")
        
    if x==32:
        
        await event.edit("馃幎ലൈലാകമേ പൂചൂടുമോ വിടവാങ്ങുമീ രാത്രിതൻ വാതിലിൽ ആകാശമേ നീർ പെയ്യുമോ പ്രണയാർദ്രമീ ശാഖിയിൽ ഇന്നിതാ.... 馃幎")
        
    if x==33:
        
        await event.edit("Not in a mood to sing. Sorry!")
