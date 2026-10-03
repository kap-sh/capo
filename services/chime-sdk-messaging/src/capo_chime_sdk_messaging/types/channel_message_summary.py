"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_status_structure
    import capo_chime_sdk_messaging.types.channel_message_type
    import capo_chime_sdk_messaging.types.content
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.message_attribute_map
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_nullable_boolean
    import capo_chime_sdk_messaging.types.target_list
    import capo_chime_sdk_messaging.types.timestamp


class ChannelMessageSummary(TypedDict, closed=True):
    message_id: NotRequired["capo_chime_sdk_messaging.types.message_id.MessageId"]
    """<p>The ID of the message.</p>"""
    content: NotRequired["capo_chime_sdk_messaging.types.content.Content"]
    """<p>The content of the channel message. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata of the message.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_type.ChannelMessageType"
    ]
    """<p>The type of message.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the message summary was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was last updated.</p>"""
    last_edited_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a message was last edited.</p>"""
    sender: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The message sender.</p>"""
    redacted: "capo_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
    """<p>Indicates whether a message was redacted.</p>"""
    status: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_status_structure.ChannelMessageStatusStructure"
    ]
    """<p>The message status. The status value is <code>SENT</code> for messages sent to a channel without a channel flow. For channels associated with channel flow, the value determines the processing stage.</p>"""
    message_attributes: NotRequired[
        "capo_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    content_type: NotRequired["capo_chime_sdk_messaging.types.content_type.ContentType"]
    """<p>The content type of the channel message listed in the summary. For Amazon Lex V2 bot responses, the content type is <code>application/amz-chime-lex-msgs</code> for success responses and <code>application/amz-chime-lex-error</code> for failure responses. For more information, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html">Processing responses from an AppInstanceBot</a> in the <i>Amazon Chime SDK Messaging Developer Guide</i>.</p>"""
    target: NotRequired["capo_chime_sdk_messaging.types.target_list.TargetList"]
    """<p>The target of a message, a sender, a user, or a bot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageSummary) -> dict:
    out: dict = {}
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
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "last_edited_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastEditedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_edited_timestamp"]
            )
        )
    if "sender" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Sender"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["sender"]
        )
    out["Redacted"] = value.get("redacted", False)
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
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "target" in value:
        import capo_chime_sdk_messaging.types.target_list

        out["Target"] = capo_chime_sdk_messaging.types.target_list.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> ChannelMessageSummary:
    out: ChannelMessageSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("LastEditedTimestamp") is not None:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_edited_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastEditedTimestamp"]
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
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("Target") is not None:
        import capo_chime_sdk_messaging.types.target_list

        out["target"] = capo_chime_sdk_messaging.types.target_list.deserialize_json(
            data["Target"]
        )
    return out
