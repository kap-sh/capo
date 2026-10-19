"""Generated from Smithy shape ``com.amazonaws.workmail#PutMobileDeviceAccessOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_id
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.mobile_device_access_rule_description
    import capo_workmail.types.mobile_device_access_rule_effect
    import capo_workmail.types.organization_id


class PutMobileDeviceAccessOverrideRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>Identifies the WorkMail organization for which you create the override.</p>"""
    user_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The WorkMail user for which you create the override. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""
    device_id: "capo_workmail.types.device_id.DeviceId"
    """<p>The mobile device for which you create the override. <code>DeviceId</code> is case insensitive.</p>"""
    effect: "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    """<p>The effect of the override, <code>ALLOW</code> or <code>DENY</code>.</p>"""
    description: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>A description of the override.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMobileDeviceAccessOverrideRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["DeviceId"] = value["device_id"]
    import capo_workmail.types.mobile_device_access_rule_effect

    out["Effect"] = (
        capo_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutMobileDeviceAccessOverrideRequest:
    out: PutMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("Effect") is not None:
        import capo_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            capo_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect",
            "",
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
