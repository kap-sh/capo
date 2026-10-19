"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#PutMetadataFlagBody``."""

from typing_extensions import TypedDict


class PutMetadataFlagBody(TypedDict, closed=True):
    new_value: "str"
    """<p>The new information to store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMetadataFlagBody) -> dict:
    out: dict = {}
    out["newValue"] = value["new_value"]
    return out


def deserialize_json(data: dict) -> PutMetadataFlagBody:
    out: PutMetadataFlagBody = {}  # type: ignore[typeddict-item]
    if data.get("newValue") is not None:
        out["new_value"] = data["newValue"]
    else:
        out["new_value"] = ""
    return out
