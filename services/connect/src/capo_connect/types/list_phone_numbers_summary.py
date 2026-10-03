"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number
    import capo_connect.types.phone_number_country_code
    import capo_connect.types.phone_number_description
    import capo_connect.types.phone_number_id
    import capo_connect.types.phone_number_type


class ListPhoneNumbersSummary(TypedDict, closed=True):
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
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through.</p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    phone_number_description: NotRequired[
        "capo_connect.types.phone_number_description.PhoneNumberDescription"
    ]
    """<p>The description of the phone number.</p>"""
    source_phone_number_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The claimed phone number ARN that was previously imported from the external service, such as Amazon Web Services End User Messaging. If it is from Amazon Web Services End User Messaging, it looks like the ARN of the phone number that was imported from Amazon Web Services End User Messaging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersSummary) -> dict:
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
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "phone_number_description" in value:
        out["PhoneNumberDescription"] = value["phone_number_description"]
    if "source_phone_number_arn" in value:
        out["SourcePhoneNumberArn"] = value["source_phone_number_arn"]
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersSummary:
    out: ListPhoneNumbersSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("PhoneNumberDescription") is not None:
        out["phone_number_description"] = data["PhoneNumberDescription"]
    if data.get("SourcePhoneNumberArn") is not None:
        out["source_phone_number_arn"] = data["SourcePhoneNumberArn"]
    return out
