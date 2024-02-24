# Taken from megadlbot_oss <https://github.com/eyaadh/megadlbot_oss/blob/master/mega/webserver/routes.py>
# Thanks to Eyaadh <https://github.com/eyaadh>

import re
import time
import math
import logging
import secrets
import mimetypes
from aiohttp import web
import aiofiles
from aiohttp.http_exceptions import BadStatusLine
from client.main import StreamBot,start_client
from server.exceptions import FIleNotFound, InvalidHash
from utils.byte_treamer import ByteStreamer


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

class_cache = {}
multi_clients = {}
work_loads = {}
@routes.get("/{name}", allow_head=True)
async def chunked_transfer(request):
    range_header = request.headers.get("Range", 0)
    multi_clients[0] = StreamBot
    work_loads[0] = 0
    name = request.match_info['name']
    index = min(work_loads, key=work_loads.get)
    faster_client = multi_clients[index]
    if faster_client in class_cache:
        tg_connect = class_cache[faster_client]
        logging.debug(f"Using cached ByteStreamer object for client {index}")
    else:
        logging.debug(f"Creating new ByteStreamer object for client {index}")
        tg_connect = ByteStreamer(faster_client)
        class_cache[faster_client] = tg_connect
    file_id = await tg_connect.get_file_properties(int(name))

    file_size = file_id.file_size

    if range_header:
        from_bytes, until_bytes = range_header.replace("bytes=", "").split("-")
        from_bytes = int(from_bytes)
        until_bytes = int(until_bytes) if until_bytes else file_size - 1
    else:
        from_bytes = request.http_range.start or 0
        until_bytes = request.http_range.stop or file_size - 1
    text = f"hey {name}"
    return web.Response(text=text)

