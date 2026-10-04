"""Generated from Smithy shape ``com.amazonaws.endusermessaging#AttachmentBody``."""

import base64
from typing import TypeAlias

"""Attachment Body"""
AttachmentBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AttachmentBody:
    return base64.b64decode(data)
