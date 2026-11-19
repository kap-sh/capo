"""Generated from Smithy shape ``com.amazonaws.guardduty#SharedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class SharedResource(TypedDict, closed=True):
    resource_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the resource. This value isn't limited to the resource types of <code>InvestigationResource</code>.</p>"""
    identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SharedResource:
    out: SharedResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    return out
