"""Generated from Smithy shape ``com.amazonaws.workmail#GetImpersonationRoleEffectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.organization_id


class GetImpersonationRoleEffectRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization where the impersonation role is defined.</p>"""
    impersonation_role_id: (
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The impersonation role ID to test.</p>"""
    target_user: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The WorkMail organization user chosen to test the impersonation role. The following identity formats are available:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImpersonationRoleEffectRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
    out["TargetUser"] = value["target_user"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImpersonationRoleEffectRequest:
    out: GetImpersonationRoleEffectRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("ImpersonationRoleId") is not None:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    else:
        out["impersonation_role_id"] = ""
    if data.get("TargetUser") is not None:
        out["target_user"] = data["TargetUser"]
    else:
        out["target_user"] = ""
    return out
