"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PhoneNumberInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.messaging_limits
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.number_status
    import capo_pinpoint_sms_voice_v2.types.number_type
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class PhoneNumberInformation(TypedDict, closed=True):
    phone_number_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the phone number.</p>"""
    phone_number_id: NotRequired["str"]
    """<p>The unique identifier for the phone number.</p>"""
    phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number in E.164 format.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.number_status.NumberStatus"
    """<p>The current status of the phone number.</p>"""
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>"""
    message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    number_capabilities: (
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    )
    """<p>Describes if the origination identity can be used for text messages, voice calls or both.</p>"""
    number_type: "capo_pinpoint_sms_voice_v2.types.number_type.NumberType"
    """<p>The type of phone number.</p>"""
    monthly_leasing_price: "str"
    """<p>The price, in US dollars, to lease the phone number.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out">Self-managed opt-outs</a> </p>"""
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    )
    """<p>The name of the OptOutList associated with the phone number.</p>"""
    international_sending_enabled: "bool"
    """<p>When set to true the international sending of phone number is Enabled.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true the phone number can't be deleted.</p>"""
    pool_id: NotRequired["str"]
    """<p>The unique identifier of the pool associated with the phone number.</p>"""
    registration_id: NotRequired["str"]
    """<p>The unique identifier for the registration.</p>"""
    messaging_limits: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.messaging_limits.MessagingLimits"
    ]
    """<p>The messaging limits that apply to the phone number, including the per-capability send rates and any advisory per-provider daily message caps.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the phone number was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PhoneNumberInformation) -> dict:
    out: dict = {}
    out["PhoneNumberArn"] = value["phone_number_arn"]
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    out["PhoneNumber"] = value["phone_number"]
    out["Status"] = value["status"]
    out["IsoCountryCode"] = value["iso_country_code"]
    out["MessageType"] = value["message_type"]
    import capo_pinpoint_sms_voice_v2.types.number_capability_list

    out["NumberCapabilities"] = (
        capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["number_capabilities"]
        )
    )
    out["NumberType"] = value["number_type"]
    out["MonthlyLeasingPrice"] = value["monthly_leasing_price"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    out["OptOutListName"] = value["opt_out_list_name"]
    out["InternationalSendingEnabled"] = value.get(
        "international_sending_enabled", False
    )
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "messaging_limits" in value:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["MessagingLimits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.serialize_aws_json_1_0(
                value["messaging_limits"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PhoneNumberInformation:
    out: PhoneNumberInformation = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberArn") is not None:
        out["phone_number_arn"] = data["PhoneNumberArn"]
    else:
        raise DeserializationError("PhoneNumberInformation.phone_number_arn required")
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("PhoneNumberInformation.phone_number required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("PhoneNumberInformation.status required")
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("PhoneNumberInformation.iso_country_code required")
    if data.get("MessageType") is not None:
        out["message_type"] = data["MessageType"]
    else:
        raise DeserializationError("PhoneNumberInformation.message_type required")
    if data.get("NumberCapabilities") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "PhoneNumberInformation.number_capabilities required"
        )
    if data.get("NumberType") is not None:
        out["number_type"] = data["NumberType"]
    else:
        raise DeserializationError("PhoneNumberInformation.number_type required")
    if data.get("MonthlyLeasingPrice") is not None:
        out["monthly_leasing_price"] = data["MonthlyLeasingPrice"]
    else:
        raise DeserializationError(
            "PhoneNumberInformation.monthly_leasing_price required"
        )
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
    else:
        raise DeserializationError("PhoneNumberInformation.opt_out_list_name required")
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
    if data.get("MessagingLimits") is not None:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["messaging_limits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.deserialize_aws_json_1_0(
                data["MessagingLimits"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("PhoneNumberInformation.created_timestamp required")
    return out
