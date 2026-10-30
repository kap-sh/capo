"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#InferenceBody``."""

import base64
from typing import TypeAlias

"""Sensitive binary payload containing customer inference data."""
InferenceBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: InferenceBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> InferenceBody:
    return base64.b64decode(data)
