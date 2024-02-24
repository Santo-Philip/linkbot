import asyncio
from pyrogram import Client
import platform
import psutil

api_id = 1474940
api_hash = "779e8d2b32ef76d0b7a11fb5f132a6b6"
token = '1802006653:AAE8Wo03glV_X51aMVUhM3W0outs5Q5sRXk'
plg = dict(root='modules')
string = 'BQAWgXwAMizhLTfPaid9DSVbusWDur-5UIWX9BO6pqEn-MAATcwYxFyqjU82QZQO_lwaaDjwbmik6QTIwwva_LJZ6KX0NfSz2XYxqNq1QecA9fHLHIGEHnJL8KLfbNWSDmo919grDCHlrdYjcSmJ15rDMEwCyLoq-V4jiYUF3Q8xLoPvCGF-DyxIrnLZWbELjxDUfv3sVBdzR9iN_A7UZ-opNFA87doMNo_pOkFv-ZFpXvO4icI79htJS-jY0Jz5CtP4fLysK9QDMN1X05lmSdjI72HrpIV9UwefVYoRSHb6sAbkwVKQCEaWeoSqJF56iOQA6L8t7itiKpTrRD7wV-cVruFUNQAAAABraHB9AQ'



StreamBot = Client(
    name='Web Streamer',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
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

