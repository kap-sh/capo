"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ReleaseSenderIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type_list
    import capo_pinpoint_sms_voice_v2.types.sender_id


class ReleaseSenderIdResult(TypedDict, closed=True):
    sender_id_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the SenderId.</p>"""
    sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    """<p>The sender ID that was released.</p>"""
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    message_types: "capo_pinpoint_sms_voice_v2.types.message_type_list.MessageTypeList"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    monthly_leasing_price: "str"
    """<p>The monthly price, in US dollars, to lease the sender ID.</p>"""
    registered: "bool"
    """<p>True if the sender ID is registered.</p>"""
    registration_id: NotRequired["str"]
    """<p>The unique identifier for the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReleaseSenderIdResult) -> dict:
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
    out["Registered"] = value.get("registered", False)
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReleaseSenderIdResult:
    out: ReleaseSenderIdResult = {}  # type: ignore[typeddict-item]
    if data.get("SenderIdArn") is not None:
        out["sender_id_arn"] = data["SenderIdArn"]
    else:
        out["sender_id_arn"] = ""
    if data.get("SenderId") is not None:
        out["sender_id"] = data["SenderId"]
    else:
        out["sender_id"] = ""
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        out["iso_country_code"] = ""
    if data.get("MessageTypes") is not None:
        import capo_pinpoint_sms_voice_v2.types.message_type_list

        out["message_types"] = (
            capo_pinpoint_sms_voice_v2.types.message_type_list.deserialize_aws_json_1_0(
                data["MessageTypes"]
            )
        )
    else:
        out["message_types"] = []
    if data.get("MonthlyLeasingPrice") is not None:
        out["monthly_leasing_price"] = data["MonthlyLeasingPrice"]
    else:
        out["monthly_leasing_price"] = ""
    if data.get("Registered") is not None:
        out["registered"] = data["Registered"]
    else:
        out["registered"] = False
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    return out
