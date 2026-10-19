"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultContentBlock``."""

from typing_extensions import TypedDict


class SearchResultContentBlock(TypedDict, closed=True):
    text: "str"
    """<p>The actual text content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultContentBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> SearchResultContentBlock:
    out: SearchResultContentBlock = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
