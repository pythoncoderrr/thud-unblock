# thud-unblock
Unblock black screen from TurboHUD

This project is a compilation of https://github.com/typcn/UnblockScreenshot and https://github.com/numaru/injector.

TurboHUD is an overlay for Diablo3. In Season 17 (S17), Zy made a plugin/helper for TurboHud to play zbarb, wizard, etc. 
KillerJohn (TurboHUD creator) did not like this. Zy Helper was opening a socket and having another program connect to that socket,
passing information from THUD into the helper to press the buttons accordingly. KillerJohn disabled any kind of network feature and
forced everyone to update. Zy changed their method to get the information out by writing directly to memory. KillerJohn disabled that too.
Then Zy wrote pixels to the screen and screen scraped the information. KillerJohn disabled it by using SetWindowDisplayAffinity 
(https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowdisplayaffinity). After Zy Helper, there OZ helper and
some others. In Season 22, KillerJohn made TurboHUD require administrative priveledges. This software now has full access to your machine, 
a huge security risk. 

By using SetWindowDisplayAffinity, a user can no longer screen shot the game with the overlay or stream the game on twitch/discord easily.
This project will remove the block from SetWindowDisplayAffinity, which results in a black screen when trying to screen shot or
stream on discord.

Instructions:

1. Create a DLL from UnblockScreenshot (https://github.com/typcn/UnblockScreenshot)
  note: You will need to download Visual C++ and compile it yourself.
  note: A compiled version for Windows 7 x64 and Windows 10 x64 are included, but you may need to compile your own for your machine.

2. Inject the DLL into the turobhud process using an injector (https://github.com/numaru/injector)
