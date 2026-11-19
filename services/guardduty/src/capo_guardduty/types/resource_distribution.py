"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.string


class ResourceDistribution(TypedDict, closed=True):
    resource_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The display name of the resource type, such as <code>Instance</code>.</p>"""
    identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the resource.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDistribution) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ResourceDistribution:
    out: ResourceDistribution = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    return out
