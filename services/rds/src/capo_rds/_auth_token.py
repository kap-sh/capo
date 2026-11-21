"""IAM authentication tokens for database connections.

A token is a presigned SigV4 URL without its scheme, which the database takes as
the password. It is signed locally; nothing is sent to AWS.
"""

from __future__ import annotations

import urllib.parse

import zapros

from capo_rds._auth._identity import Credentials
from capo_rds._auth._sigv4 import SigV4AuthContext, presign_sigv4

# What a token signs as its payload: the SHA-256 of an empty body
_EMPTY_PAYLOAD_HASH = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def presign_auth_token(
    host: str,
    params: dict[str, str],
    *,
    credentials: Credentials,
    region: str,
    signing_name: str,
    expires_in: int,
) -> str:
    """A presigned GET of ``https://{host}/?{params}``, without the scheme: what the database takes as the password."""
    request = zapros.Request(
        zapros.URL(f"https://{host}/?{urllib.parse.urlencode(params)}"), "GET"
    )
    ctx: SigV4AuthContext = {
        "type": "sig_v4",
        "access_key_id": credentials["access_key"],
        "secret_access_key": credentials["secret_key"],
        "session_token": credentials.get("session_token"),
        "signing_region": region,
        "signing_name": signing_name,
        "disable_double_encoding": False,
        "disable_normalize_path": False,
    }
    presigned = presign_sigv4(
        request, ctx, expires_in=expires_in, payload_hash=_EMPTY_PAYLOAD_HASH
    )
    return str(presigned.url).removeprefix("https://")
