"""Generated from Smithy shape ``com.amazonaws.neptunedata#PropertygraphData``."""

from typing_extensions import NotRequired, TypedDict

PropertygraphData = TypedDict(
    "PropertygraphData",
    {
        "id": "str",
        "type": "str",
        "key": "str",
        "value": "object",
        "from": NotRequired["str"],
        "to": NotRequired["str"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PropertygraphData) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["key"] = value["key"]
    out["value"] = value["value"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    return out


def deserialize_json(data: dict) -> PropertygraphData:
    out: PropertygraphData = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    if data.get("from") is not None:
        out["from"] = data["from"]
    if data.get("to") is not None:
        out["to"] = data["to"]
    return out
