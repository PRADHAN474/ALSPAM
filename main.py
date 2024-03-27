import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"AltBots/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"AltBots.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["AltBots.modules." + plugin_name] = load
    print("𝗢𝗫𝗬𝗚𝗘𝗡 𝗛𝗔𝗦 𝗜𝗠𝗣𝗢𝗥𝗧𝗘𝗗 " + plugin_name)


files = glob.glob("AltBots/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\𝗢𝗫𝗬𝗚𝗘𝗡 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗗𝗘𝗣𝗟𝗢𝗬𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬⚡\nMy Master ---> 🦋⃟ ᴠͥɪͣᴘͫ ꪀꪖ𝘬𝘴ꫝ🥀🦋͜͡•─⃛͢ @naksh_hu_vai")


async def main():
    await X1.run_until_disconnected()
    await X2.run_until_disconnected()
    await X3.run_until_disconnected()
    await X4.run_until_disconnected()
    await X5.run_until_disconnected()
    await X6.run_until_disconnected()
    await X7.run_until_disconnected()
    await X8.run_until_disconnected()
    await X9.run_until_disconnected()
    await X10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
