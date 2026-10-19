"""Generated from Smithy shape ``com.amazonaws.workmail#ListMobileDeviceAccessOverridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_id
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.max_results
    import capo_workmail.types.next_token
    import capo_workmail.types.organization_id


class ListMobileDeviceAccessOverridesRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which to list mobile device access overrides.</p>"""
    user_id: NotRequired["capo_workmail.types.entity_identifier.EntityIdentifier"]
    """<p>The WorkMail user under which you list the mobile device access overrides. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""
    device_id: NotRequired["capo_workmail.types.device_id.DeviceId"]
    """<p>The mobile device to which the access override applies.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not require a token.</p>"""
    max_results: NotRequired["capo_workmail.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileDeviceAccessOverridesRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileDeviceAccessOverridesRequest:
    out: ListMobileDeviceAccessOverridesRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
