"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RequestPhoneNumberResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.number_status
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.requestable_number_type
    import capo_pinpoint_sms_voice_v2.types.tag_list
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class RequestPhoneNumberResult(TypedDict, closed=True):
    phone_number_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the requested phone number.</p>"""
    phone_number_id: NotRequired["str"]
    """<p>The unique identifier of the new phone number.</p>"""
    phone_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    ]
    """<p>The new phone number that was requested.</p>"""
    status: NotRequired["capo_pinpoint_sms_voice_v2.types.number_status.NumberStatus"]
    """<p>The current status of the request.</p>"""
    iso_country_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>"""
    message_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    number_capabilities: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    ]
    """<p>Indicates if the phone number will be used for text messages, voice messages or both. </p>"""
    number_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.requestable_number_type.RequestableNumberType"
    ]
    """<p>The type of number that was released.</p>"""
    monthly_leasing_price: NotRequired["str"]
    """<p>The monthly price, in US dollars, to lease the phone number.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The ARN used to identify the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList that is associated with the requested phone number.</p>"""
    international_sending_enabled: "bool"
    """<p>By default this is set to false. When set to true the international sending of phone number is Enabled. </p>"""
    deletion_protection_enabled: "bool"
    """<p>By default this is set to false. When set to true the phone number can't be deleted. </p>"""
    pool_id: NotRequired["str"]
    """<p>The unique identifier of the pool associated with the phone number </p>"""
    registration_id: NotRequired["str"]
    """<p>The unique identifier for the registration.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the phone number.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the phone number was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestPhoneNumberResult) -> dict:
    out: dict = {}
    if "phone_number_arn" in value:
        out["PhoneNumberArn"] = value["phone_number_arn"]
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "status" in value:
        out["Status"] = value["status"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "message_type" in value:
        out["MessageType"] = value["message_type"]
    if "number_capabilities" in value:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["NumberCapabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
                value["number_capabilities"]
            )
        )
    if "number_type" in value:
        out["NumberType"] = value["number_type"]
    if "monthly_leasing_price" in value:
        out["MonthlyLeasingPrice"] = value["monthly_leasing_price"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    out["InternationalSendingEnabled"] = value.get(
        "international_sending_enabled", False
    )
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "created_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestPhoneNumberResult:
    out: RequestPhoneNumberResult = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberArn") is not None:
        out["phone_number_arn"] = data["PhoneNumberArn"]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    if data.get("MessageType") is not None:
        out["message_type"] = data["MessageType"]
    if data.get("NumberCapabilities") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    if data.get("NumberType") is not None:
        out["number_type"] = data["NumberType"]
    if data.get("MonthlyLeasingPrice") is not None:
        out["monthly_leasing_price"] = data["MonthlyLeasingPrice"]
    if data.get("TwoWayEnabled") is not None:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    else:
        out["two_way_enabled"] = False
    if data.get("TwoWayChannelArn") is not None:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if data.get("TwoWayChannelRole") is not None:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if data.get("SelfManagedOptOutsEnabled") is not None:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    else:
        out["self_managed_opt_outs_enabled"] = False
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("InternationalSendingEnabled") is not None:
        out["international_sending_enabled"] = data["InternationalSendingEnabled"]
    else:
        out["international_sending_enabled"] = False
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
