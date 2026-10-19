"""Generated from Smithy shape ``com.amazonaws.connectcases#TextAttributes``."""

from typing_extensions import TypedDict


class TextAttributes(TypedDict, closed=True):
    is_multiline: "bool"
    """<p>Attribute that defines rendering component and validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextAttributes) -> dict:
    out: dict = {}
    out["isMultiline"] = value["is_multiline"]
    return out


def deserialize_json(data: dict) -> TextAttributes:
    out: TextAttributes = {}  # type: ignore[typeddict-item]
    if data.get("isMultiline") is not None:
        out["is_multiline"] = data["isMultiline"]
    else:
        out["is_multiline"] = False
    return out
