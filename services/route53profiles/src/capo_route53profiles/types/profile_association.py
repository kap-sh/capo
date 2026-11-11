"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.account_id
    import capo_route53profiles.types.name
    import capo_route53profiles.types.priority
    import capo_route53profiles.types.profile_status
    import capo_route53profiles.types.resource_id
    import capo_route53profiles.types.rfc3339_timestamp
    import capo_route53profiles.types.string


class ProfileAssociation(TypedDict, closed=True):
    id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile association. </p>"""
    name: NotRequired["capo_route53profiles.types.name.Name"]
    """<p> Name of the Profile association. </p>"""
    owner_id: NotRequired["capo_route53profiles.types.account_id.AccountId"]
    """<p> Amazon Web Services account ID of the Profile association owner. </p>"""
    profile_id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> ID of the Profile. </p>"""
    resource_id: NotRequired["capo_route53profiles.types.resource_id.ResourceId"]
    """<p> The Amazon Resource Name (ARN) of the VPC. </p>"""
    status: NotRequired["capo_route53profiles.types.profile_status.ProfileStatus"]
    """<p> Status of the Profile association. </p>"""
    status_message: NotRequired["capo_route53profiles.types.string.String"]
    """<p> Additional information about the Profile association. </p>"""
    creation_time: NotRequired[
        "capo_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile association was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "capo_route53profiles.types.rfc3339_timestamp.Rfc3339Timestamp"
    ]
    """<p> The date and time that the Profile association was modified, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    priority: NotRequired["capo_route53profiles.types.priority.Priority"]
    """<p> The priority of the Profile association. Route 53 VPC Resolver evaluates the Profile associations for a VPC in priority order, starting with the lowest value. Associations created without a priority have priority 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "status" in value:
        import capo_route53profiles.types.profile_status

        out["Status"] = capo_route53profiles.types.profile_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_time" in value:
        import capo_route53profiles.types.rfc3339_timestamp

        out["CreationTime"] = (
            capo_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "modification_time" in value:
        import capo_route53profiles.types.rfc3339_timestamp

        out["ModificationTime"] = (
            capo_route53profiles.types.rfc3339_timestamp.serialize_json(
                value["modification_time"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> ProfileAssociation:
    out: ProfileAssociation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Status") is not None:
        import capo_route53profiles.types.profile_status

        out["status"] = capo_route53profiles.types.profile_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreationTime") is not None:
        import capo_route53profiles.types.rfc3339_timestamp

        out["creation_time"] = (
            capo_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if data.get("ModificationTime") is not None:
        import capo_route53profiles.types.rfc3339_timestamp

        out["modification_time"] = (
            capo_route53profiles.types.rfc3339_timestamp.deserialize_json(
                data["ModificationTime"]
            )
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    return out
