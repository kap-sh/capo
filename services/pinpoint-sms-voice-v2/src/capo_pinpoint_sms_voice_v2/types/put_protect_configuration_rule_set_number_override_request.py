"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutProtectConfigurationRuleSetNumberOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action


class PutProtectConfigurationRuleSetNumberOverrideRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    action: "capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action.ProtectConfigurationRuleOverrideAction"
    """<p>The action for the rule to either block or allow messages to the destination phone number.</p>"""
    expiration_timestamp: NotRequired["datetime.datetime"]
    """<p>The time the rule will expire at. If <code>ExpirationTimestamp</code> is not set then the rule does not expire.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: PutProtectConfigurationRuleSetNumberOverrideRequest,
) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["Action"] = value["action"]
    if "expiration_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ExpirationTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> PutProtectConfigurationRuleSetNumberOverrideRequest:
    out: PutProtectConfigurationRuleSetNumberOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        out["destination_phone_number"] = ""
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    if data.get("ExpirationTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["expiration_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ExpirationTimestamp"]
            )
        )
    return out
