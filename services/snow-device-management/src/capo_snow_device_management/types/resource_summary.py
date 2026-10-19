"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ResourceSummary``."""

from typing_extensions import NotRequired, TypedDict


class ResourceSummary(TypedDict, closed=True):
    resource_type: "str"
    """<p>The resource type.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSummary) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ResourceSummary:
    out: ResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
