"""Generated from Smithy shape ``com.amazonaws.datazone#Resource``."""

from typing_extensions import NotRequired, TypedDict


class Resource(TypedDict, closed=True):
    provider: NotRequired["str"]
    """<p>The provider of a provisioned resource of this Amazon DataZone environment.</p>"""
    name: NotRequired["str"]
    """<p>The name of a provisioned resource of this Amazon DataZone environment.</p>"""
    value: "str"
    """<p>The value of a provisioned resource of this Amazon DataZone environment.</p>"""
    type: "str"
    """<p>The type of a provisioned resource of this Amazon DataZone environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "provider" in value:
        out["provider"] = value["provider"]
    if "name" in value:
        out["name"] = value["name"]
    out["value"] = value["value"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
