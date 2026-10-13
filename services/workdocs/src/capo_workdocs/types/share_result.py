"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.message_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.role_type
    import capo_workdocs.types.share_status_type


class ShareResult(TypedDict, closed=True):
    principal_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the principal.</p>"""
    invitee_principal_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the invited user.</p>"""
    role: NotRequired["capo_workdocs.types.role_type.RoleType"]
    """<p>The role.</p>"""
    status: NotRequired["capo_workdocs.types.share_status_type.ShareStatusType"]
    """<p>The status.</p>"""
    share_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the resource that was shared.</p>"""
    status_message: NotRequired["capo_workdocs.types.message_type.MessageType"]
    """<p>The status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareResult) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "invitee_principal_id" in value:
        out["InviteePrincipalId"] = value["invitee_principal_id"]
    if "role" in value:
        import capo_workdocs.types.role_type

        out["Role"] = capo_workdocs.types.role_type.serialize_json(value["role"])
    if "status" in value:
        import capo_workdocs.types.share_status_type

        out["Status"] = capo_workdocs.types.share_status_type.serialize_json(
            value["status"]
        )
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ShareResult:
    out: ShareResult = {}  # type: ignore[typeddict-item]
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    if data.get("InviteePrincipalId") is not None:
        out["invitee_principal_id"] = data["InviteePrincipalId"]
    if data.get("Role") is not None:
        import capo_workdocs.types.role_type

        out["role"] = capo_workdocs.types.role_type.deserialize_json(data["Role"])
    if data.get("Status") is not None:
        import capo_workdocs.types.share_status_type

        out["status"] = capo_workdocs.types.share_status_type.deserialize_json(
            data["Status"]
        )
    if data.get("ShareId") is not None:
        out["share_id"] = data["ShareId"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


def redact_sensitive(value: ShareResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "status_message" in value:
        out["status_message"] = "*** Sensitive Data Redacted ***"
    return out
