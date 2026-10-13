"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SendChannelMessageRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_persistence_type
    import capo_chime_sdk_messaging.types.channel_message_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.client_request_token
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.message_attribute_map
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_content
    import capo_chime_sdk_messaging.types.push_notification_configuration
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.target_list


class SendChannelMessageRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    content: "capo_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    """<p>The content of the channel message.</p>"""
    type: "capo_chime_sdk_messaging.types.channel_message_type.ChannelMessageType"
    """<p>The type of message, <code>STANDARD</code> or <code>CONTROL</code>.</p> <p> <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p>"""
    persistence: "capo_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType"
    """<p>Boolean that controls whether the message is persisted on the back end. Required.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The optional metadata for each message.</p>"""
    client_request_token: (
        "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The <code>Idempotency</code> token for each client request.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    push_notification: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
    ]
    """<p>The push notification configuration of the message.</p>"""
    message_attributes: NotRequired[
        "capo_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>The attributes for the message, used for message filtering along with a <code>FilterRule</code> defined in the <code>PushNotificationPreferences</code>.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p>"""
    content_type: NotRequired["capo_chime_sdk_messaging.types.content_type.ContentType"]
    """<p>The content type of the channel message.</p>"""
    target: NotRequired["capo_chime_sdk_messaging.types.target_list.TargetList"]
    """<p>The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendChannelMessageRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    import capo_chime_sdk_messaging.types.channel_message_type

    out["Type"] = capo_chime_sdk_messaging.types.channel_message_type.serialize_json(
        value["type"]
    )
    import capo_chime_sdk_messaging.types.channel_message_persistence_type

    out["Persistence"] = (
        capo_chime_sdk_messaging.types.channel_message_persistence_type.serialize_json(
            value["persistence"]
        )
    )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
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
    if "target" in value:
        import capo_chime_sdk_messaging.types.target_list

        out["Target"] = capo_chime_sdk_messaging.types.target_list.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> SendChannelMessageRequest:
    out: SendChannelMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("SendChannelMessageRequest.content required")
    if data.get("Type") is not None:
        import capo_chime_sdk_messaging.types.channel_message_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_message_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SendChannelMessageRequest.type required")
    if data.get("Persistence") is not None:
        import capo_chime_sdk_messaging.types.channel_message_persistence_type

        out["persistence"] = (
            capo_chime_sdk_messaging.types.channel_message_persistence_type.deserialize_json(
                data["Persistence"]
            )
        )
    else:
        raise DeserializationError("SendChannelMessageRequest.persistence required")
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "SendChannelMessageRequest.client_request_token required"
        )
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
    if data.get("Target") is not None:
        import capo_chime_sdk_messaging.types.target_list

        out["target"] = capo_chime_sdk_messaging.types.target_list.deserialize_json(
            data["Target"]
        )
    return out


def redact_sensitive(value: SendChannelMessageRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    if "push_notification" in value:
        import capo_chime_sdk_messaging.types.push_notification_configuration

        out["push_notification"] = (
            capo_chime_sdk_messaging.types.push_notification_configuration.redact_sensitive(
                value["push_notification"]
            )
        )
    if "message_attributes" in value:
        out["message_attributes"] = "*** Sensitive Data Redacted ***"
    if "content_type" in value:
        out["content_type"] = "*** Sensitive Data Redacted ***"
    return out
