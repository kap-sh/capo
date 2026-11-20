"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InferenceRouterBodyBlob``."""

import base64
from typing import TypeAlias

"""<p>The inference request or response body.</p>"""
InferenceRouterBodyBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: InferenceRouterBodyBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> InferenceRouterBodyBlob:
    return base64.b64decode(data)
