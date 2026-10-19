"""Generated from Smithy shape ``com.amazonaws.iot#HttpActionHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.header_key
    import capo_iot.types.header_value


class HttpActionHeader(TypedDict, closed=True):
    key: "capo_iot.types.header_key.HeaderKey"
    """<p>The HTTP header key.</p>"""
    value: "capo_iot.types.header_value.HeaderValue"
    """<p>The HTTP header value. Substitution templates are supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpActionHeader) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HttpActionHeader:
    out: HttpActionHeader = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
