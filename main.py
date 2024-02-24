# (c) adarsh-goel
import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from client.main import StreamBot, start_client
from aiohttp import web
from server import web_server

string = 'BQAWgXwAhEWATO6TJoTDqNKrCA7sBoCRe0tz2grQjasFJYy9NCMr6oUUS1d6Lp2NSnWYbepgaN64Nfj2bTBFwgeXwkzRxsYDHpTIt9KTNbYAUZh5R3vm8cODMjFCh34c06qGd1L3tWJ6s_sDwqUmmh30iN-lw-hBFrYFHfn0r8hLKqBcYrFDSV-MqJA41934zF5opLXHwjoVr7gwHJ3HwQ8oeivT2LHPzhTfVHe9vGV_ypzLcfvElGMR5ZdYtQiQYxFhU2QliGTtRTOoL1Urx0PA8Mjckexl81q10euS413p4CU3ke_r_-uZtk1-Btept7xyqTegPfXbUEIC9EKwro6-A39ukwAAAABraHB9AQ'
# token = '5804042113:AAHDHqINXxrofNXoaM6LwcZJP5CCoxxDnPE'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

ppath = "modules/*.py"
files = glob.glob(ppath)

loop = asyncio.get_event_loop()


async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    await  StreamBot.start()
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    print("------------------------------ DONE ------------------------------")
    print()
    print(
        "---------------------- Initializing Clients ----------------------"
    )
    # await start_client(client='shjas',string=token)
    print("------------------------------ DONE ------------------------------")
    print('\n')
    print('--------------------------- Importing ---------------------------')


    print('-------------------- Initalizing Web Server -------------------------')
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "localhost"
    PORT = 8080
    await web.TCPSite(app, bind_address,PORT).start()
    print('----------------------------- DONE ---------------------------------------------------------------------')
    print('\n')
    print('---------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------')
    print(' follow me for more such exciting bots! https://github.com/ITZ-JEOL')
    print('---------------------------------------------------------------------------------------------------------')
    print('\n')
    print('----------------------- Service Started -----------------------------------------------------------------')
    print('                        bot =>> {}'.format((await StreamBot.get_me()).first_name))
    print('                        server ip =>> {}:{}'.format(bind_address, PORT))
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')