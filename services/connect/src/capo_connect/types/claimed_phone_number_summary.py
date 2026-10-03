"""Generated from Smithy shape ``com.amazonaws.connect#ClaimedPhoneNumberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number
    import capo_connect.types.phone_number_country_code
    import capo_connect.types.phone_number_description
    import capo_connect.types.phone_number_id
    import capo_connect.types.phone_number_status
    import capo_connect.types.phone_number_type
    import capo_connect.types.tag_map


class ClaimedPhoneNumberSummary(TypedDict, closed=True):
    phone_number_id: NotRequired["capo_connect.types.phone_number_id.PhoneNumberId"]
    """<p>A unique identifier for the phone number.</p>"""
    phone_number_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the phone number.</p>"""
    phone_number: NotRequired["capo_connect.types.phone_number.PhoneNumber"]
    """<p>The phone number. Phone numbers are formatted <code>[+] [country code] [subscriber number including area code]</code>.</p>"""
    phone_number_country_code: NotRequired[
        "capo_connect.types.phone_number_country_code.PhoneNumberCountryCode"
    ]
    """<p>The ISO country code.</p>"""
    phone_number_type: NotRequired[
        "capo_connect.types.phone_number_type.PhoneNumberType"
    ]
    """<p>The type of phone number.</p>"""
    phone_number_description: NotRequired[
        "capo_connect.types.phone_number_description.PhoneNumberDescription"
    ]
    """<p>The description of the phone number.</p>"""
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through.</p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    phone_number_status: NotRequired[
        "capo_connect.types.phone_number_status.PhoneNumberStatus"
    ]
    """<p>The status of the phone number.</p> <ul> <li> <p> <code>CLAIMED</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html">ClaimPhoneNumber</a> or <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html">UpdatePhoneNumber</a> operation succeeded.</p> </li> <li> <p> <code>IN_PROGRESS</code> means a <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html">ClaimPhoneNumber</a>, <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html">UpdatePhoneNumber</a>, or <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumberMetadata.html">UpdatePhoneNumberMetadata</a> operation is still in progress and has not yet completed. You can call <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html">DescribePhoneNumber</a> at a later time to verify if the previous operation has completed.</p> </li> <li> <p> <code>FAILED</code> indicates that the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html">ClaimPhoneNumber</a> or <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html">UpdatePhoneNumber</a> operation has failed. It will include a message indicating the failure reason. A common reason for a failure may be that the <code>TargetArn</code> value you are claiming or updating a phone number to has reached its limit of total claimed numbers. If you received a <code>FAILED</code> status from a <code>ClaimPhoneNumber</code> API call, you have one day to retry claiming the phone number before the number is released back to the inventory for other customers to claim.</p> </li> </ul> <note> <p>You will not be billed for the phone number during the 1-day period if number claiming fails. </p> </note>"""
    source_phone_number_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The claimed phone number ARN that was previously imported from the external service, such as Amazon Web Services End User Messaging. If it is from Amazon Web Services End User Messaging, it looks like the ARN of the phone number that was imported from Amazon Web Services End User Messaging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClaimedPhoneNumberSummary) -> dict:
    out: dict = {}
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "phone_number_arn" in value:
        out["PhoneNumberArn"] = value["phone_number_arn"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "phone_number_country_code" in value:
        import capo_connect.types.phone_number_country_code

        out["PhoneNumberCountryCode"] = (
            capo_connect.types.phone_number_country_code.serialize_json(
                value["phone_number_country_code"]
            )
        )
    if "phone_number_type" in value:
        import capo_connect.types.phone_number_type

        out["PhoneNumberType"] = capo_connect.types.phone_number_type.serialize_json(
            value["phone_number_type"]
        )
    if "phone_number_description" in value:
        out["PhoneNumberDescription"] = value["phone_number_description"]
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "phone_number_status" in value:
        import capo_connect.types.phone_number_status

        out["PhoneNumberStatus"] = (
            capo_connect.types.phone_number_status.serialize_json(
                value["phone_number_status"]
            )
        )
    if "source_phone_number_arn" in value:
        out["SourcePhoneNumberArn"] = value["source_phone_number_arn"]
    return out


def deserialize_json(data: dict) -> ClaimedPhoneNumberSummary:
    out: ClaimedPhoneNumberSummary = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    if data.get("PhoneNumberArn") is not None:
        out["phone_number_arn"] = data["PhoneNumberArn"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("PhoneNumberCountryCode") is not None:
        import capo_connect.types.phone_number_country_code

        out["phone_number_country_code"] = (
            capo_connect.types.phone_number_country_code.deserialize_json(
                data["PhoneNumberCountryCode"]
            )
        )
    if data.get("PhoneNumberType") is not None:
        import capo_connect.types.phone_number_type

        out["phone_number_type"] = (
            capo_connect.types.phone_number_type.deserialize_json(
                data["PhoneNumberType"]
            )
        )
    if data.get("PhoneNumberDescription") is not None:
        out["phone_number_description"] = data["PhoneNumberDescription"]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("PhoneNumberStatus") is not None:
        import capo_connect.types.phone_number_status

        out["phone_number_status"] = (
            capo_connect.types.phone_number_status.deserialize_json(
                data["PhoneNumberStatus"]
            )
        )
    if data.get("SourcePhoneNumberArn") is not None:
        out["source_phone_number_arn"] = data["SourcePhoneNumberArn"]
    return out
