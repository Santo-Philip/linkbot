import asyncio
from pyrogram import Client
import platform
import psutil

api_id = 1474940
api_hash = "779e8d2b32ef76d0b7a11fb5f132a6b6"
token = '1802006653:AAGzce8dLMJU534x4Q4RN5iBbbklggMGbU4'
plg = dict(root='modules')
string = 'BQAWgXwAhEWATO6TJoTDqNKrCA7sBoCRe0tz2grQjasFJYy9NCMr6oUUS1d6Lp2NSnWYbepgaN64Nfj2bTBFwgeXwkzRxsYDHpTIt9KTNbYAUZh5R3vm8cODMjFCh34c06qGd1L3tWJ6s_sDwqUmmh30iN-lw-hBFrYFHfn0r8hLKqBcYrFDSV-MqJA41934zF5opLXHwjoVr7gwHJ3HwQ8oeivT2LHPzhTfVHe9vGV_ypzLcfvElGMR5ZdYtQiQYxFhU2QliGTtRTOoL1Urx0PA8Mjckexl81q10euS413p4CU3ke_r_-uZtk1-Btept7xyqTegPfXbUEIC9EKwro6-A39ukwAAAABraHB9AQ'



StreamBot = Client(
    name='Web Streamer',
    api_id=api_id,
    api_hash=api_hash,
    session_string=string,
    plugins=plg
)

async def start_client(client,string):
    try:
        client = await Client(client, api_id=api_id, api_hash=api_hash,session_string=string,plugins=plg).start()
        await asyncio.sleep(2)
        await client.send_message(1205330781,'hello')
        my_system = platform.uname()

        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")
        print(f"Ram Used : {psutil.virtual_memory().percent}%")
        print(f"Available Ram : {psutil.virtual_memory().available * 100 / psutil.virtual_memory().total:.2f}%")

    except Exception as e:
        print(f"Client initialization in stream bot failed with error : {e}")

