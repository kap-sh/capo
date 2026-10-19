"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteMobileDeviceAccessRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.mobile_device_access_rule_id
    import capo_workmail.types.organization_id


class DeleteMobileDeviceAccessRuleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which the rule will be deleted.</p>"""
    mobile_device_access_rule_id: (
        "capo_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    )
    """<p>The identifier of the rule to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMobileDeviceAccessRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMobileDeviceAccessRuleRequest:
    out: DeleteMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("MobileDeviceAccessRuleId") is not None:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    else:
        out["mobile_device_access_rule_id"] = ""
    return out
