"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendRcsMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.max_price
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration
    import capo_pinpoint_sms_voice_v2.types.rcs_message_content
    import capo_pinpoint_sms_voice_v2.types.rcs_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.rcs_message_traffic_type
    import capo_pinpoint_sms_voice_v2.types.rcs_time_to_live


class SendRcsMessageRequest(TypedDict, closed=True):
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    origination_identity: "capo_pinpoint_sms_voice_v2.types.rcs_message_origination_identity.RcsMessageOriginationIdentity"
    """<p>The origination identity of the message. This can be either the RcsAgentId, RcsAgentArn, PoolId, or PoolArn.</p>"""
    rcs_message_content: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_message_content.RcsMessageContent"
    ]
    """<p>The content of the RCS message. Contains the message content (text, file, rich card, or carousel) and optional message-level suggested actions.</p>"""
    time_to_live: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_time_to_live.RcsTimeToLive"
    ]
    """<p>The duration in seconds that the RCS message is valid for delivery. If the message cannot be delivered within this duration, it is considered expired. Valid values are 1 to 172800 (48 hours). If a FallbackConfiguration is provided, the fallback is triggered when the duration expires without delivery confirmation.</p>"""
    message_traffic_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_message_traffic_type.RcsMessageTrafficType"
    ]
    """<p>The traffic type of the RCS message. Valid values are AUTHENTICATION, TRANSACTION, PROMOTION, SERVICE_REQUEST, and ACKNOWLEDGEMENT. This field is reserved for future use.</p>"""
    fallback_configuration: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration.RcsFallbackConfiguration"
    ]
    """<p>Configuration for SMS or MMS fallback when RCS delivery fails. If provided, the service sends a fallback message via the specified channel when the RCS message fails or the TimeToLive expires.</p>"""
    protect_configuration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    ]
    """<p>The unique identifier of the protect configuration to use.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    max_price: NotRequired["capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"]
    """<p>The maximum amount that you want to spend, in US dollars, per each RCS message.</p>"""
    dry_run: NotRequired["bool"]
    """<p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>"""
    context: NotRequired["capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendRcsMessageRequest) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["OriginationIdentity"] = value["origination_identity"]
    if "rcs_message_content" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_message_content

        out["RcsMessageContent"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_message_content.serialize_aws_json_1_0(
                value["rcs_message_content"]
            )
        )
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "message_traffic_type" in value:
        out["MessageTrafficType"] = value["message_traffic_type"]
    if "fallback_configuration" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration

        out["FallbackConfiguration"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration.serialize_aws_json_1_0(
                value["fallback_configuration"]
            )
        )
    if "protect_configuration_id" in value:
        out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "max_price" in value:
        out["MaxPrice"] = value["max_price"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "context" in value:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["Context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendRcsMessageRequest:
    out: SendRcsMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "SendRcsMessageRequest.destination_phone_number required"
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "SendRcsMessageRequest.origination_identity required"
        )
    if data.get("RcsMessageContent") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_message_content

        out["rcs_message_content"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_message_content.deserialize_aws_json_1_0(
                data["RcsMessageContent"]
            )
        )
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("MessageTrafficType") is not None:
        out["message_traffic_type"] = data["MessageTrafficType"]
    if data.get("FallbackConfiguration") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration

        out["fallback_configuration"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration.deserialize_aws_json_1_0(
                data["FallbackConfiguration"]
            )
        )
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("MaxPrice") is not None:
        out["max_price"] = data["MaxPrice"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("Context") is not None:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.deserialize_aws_json_1_0(
                data["Context"]
            )
        )
    if data.get("MessageFeedbackEnabled") is not None:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    return out
