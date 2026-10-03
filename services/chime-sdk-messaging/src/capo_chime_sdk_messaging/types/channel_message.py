"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_persistence_type
    import capo_chime_sdk_messaging.types.channel_message_status_structure
    import capo_chime_sdk_messaging.types.channel_message_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.content
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.message_attribute_map
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_nullable_boolean
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.target_list
    import capo_chime_sdk_messaging.types.timestamp


class ChannelMessage(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    message_id: NotRequired["capo_chime_sdk_messaging.types.message_id.MessageId"]
    """<p>The ID of a message.</p>"""
    content: NotRequired["capo_chime_sdk_messaging.types.content.Content"]
    """<p>The content of the channel message. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The message metadata.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_type.ChannelMessageType"
    ]
    """<p>The message type.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the message was created.</p>"""
    last_edited_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was edited.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was updated.</p>"""
    sender: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The message sender.</p>"""
    redacted: "capo_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
    """<p>Hides the content of a message.</p>"""
    persistence: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType"
    ]
    """<p>The persistence setting for a channel message.</p>"""
    status: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The status of the channel message.</p>"""
    message_attributes: NotRequired[
        "capo_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel.</p>"""
    content_type: NotRequired["capo_chime_sdk_messaging.types.content_type.ContentType"]
    """<p>The content type of the channel message. For Amazon Lex V2 bot responses, the content type is <code>application/amz-chime-lex-msgs</code> for success responses and <code>application/amz-chime-lex-error</code> for failure responses. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    target: NotRequired["capo_chime_sdk_messaging.types.target_list.TargetList"]
    """<p>The target of a message, a sender, a user, or a bot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessage) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "type" in value:
        import capo_chime_sdk_messaging.types.channel_message_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.channel_message_type.serialize_json(
                value["type"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_edited_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastEditedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_edited_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "sender" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Sender"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["sender"]
        )
    out["Redacted"] = value.get("redacted", False)
    if "persistence" in value:
        import capo_chime_sdk_messaging.types.channel_message_persistence_type

        out["Persistence"] = (
            capo_chime_sdk_messaging.types.channel_message_persistence_type.serialize_json(
                value["persistence"]
            )
        )
    if "status" in value:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["Status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.serialize_json(
                value["status"]
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


def deserialize_json(data: dict) -> ChannelMessage:
    out: ChannelMessage = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("Type") is not None:
        import capo_chime_sdk_messaging.types.channel_message_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_message_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastEditedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_edited_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastEditedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("Sender") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["sender"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Sender"]
        )
    if data.get("Redacted") is not None:
        out["redacted"] = data["Redacted"]
    else:
        out["redacted"] = False
    if data.get("Persistence") is not None:
        import capo_chime_sdk_messaging.types.channel_message_persistence_type

        out["persistence"] = (
            capo_chime_sdk_messaging.types.channel_message_persistence_type.deserialize_json(
                data["Persistence"]
            )
        )
    if data.get("Status") is not None:
        import capo_chime_sdk_messaging.types.channel_message_status_structure

        out["status"] = (
            capo_chime_sdk_messaging.types.channel_message_status_structure.deserialize_json(
                data["Status"]
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
