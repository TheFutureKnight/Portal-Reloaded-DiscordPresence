# Portal-Reloaded-DiscordPresence

## Installation:
- Install the mod from steam (of course you need to own portal 2 first)
- Install the exe from the release page or install the code (python) and run it/compile it/use it
- NOTE: THE EXE MIGHT TRIGGER SOME ANTI-VIRUSES. Sorry for the inconvenience.
- Replace it with the shortcut on your desktop (this won't be able to launch from steam unless you set it as a non-steam game)
- Enjoy your Rich Presence on Discord :)

### Pros:
- "It just works" - Todd Howard, CEO of Bethesda Games Studios
- Launches the game
- Closes when the game is closed
- will retry if Discord got closed while playing and carry on the time since you started playing if Discord opened up again

### Cons:
- It has pre-determined values for the Rich Presence, unless you download the code and recompile it yourself

#### Known issues:
- If you open the mod from the exe, then open normal Portal 2 then exit the mod version, the rich presence will remain running until you close that :(
- It only waits 15 minutes for portal mod to open, if it doesn't it just auto closes, so if there's a 20 minute worth of update re-open the exe

## To-Do list ~~(if I get requested to do them)~~:
- Add support for a config ini file that updates the values automatically ~~(Already know how and I have a version with that in mind, just not sure if other people would like that or not)~~

# The Code
So you've chosen to recompile the code? Well here's a small guide for it because it's pretty hard otherwise.

## Requirements:
- [Python](https://www.python.org/)
- [Pypresence](https://github.com/qwertyquerty/pypresence)
- [Psutil](https://pypi.org/project/psutil/)
- A compiler ;) the one used for this project is [Pyinstaller](https://github.com/pyinstaller/pyinstaller)

## Guide:
- After installing the requirements, edit the file if you wish, the strings of the rich presence are defined after the imports
- open cmd inside the folder where you have the python file in
- type in this line `pyinstaller --onefile "Portal Reloaded.pyw"`
- to add the icon just add this part `-i icon.ico`
- to use upx which is with the rest of the code at this part `--upx-dir=upx396`
- if it for some reason opens the console when click the exe (which by default it shouldn't) add this part `--noconsole`
- Note: if it opens the console (which it shouldn't) then just add `--noconsole` at the end
