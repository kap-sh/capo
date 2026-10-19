"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_id
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class GetMobileDeviceAccessOverrideRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to which you want to apply the override.</p>"""
    user_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>Identifies the WorkMail user for the override. Accepts the following types of user identities: </p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""
    device_id: "capo_workmail.types.device_id.DeviceId"
    """<p>The mobile device to which the override applies. <code>DeviceId</code> is case insensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessOverrideRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["DeviceId"] = value["device_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessOverrideRequest:
    out: GetMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
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
    return out
