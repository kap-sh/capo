"""Canned S3 replies for the mocked clients in ``tests/s3/conftest.py``.

For tests that need a failure on demand (a proxy's HTML error page, a
throttled or timed-out request, ...), which a real endpoint cannot produce.
Replies are ``Mock.callback`` functions rather than ``Response`` objects: a
body can be read only once, and a mock may answer many times.
"""

from __future__ import annotations

from collections.abc import Callable

import pytest
from zapros import Request, Response
from zapros.matchers import method

Reply = Callable[[Request], Response]

LIST_BUCKETS = method("GET").path("/")
HEAD_OBJECT = method("HEAD").path("/key")

# Error bodies from something in front of S3, neither of them well-formed XML.
NGINX_PAGE = (
    b'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>502 Bad Gateway</title></head>'
    b"<body><center><h1>502 Bad Gateway</h1></center><hr><center>nginx</center></body></html>"
)
ENVOY_TEXT = b"upstream connect error or disconnect/reset before headers. reset reason: connection failure"
PROXY_BODIES = [pytest.param(NGINX_PAGE, id="nginx-html"), pytest.param(ENVOY_TEXT, id="envoy-text")]


def reply(status: int, body: bytes = b"") -> Reply:
    return lambda request: Response(status, content=body)


def s3_error(status: int, code: str) -> Reply:
    return reply(status, f"<Error><Code>{code}</Code><Message>m</Message></Error>".encode())


LIST_BUCKETS_OK = reply(200, b"<ListAllMyBucketsResult><Buckets/></ListAllMyBucketsResult>")
