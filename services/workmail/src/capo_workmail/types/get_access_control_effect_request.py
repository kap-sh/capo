"""Generated from Smithy shape ``com.amazonaws.workmail#GetAccessControlEffectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_action
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.ip_address
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_identifier


class GetAccessControlEffectRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization.</p>"""
    ip_address: "capo_workmail.types.ip_address.IpAddress"
    """<p>The IPv4 address.</p>"""
    action: "capo_workmail.types.access_control_rule_action.AccessControlRuleAction"
    """<p>The access protocol action. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    user_id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The user ID.</p>"""
    impersonation_role_id: NotRequired[
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    ]
    """<p>The impersonation role ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessControlEffectRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["IpAddress"] = value["ip_address"]
    out["Action"] = value["action"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "impersonation_role_id" in value:
        out["ImpersonationRoleId"] = value["impersonation_role_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessControlEffectRequest:
    out: GetAccessControlEffectRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    else:
        out["ip_address"] = ""
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("ImpersonationRoleId") is not None:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    return out
