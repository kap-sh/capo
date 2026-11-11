"""Generated from Smithy shape ``com.amazonaws.route53profiles#UpdateProfileAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.name
    import capo_route53profiles.types.priority
    import capo_route53profiles.types.resource_id


class UpdateProfileAssociationRequest(TypedDict, closed=True):
    profile_association_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the Profile association to update. </p>"""
    name: NotRequired["capo_route53profiles.types.name.Name"]
    """<p> The name of the Profile association. </p>"""
    priority: NotRequired["capo_route53profiles.types.priority.Priority"]
    """<p> The new priority of the Profile association. Route 53 VPC Resolver evaluates the Profile associations for a VPC in priority order, starting with the lowest value. </p> <p>The priority must be unique among the Profile associations for the VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileAssociationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> UpdateProfileAssociationRequest:
    out: UpdateProfileAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    return out
