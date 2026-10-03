"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationRuleSetNumberOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action


class ProtectConfigurationRuleSetNumberOverride(TypedDict, closed=True):
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the rule was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    action: "capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action.ProtectConfigurationRuleOverrideAction"
    """<p>The action for the rule to perform of either blocking or allowing messages to the destination phone number.</p>"""
    iso_country_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    expiration_timestamp: NotRequired["datetime.datetime"]
    """<p>The time the rule will expire at. If <code>ExpirationTimestamp</code> is not set then the rule will not expire.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtectConfigurationRuleSetNumberOverride) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["Action"] = value["action"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "expiration_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ExpirationTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProtectConfigurationRuleSetNumberOverride:
    out: ProtectConfigurationRuleSetNumberOverride = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "ProtectConfigurationRuleSetNumberOverride.destination_phone_number required"
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectConfigurationRuleSetNumberOverride.created_timestamp required"
        )
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        raise DeserializationError(
            "ProtectConfigurationRuleSetNumberOverride.action required"
        )
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    if data.get("ExpirationTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["expiration_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ExpirationTimestamp"]
            )
        )
    return out
