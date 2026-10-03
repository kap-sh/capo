"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendMediaMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.max_price
    import capo_pinpoint_sms_voice_v2.types.media_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.media_url_list
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.text_message_body
    import capo_pinpoint_sms_voice_v2.types.time_to_live


class SendMediaMessageRequest(TypedDict, closed=True):
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    origination_identity: "capo_pinpoint_sms_voice_v2.types.media_message_origination_identity.MediaMessageOriginationIdentity"
    """<p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    message_body: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.text_message_body.TextMessageBody"
    ]
    """<p>The text body of the message.</p>"""
    media_urls: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.media_url_list.MediaUrlList"
    ]
    """<p>An array of URLs to each media file to send. </p> <p>The media files have to be stored in an S3 bucket. Supported media file formats are listed in <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/mms-limitations-character.html">MMS file types, size and character limits</a>. For more information on creating an S3 bucket and managing objects, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html">Creating a bucket</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html">Uploading objects</a> in the <i>Amazon S3 User Guide</i>, and <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/send-mms-message.html#send-mms-message-bucket">Setting up an Amazon S3 bucket for MMS files</a> in the <i>Amazon Web Services End User Messaging SMS User Guide</i>.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    max_price: NotRequired["capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"]
    """<p>The maximum amount that you want to spend, in US dollars, per each MMS message.</p>"""
    time_to_live: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
    ]
    """<p>How long the media message is valid for. By default this is 72 hours.</p>"""
    context: NotRequired["capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    dry_run: "bool"
    """<p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>"""
    protect_configuration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    ]
    """<p>The unique identifier of the protect configuration to use.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMediaMessageRequest) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["OriginationIdentity"] = value["origination_identity"]
    if "message_body" in value:
        out["MessageBody"] = value["message_body"]
    if "media_urls" in value:
        import capo_pinpoint_sms_voice_v2.types.media_url_list

        out["MediaUrls"] = (
            capo_pinpoint_sms_voice_v2.types.media_url_list.serialize_aws_json_1_0(
                value["media_urls"]
            )
        )
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
    out["DryRun"] = value.get("dry_run", False)
    if "protect_configuration_id" in value:
        out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendMediaMessageRequest:
    out: SendMediaMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "SendMediaMessageRequest.destination_phone_number required"
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "SendMediaMessageRequest.origination_identity required"
        )
    if data.get("MessageBody") is not None:
        out["message_body"] = data["MessageBody"]
    if data.get("MediaUrls") is not None:
        import capo_pinpoint_sms_voice_v2.types.media_url_list

        out["media_urls"] = (
            capo_pinpoint_sms_voice_v2.types.media_url_list.deserialize_aws_json_1_0(
                data["MediaUrls"]
            )
        )
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
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    if data.get("MessageFeedbackEnabled") is not None:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    return out
