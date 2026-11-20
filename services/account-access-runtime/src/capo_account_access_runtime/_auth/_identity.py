from __future__ import annotations

from datetime import datetime
from typing import TypedDict

from typing_extensions import NotRequired


class Identity(TypedDict):
    expiration: NotRequired[datetime | None]


class BearerToken(Identity):
    token: str
