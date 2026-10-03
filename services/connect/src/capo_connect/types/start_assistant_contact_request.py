"""Generated from Smithy shape ``com.amazonaws.connect#StartAssistantContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.ai_agent_input
    import capo_connect.types.attributes
    import capo_connect.types.chat_message
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.participant_details
    import capo_connect.types.persistent_chat


class StartAssistantContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    ai_agent: "capo_connect.types.ai_agent_input.AiAgentInput"
    """<p>The AI agent configuration for this contact.</p>"""
    participant_details: "capo_connect.types.participant_details.ParticipantDetails"
    """<p>The display name and other details that identify the chat participant.</p>"""
    initial_message: NotRequired["capo_connect.types.chat_message.ChatMessage"]
    """<p>The initial message to send to the newly created chat.</p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A map of key-value pairs to associate with the contact. We make these attributes available to flows as standard contact attributes.</p> <p>You can provide up to 32,768 UTF-8 bytes across all key-value pairs for each contact.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    persistent_chat: NotRequired["capo_connect.types.persistent_chat.PersistentChat"]
    """<p>The configuration that enables persistent chat. For more information about persistent chat and its use cases, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html">Enable persistent chat</a>.</p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of an Connect Customer contact related to the new assistant contact.</p> <note> <p>You cannot provide both <code>RelatedContactId</code> and <code>PersistentChat</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssistantContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.ai_agent_input

    out["AiAgent"] = capo_connect.types.ai_agent_input.serialize_json(value["ai_agent"])
    import capo_connect.types.participant_details

    out["ParticipantDetails"] = capo_connect.types.participant_details.serialize_json(
        value["participant_details"]
    )
    if "initial_message" in value:
        import capo_connect.types.chat_message

        out["InitialMessage"] = capo_connect.types.chat_message.serialize_json(
            value["initial_message"]
        )
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "persistent_chat" in value:
        import capo_connect.types.persistent_chat

        out["PersistentChat"] = capo_connect.types.persistent_chat.serialize_json(
            value["persistent_chat"]
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    return out


def deserialize_json(data: dict) -> StartAssistantContactRequest:
    out: StartAssistantContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartAssistantContactRequest.instance_id required")
    if data.get("AiAgent") is not None:
        import capo_connect.types.ai_agent_input

        out["ai_agent"] = capo_connect.types.ai_agent_input.deserialize_json(
            data["AiAgent"]
        )
    else:
        raise DeserializationError("StartAssistantContactRequest.ai_agent required")
    if data.get("ParticipantDetails") is not None:
        import capo_connect.types.participant_details

        out["participant_details"] = (
            capo_connect.types.participant_details.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartAssistantContactRequest.participant_details required"
        )
    if data.get("InitialMessage") is not None:
        import capo_connect.types.chat_message

        out["initial_message"] = capo_connect.types.chat_message.deserialize_json(
            data["InitialMessage"]
        )
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("PersistentChat") is not None:
        import capo_connect.types.persistent_chat

        out["persistent_chat"] = capo_connect.types.persistent_chat.deserialize_json(
            data["PersistentChat"]
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    return out
