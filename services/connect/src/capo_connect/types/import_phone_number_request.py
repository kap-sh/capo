"""Generated from Smithy shape ``com.amazonaws.connect#ImportPhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number_description
    import capo_connect.types.tag_map


class ImportPhoneNumberRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    source_phone_number_arn: "capo_connect.types.arn.ARN"
    """<p>The claimed phone number ARN being imported from the external service, such as Amazon Web Services End User Messaging. If it is from Amazon Web Services End User Messaging, it looks like the ARN of the phone number to import from Amazon Web Services End User Messaging.</p>"""
    phone_number_description: NotRequired[
        "capo_connect.types.phone_number_description.PhoneNumberDescription"
    ]
    """<p>The description of the phone number.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPhoneNumberRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["SourcePhoneNumberArn"] = value["source_phone_number_arn"]
    if "phone_number_description" in value:
        out["PhoneNumberDescription"] = value["phone_number_description"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportPhoneNumberRequest:
    out: ImportPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("ImportPhoneNumberRequest.instance_id required")
    if data.get("SourcePhoneNumberArn") is not None:
        out["source_phone_number_arn"] = data["SourcePhoneNumberArn"]
    else:
        raise DeserializationError(
            "ImportPhoneNumberRequest.source_phone_number_arn required"
        )
    if data.get("PhoneNumberDescription") is not None:
        out["phone_number_description"] = data["PhoneNumberDescription"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
