"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SenderIdInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type_list
    import capo_pinpoint_sms_voice_v2.types.messaging_limits
    import capo_pinpoint_sms_voice_v2.types.sender_id


class SenderIdInformation(TypedDict, closed=True):
    sender_id_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the SenderId.</p>"""
    sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    """<p>The alphanumeric sender ID in a specific country that you'd like to describe.</p>"""
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>"""
    message_types: "capo_pinpoint_sms_voice_v2.types.message_type_list.MessageTypeList"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    monthly_leasing_price: "str"
    """<p>The monthly leasing price, in US dollars.</p>"""
    deletion_protection_enabled: "bool"
    """<p>By default this is set to false. When set to true the sender ID can't be deleted.</p>"""
    registered: "bool"
    """<p>True if the sender ID is registered.</p>"""
    registration_id: NotRequired["str"]
    """<p>The unique identifier for the registration.</p>"""
    messaging_limits: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.messaging_limits.MessagingLimits"
    ]
    """<p>The messaging limits that apply to the sender ID, including the per-capability send rates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderIdInformation) -> dict:
    out: dict = {}
    out["SenderIdArn"] = value["sender_id_arn"]
    out["SenderId"] = value["sender_id"]
    out["IsoCountryCode"] = value["iso_country_code"]
    import capo_pinpoint_sms_voice_v2.types.message_type_list

    out["MessageTypes"] = (
        capo_pinpoint_sms_voice_v2.types.message_type_list.serialize_aws_json_1_0(
            value["message_types"]
        )
    )
    out["MonthlyLeasingPrice"] = value["monthly_leasing_price"]
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    out["Registered"] = value.get("registered", False)
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "messaging_limits" in value:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["MessagingLimits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.serialize_aws_json_1_0(
                value["messaging_limits"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SenderIdInformation:
    out: SenderIdInformation = {}  # type: ignore[typeddict-item]
    if data.get("SenderIdArn") is not None:
        out["sender_id_arn"] = data["SenderIdArn"]
    else:
        raise DeserializationError("SenderIdInformation.sender_id_arn required")
    if data.get("SenderId") is not None:
        out["sender_id"] = data["SenderId"]
    else:
        raise DeserializationError("SenderIdInformation.sender_id required")
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("SenderIdInformation.iso_country_code required")
    if data.get("MessageTypes") is not None:
        import capo_pinpoint_sms_voice_v2.types.message_type_list

        out["message_types"] = (
            capo_pinpoint_sms_voice_v2.types.message_type_list.deserialize_aws_json_1_0(
                data["MessageTypes"]
            )
        )
    else:
        raise DeserializationError("SenderIdInformation.message_types required")
    if data.get("MonthlyLeasingPrice") is not None:
        out["monthly_leasing_price"] = data["MonthlyLeasingPrice"]
    else:
        raise DeserializationError("SenderIdInformation.monthly_leasing_price required")
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("Registered") is not None:
        out["registered"] = data["Registered"]
    else:
        out["registered"] = False
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    if data.get("MessagingLimits") is not None:
        import capo_pinpoint_sms_voice_v2.types.messaging_limits

        out["messaging_limits"] = (
            capo_pinpoint_sms_voice_v2.types.messaging_limits.deserialize_aws_json_1_0(
                data["MessagingLimits"]
            )
        )
    return out
