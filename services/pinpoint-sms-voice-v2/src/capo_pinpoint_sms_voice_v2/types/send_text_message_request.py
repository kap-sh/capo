"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendTextMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.destination_country_parameters
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.max_price
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.text_message_body
    import capo_pinpoint_sms_voice_v2.types.text_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.time_to_live


class SendTextMessageRequest(TypedDict, closed=True):
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    origination_identity: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.text_message_origination_identity.TextMessageOriginationIdentity"
    ]
    """<p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, RcsAgentId, RcsAgentArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    message_body: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.text_message_body.TextMessageBody"
    ]
    """<p>The body of the text message.</p>"""
    message_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The type of message. Valid values are for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    keyword: NotRequired["capo_pinpoint_sms_voice_v2.types.keyword.Keyword"]
    """<p>When you register a short code in the US, you must specify a program name. If you don’t have a US short code, omit this attribute.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    max_price: NotRequired["capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"]
    """<p>The maximum amount that you want to spend, in US dollars, per each text message. If the calculated amount to send the text message is greater than <code>MaxPrice</code>, the message is not sent and an error is returned.</p>"""
    time_to_live: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
    ]
    """<p>How long the text message is valid for, in seconds. By default this is 72 hours. If the messages isn't handed off before the TTL expires we stop attempting to hand off the message and return <code>TTL_EXPIRED</code> event.</p>"""
    context: NotRequired["capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    destination_country_parameters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.destination_country_parameters.DestinationCountryParameters"
    ]
    """<p>This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html">Special requirements for sending SMS messages to recipients in India</a>. </p> <ul> <li> <p> <code>IN_ENTITY_ID</code> The entity ID or Principal Entity (PE) ID that you received after completing the sender ID registration process.</p> </li> <li> <p> <code>IN_TEMPLATE_ID</code> The template ID that you received after completing the sender ID registration process.</p> <important> <p>Make sure that the Template ID that you specify matches your message template exactly. If your message doesn't match the template that you provided during the registration process, the mobile carriers might reject your message.</p> </important> </li> </ul>"""
    dry_run: "bool"
    """<p>When set to true, the message is checked and validated, but isn't sent to the end recipient. You are not charged for using <code>DryRun</code>.</p> <p>The Message Parts per Second (MPS) limit when using <code>DryRun</code> is five. If your origination identity has a lower MPS limit then the lower MPS limit is used. For more information about MPS limits, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html">Message Parts per Second (MPS) limits</a> in the <i>End User Messaging SMS User Guide</i>..</p>"""
    protect_configuration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    ]
    """<p>The unique identifier for the protect configuration.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendTextMessageRequest) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "message_body" in value:
        out["MessageBody"] = value["message_body"]
    if "message_type" in value:
        out["MessageType"] = value["message_type"]
    if "keyword" in value:
        out["Keyword"] = value["keyword"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "max_price" in value:
        out["MaxPrice"] = value["max_price"]
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "context" in value:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["Context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "destination_country_parameters" in value:
        import capo_pinpoint_sms_voice_v2.types.destination_country_parameters

        out["DestinationCountryParameters"] = (
            capo_pinpoint_sms_voice_v2.types.destination_country_parameters.serialize_aws_json_1_0(
                value["destination_country_parameters"]
            )
        )
    out["DryRun"] = value.get("dry_run", False)
    if "protect_configuration_id" in value:
        out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendTextMessageRequest:
    out: SendTextMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "SendTextMessageRequest.destination_phone_number required"
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    if data.get("MessageBody") is not None:
        out["message_body"] = data["MessageBody"]
    if data.get("MessageType") is not None:
        out["message_type"] = data["MessageType"]
    if data.get("Keyword") is not None:
        out["keyword"] = data["Keyword"]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("MaxPrice") is not None:
        out["max_price"] = data["MaxPrice"]
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("Context") is not None:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.deserialize_aws_json_1_0(
                data["Context"]
            )
        )
    if data.get("DestinationCountryParameters") is not None:
        import capo_pinpoint_sms_voice_v2.types.destination_country_parameters

        out["destination_country_parameters"] = (
            capo_pinpoint_sms_voice_v2.types.destination_country_parameters.deserialize_aws_json_1_0(
                data["DestinationCountryParameters"]
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
