"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.chat_input_stream
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.message_id
    import capo_qbusiness.types.user_groups
    import capo_qbusiness.types.user_id


class ChatInput(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to a streaming Amazon Q Business conversation.</p>"""
    user_id: NotRequired["capo_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user attached to the chat input. </p>"""
    user_groups: NotRequired["capo_qbusiness.types.user_groups.UserGroups"]
    """<p>The group names that a user associated with the chat input belongs to.</p>"""
    conversation_id: NotRequired["capo_qbusiness.types.conversation_id.ConversationId"]
    """<p>The identifier of the Amazon Q Business conversation.</p>"""
    parent_message_id: NotRequired["capo_qbusiness.types.message_id.MessageId"]
    """<p>The identifier used to associate a user message with a AI generated response.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the chat input.</p>"""
    input_stream: NotRequired["capo_qbusiness.types.chat_input_stream.ChatInputStream"]
    """<p>The streaming input for the <code>Chat</code> API.</p>"""


def redact_sensitive(value: ChatInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_stream" in value:
        out["input_stream"] = "*** Streaming Data Redacted ***"
    return out
