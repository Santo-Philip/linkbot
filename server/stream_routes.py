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
from client.main import StreamBot
from server.exceptions import FIleNotFound, InvalidHash
from utils.byte_treamer import ByteStreamer


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
