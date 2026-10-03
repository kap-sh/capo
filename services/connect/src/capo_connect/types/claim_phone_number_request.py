"""Generated from Smithy shape ``com.amazonaws.connect#ClaimPhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number
    import capo_connect.types.phone_number_description
    import capo_connect.types.tag_map


class ClaimPhoneNumberRequest(TypedDict, closed=True):
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    phone_number: "capo_connect.types.phone_number.PhoneNumber"
    """<p>The phone number you want to claim. Phone numbers are formatted <code>[+] [country code] [subscriber number including area code]</code>.</p>"""
    phone_number_description: NotRequired[
        "capo_connect.types.phone_number_description.PhoneNumberDescription"
    ]
    """<p>The description of the phone number.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>Pattern: <code>^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClaimPhoneNumberRequest) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    out["PhoneNumber"] = value["phone_number"]
    if "phone_number_description" in value:
        out["PhoneNumberDescription"] = value["phone_number_description"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ClaimPhoneNumberRequest:
    out: ClaimPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("ClaimPhoneNumberRequest.phone_number required")
    if data.get("PhoneNumberDescription") is not None:
        out["phone_number_description"] = data["PhoneNumberDescription"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
