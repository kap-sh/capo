"""Generated from Smithy shape ``com.amazonaws.datazone#GroupProfileSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_profile_id
    import capo_datazone.types.group_profile_name
    import capo_datazone.types.group_profile_status


class GroupProfileSummary(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain of a group profile.</p>"""
    id: NotRequired["capo_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The ID of a group profile.</p>"""
    status: NotRequired["capo_datazone.types.group_profile_status.GroupProfileStatus"]
    """<p>The status of a group profile.</p>"""
    group_name: NotRequired["capo_datazone.types.group_profile_name.GroupProfileName"]
    """<p>The group name of a group profile.</p>"""
    role_principal_arn: NotRequired["str"]
    """<p>The ARN of the IAM role principal. This role is associated with the group profile.</p>"""
    role_principal_id: NotRequired["str"]
    """<p>The unique identifier of the IAM role principal. This principal is associated with the group profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupProfileSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        import capo_datazone.types.group_profile_status

        out["status"] = capo_datazone.types.group_profile_status.serialize_json(
            value["status"]
        )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "role_principal_arn" in value:
        out["rolePrincipalArn"] = value["role_principal_arn"]
    if "role_principal_id" in value:
        out["rolePrincipalId"] = value["role_principal_id"]
    return out


def deserialize_json(data: dict) -> GroupProfileSummary:
    out: GroupProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("status") is not None:
        import capo_datazone.types.group_profile_status

        out["status"] = capo_datazone.types.group_profile_status.deserialize_json(
            data["status"]
        )
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    if data.get("rolePrincipalArn") is not None:
        out["role_principal_arn"] = data["rolePrincipalArn"]
    if data.get("rolePrincipalId") is not None:
        out["role_principal_id"] = data["rolePrincipalId"]
    return out


def redact_sensitive(value: GroupProfileSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_name" in value:
        out["group_name"] = "*** Sensitive Data Redacted ***"
    return out
