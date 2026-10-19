"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteAccessControlRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_name
    import capo_workmail.types.organization_id


class DeleteAccessControlRuleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization.</p>"""
    name: "capo_workmail.types.access_control_rule_name.AccessControlRuleName"
    """<p>The name of the access control rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccessControlRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccessControlRuleRequest:
    out: DeleteAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
