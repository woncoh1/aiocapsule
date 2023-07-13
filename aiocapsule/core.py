# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/core.ipynb.

# %% ../nbs/core.ipynb 2
from __future__ import annotations

import aiohttp

# %% auto 0
__all__ = ['send_http_request']

# %% ../nbs/core.ipynb 4
async def send_http_request(
    method:str,
    url:str,
    headers:dict|None=None,
    params:dict|None=None,
    data:dict|str|None=None,
    json:dict|None=None,
    proxy:str|None=None,
    auth:aiohttp.BasicAuth|None=None,
    text:bool=False,
) -> str|dict:
    "Asynchronously send a HTTP request with a new session and return the response."
    async with aiohttp.ClientSession(
        headers=headers,
        auth=auth,
    ) as session:
        methods = {
            'GET': session.get,
            'POST': session.post,
            'DELETE': session.delete,
            'PUT': session.put,
        }
        request = methods.get(
            method,
            session.get,
        )
        async with request(
            url,
            params=params,
            data=data,
            json=json,
            proxy=proxy,
        ) as response:
            if text:
                return await response.text()
            else:
                return await response.json()