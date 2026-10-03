"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Item``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.attachments
    import capo_connectparticipant.types.chat_content
    import capo_connectparticipant.types.chat_content_type
    import capo_connectparticipant.types.chat_item_id
    import capo_connectparticipant.types.chat_item_type
    import capo_connectparticipant.types.contact_id
    import capo_connectparticipant.types.display_name
    import capo_connectparticipant.types.instant
    import capo_connectparticipant.types.message_metadata
    import capo_connectparticipant.types.participant_id
    import capo_connectparticipant.types.participant_role


class Item(TypedDict, closed=True):
    absolute_time: NotRequired["capo_connectparticipant.types.instant.Instant"]
    """<p>The time when the message or event was sent.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""
    content: NotRequired["capo_connectparticipant.types.chat_content.ChatContent"]
    """<p>The content of the message or event.</p>"""
    content_type: NotRequired[
        "capo_connectparticipant.types.chat_content_type.ChatContentType"
    ]
    """<p>The type of content of the item.</p>"""
    id: NotRequired["capo_connectparticipant.types.chat_item_id.ChatItemId"]
    """<p>The ID of the item.</p>"""
    type: NotRequired["capo_connectparticipant.types.chat_item_type.ChatItemType"]
    """<p>Type of the item: message or event. </p>"""
    participant_id: NotRequired[
        "capo_connectparticipant.types.participant_id.ParticipantId"
    ]
    """<p>The ID of the sender in the session.</p>"""
    display_name: NotRequired["capo_connectparticipant.types.display_name.DisplayName"]
    """<p>The chat display name of the sender.</p>"""
    participant_role: NotRequired[
        "capo_connectparticipant.types.participant_role.ParticipantRole"
    ]
    """<p>The role of the sender. For example, is it a customer, agent, or system.</p>"""
    attachments: NotRequired["capo_connectparticipant.types.attachments.Attachments"]
    """<p>Provides information about the attachments.</p>"""
    message_metadata: NotRequired[
        "capo_connectparticipant.types.message_metadata.MessageMetadata"
    ]
    """<p>The metadata related to the message. Currently this supports only information related to message receipts.</p>"""
    related_contact_id: NotRequired[
        "capo_connectparticipant.types.contact_id.ContactId"
    ]
    """<p>The contactId on which the transcript item was originally sent. This field is only populated for persistent chats when the transcript item is from the past chat session. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html">Enable persistent chat</a>.</p>"""
    contact_id: NotRequired["capo_connectparticipant.types.contact_id.ContactId"]
    """<p>The contactId on which the transcript item was originally sent. This field is populated only when the transcript item is from the current chat session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Item) -> dict:
    out: dict = {}
    if "absolute_time" in value:
        out["AbsoluteTime"] = value["absolute_time"]
    if "content" in value:
        out["Content"] = value["content"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_connectparticipant.types.chat_item_type

        out["Type"] = capo_connectparticipant.types.chat_item_type.serialize_json(
            value["type"]
        )
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "participant_role" in value:
        import capo_connectparticipant.types.participant_role

        out["ParticipantRole"] = (
            capo_connectparticipant.types.participant_role.serialize_json(
                value["participant_role"]
            )
        )
    if "attachments" in value:
        import capo_connectparticipant.types.attachments

        out["Attachments"] = capo_connectparticipant.types.attachments.serialize_json(
            value["attachments"]
        )
    if "message_metadata" in value:
        import capo_connectparticipant.types.message_metadata

        out["MessageMetadata"] = (
            capo_connectparticipant.types.message_metadata.serialize_json(
                value["message_metadata"]
            )
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> Item:
    out: Item = {}  # type: ignore[typeddict-item]
    if data.get("AbsoluteTime") is not None:
        out["absolute_time"] = data["AbsoluteTime"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_connectparticipant.types.chat_item_type

        out["type"] = capo_connectparticipant.types.chat_item_type.deserialize_json(
            data["Type"]
        )
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("ParticipantRole") is not None:
        import capo_connectparticipant.types.participant_role

        out["participant_role"] = (
            capo_connectparticipant.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    if data.get("Attachments") is not None:
        import capo_connectparticipant.types.attachments

        out["attachments"] = capo_connectparticipant.types.attachments.deserialize_json(
            data["Attachments"]
        )
    if data.get("MessageMetadata") is not None:
        import capo_connectparticipant.types.message_metadata

        out["message_metadata"] = (
            capo_connectparticipant.types.message_metadata.deserialize_json(
                data["MessageMetadata"]
            )
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    return out
