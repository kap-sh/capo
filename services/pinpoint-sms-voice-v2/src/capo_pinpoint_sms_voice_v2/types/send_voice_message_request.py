"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendVoiceMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.max_price
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.time_to_live
    import capo_pinpoint_sms_voice_v2.types.voice_id
    import capo_pinpoint_sms_voice_v2.types.voice_message_body
    import capo_pinpoint_sms_voice_v2.types.voice_message_body_text_type
    import capo_pinpoint_sms_voice_v2.types.voice_message_origination_identity


class SendVoiceMessageRequest(TypedDict, closed=True):
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    origination_identity: "capo_pinpoint_sms_voice_v2.types.voice_message_origination_identity.VoiceMessageOriginationIdentity"
    """<p>The origination identity to use for the voice call. This can be the PhoneNumber, PhoneNumberId, PhoneNumberArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    message_body: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.voice_message_body.VoiceMessageBody"
    ]
    """<p>The text to convert to a voice message.</p>"""
    message_body_text_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.voice_message_body_text_type.VoiceMessageBodyTextType"
    ]
    """<p>Specifies if the MessageBody field contains text or <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">speech synthesis markup language (SSML)</a>.</p> <ul> <li> <p>TEXT: This is the default value. When used the maximum character limit is 3000.</p> </li> <li> <p>SSML: When used the maximum character limit is 6000 including SSML tagging.</p> </li> </ul>"""
    voice_id: NotRequired["capo_pinpoint_sms_voice_v2.types.voice_id.VoiceId"]
    """<p>The voice for the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly</a> service to use. By default this is set to "MATTHEW".</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    max_price_per_minute: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"
    ]
    """<p>The maximum amount to spend per voice message, in US dollars.</p>"""
    time_to_live: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
    ]
    """<p>How long the voice message is valid for. By default this is 72 hours.</p>"""
    context: NotRequired["capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    dry_run: "bool"
    """<p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>"""
    protect_configuration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    ]
    """<p>The unique identifier for the protect configuration.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendVoiceMessageRequest) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["OriginationIdentity"] = value["origination_identity"]
    if "message_body" in value:
        out["MessageBody"] = value["message_body"]
    if "message_body_text_type" in value:
        out["MessageBodyTextType"] = value["message_body_text_type"]
    if "voice_id" in value:
        out["VoiceId"] = value["voice_id"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "max_price_per_minute" in value:
        out["MaxPricePerMinute"] = value["max_price_per_minute"]
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "context" in value:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["Context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.serialize_aws_json_1_0(
                value["context"]
            )
        )
    out["DryRun"] = value.get("dry_run", False)
    if "protect_configuration_id" in value:
        out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendVoiceMessageRequest:
    out: SendVoiceMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "SendVoiceMessageRequest.destination_phone_number required"
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "SendVoiceMessageRequest.origination_identity required"
        )
    if data.get("MessageBody") is not None:
        out["message_body"] = data["MessageBody"]
    if data.get("MessageBodyTextType") is not None:
        out["message_body_text_type"] = data["MessageBodyTextType"]
    if data.get("VoiceId") is not None:
        out["voice_id"] = data["VoiceId"]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("MaxPricePerMinute") is not None:
        out["max_price_per_minute"] = data["MaxPricePerMinute"]
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("Context") is not None:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.deserialize_aws_json_1_0(
                data["Context"]
            )
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    if data.get("MessageFeedbackEnabled") is not None:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    return out
