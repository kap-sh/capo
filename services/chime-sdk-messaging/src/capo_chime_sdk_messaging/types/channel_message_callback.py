"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageCallback``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.message_attribute_map
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_content
    import capo_chime_sdk_messaging.types.push_notification_configuration
    import capo_chime_sdk_messaging.types.sub_channel_id


class ChannelMessageCallback(TypedDict, closed=True):
    message_id: "capo_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The message ID.</p>"""
    content: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    ]
    """<p>The message content. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The message metadata.</p>"""
    push_notification: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
    ]
    """<p>The push notification configuration of the message.</p>"""
    message_attributes: NotRequired[
        "capo_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel.</p>"""
    content_type: NotRequired["capo_chime_sdk_messaging.types.content_type.ContentType"]
    """<p>The content type of the call-back message. For Amazon Lex V2 bot responses, the content type is <code>application/amz-chime-lex-msgs</code> for success responses and <code>application/amz-chime-lex-error</code> for failure responses. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageCallback) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "push_notification" in value:
        import capo_chime_sdk_messaging.types.push_notification_configuration

        out["PushNotification"] = (
            capo_chime_sdk_messaging.types.push_notification_configuration.serialize_json(
                value["push_notification"]
            )
        )
    if "message_attributes" in value:
        import capo_chime_sdk_messaging.types.message_attribute_map

        out["MessageAttributes"] = (
            capo_chime_sdk_messaging.types.message_attribute_map.serialize_json(
                value["message_attributes"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> ChannelMessageCallback:
    out: ChannelMessageCallback = {}  # type: ignore[typeddict-item]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    else:
        raise DeserializationError("ChannelMessageCallback.message_id required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("PushNotification") is not None:
        import capo_chime_sdk_messaging.types.push_notification_configuration

        out["push_notification"] = (
            capo_chime_sdk_messaging.types.push_notification_configuration.deserialize_json(
                data["PushNotification"]
            )
        )
    if data.get("MessageAttributes") is not None:
        import capo_chime_sdk_messaging.types.message_attribute_map

        out["message_attributes"] = (
            capo_chime_sdk_messaging.types.message_attribute_map.deserialize_json(
                data["MessageAttributes"]
            )
        )
    if data.get("SubChannelId") is not None:
        out["sub_channel_id"] = data["SubChannelId"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    return out
