"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatSyncInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.attachments_input
    import capo_qbusiness.types.attribute_filter
    import capo_qbusiness.types.auth_challenge_response
    import capo_qbusiness.types.chat_mode
    import capo_qbusiness.types.chat_mode_configuration
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.message_id
    import capo_qbusiness.types.user_groups
    import capo_qbusiness.types.user_id
    import capo_qbusiness.types.user_message


class ChatSyncInput(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the Amazon Q Business conversation.</p>"""
    user_id: NotRequired["capo_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user attached to the chat input.</p>"""
    user_groups: NotRequired["capo_qbusiness.types.user_groups.UserGroups"]
    """<p>The group names that a user associated with the chat input belongs to.</p>"""
    user_message: NotRequired["capo_qbusiness.types.user_message.UserMessage"]
    """<p>A end user message in a conversation.</p>"""
    attachments: NotRequired["capo_qbusiness.types.attachments_input.AttachmentsInput"]
    """<p>A list of files uploaded directly during chat. You can upload a maximum of 5 files of upto 10 MB each.</p>"""
    action_execution: NotRequired[
        "capo_qbusiness.types.action_execution.ActionExecution"
    ]
    """<p>A request from an end user to perform an Amazon Q Business plugin action.</p>"""
    auth_challenge_response: NotRequired[
        "capo_qbusiness.types.auth_challenge_response.AuthChallengeResponse"
    ]
    """<p>An authentication verification event response by a third party authentication server to Amazon Q Business.</p>"""
    conversation_id: NotRequired["capo_qbusiness.types.conversation_id.ConversationId"]
    """<p>The identifier of the Amazon Q Business conversation.</p>"""
    parent_message_id: NotRequired["capo_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the previous system message in a conversation.</p>"""
    attribute_filter: NotRequired[
        "capo_qbusiness.types.attribute_filter.AttributeFilter"
    ]
    """<p>Enables filtering of Amazon Q Business web experience responses based on document attributes or metadata fields.</p>"""
    chat_mode: NotRequired["capo_qbusiness.types.chat_mode.ChatMode"]
    """<p>The <code>chatMode</code> parameter determines the chat modes available to Amazon Q Business users:</p> <ul> <li> <p> <code>RETRIEVAL_MODE</code> - If you choose this mode, Amazon Q generates responses solely from the data sources connected and indexed by the application. If an answer is not found in the data sources or there are no data sources available, Amazon Q will respond with a "<i>No Answer Found</i>" message, unless LLM knowledge has been enabled. In that case, Amazon Q will generate a response from the LLM knowledge</p> </li> <li> <p> <code>CREATOR_MODE</code> - By selecting this mode, you can choose to generate responses only from the LLM knowledge. You can also attach files and have Amazon Q generate a response based on the data in those files. If the attached files do not contain an answer for the query, Amazon Q will automatically fall back to generating a response from the LLM knowledge.</p> </li> <li> <p> <code>PLUGIN_MODE</code> - By selecting this mode, users can choose to use plugins in chat to get their responses.</p> </li> </ul> <note> <p>If none of the modes are selected, Amazon Q will only respond using the information from the attached files.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html">Admin controls and guardrails</a>, <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html">Plugins</a>, and <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope">Response sources</a>.</p>"""
    chat_mode_configuration: NotRequired[
        "capo_qbusiness.types.chat_mode_configuration.ChatModeConfiguration"
    ]
    """<p>The chat mode configuration for an Amazon Q Business application.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify a chat request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatSyncInput) -> dict:
    out: dict = {}
    if "user_message" in value:
        out["userMessage"] = value["user_message"]
    if "attachments" in value:
        import capo_qbusiness.types.attachments_input

        out["attachments"] = capo_qbusiness.types.attachments_input.serialize_json(
            value["attachments"]
        )
    if "action_execution" in value:
        import capo_qbusiness.types.action_execution

        out["actionExecution"] = capo_qbusiness.types.action_execution.serialize_json(
            value["action_execution"]
        )
    if "auth_challenge_response" in value:
        import capo_qbusiness.types.auth_challenge_response

        out["authChallengeResponse"] = (
            capo_qbusiness.types.auth_challenge_response.serialize_json(
                value["auth_challenge_response"]
            )
        )
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "parent_message_id" in value:
        out["parentMessageId"] = value["parent_message_id"]
    if "attribute_filter" in value:
        import capo_qbusiness.types.attribute_filter

        out["attributeFilter"] = capo_qbusiness.types.attribute_filter.serialize_json(
            value["attribute_filter"]
        )
    if "chat_mode" in value:
        import capo_qbusiness.types.chat_mode

        out["chatMode"] = capo_qbusiness.types.chat_mode.serialize_json(
            value["chat_mode"]
        )
    if "chat_mode_configuration" in value:
        import capo_qbusiness.types.chat_mode_configuration

        out["chatModeConfiguration"] = (
            capo_qbusiness.types.chat_mode_configuration.serialize_json(
                value["chat_mode_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ChatSyncInput:
    out: ChatSyncInput = {}  # type: ignore[typeddict-item]
    if data.get("userMessage") is not None:
        out["user_message"] = data["userMessage"]
    if data.get("attachments") is not None:
        import capo_qbusiness.types.attachments_input

        out["attachments"] = capo_qbusiness.types.attachments_input.deserialize_json(
            data["attachments"]
        )
    if data.get("actionExecution") is not None:
        import capo_qbusiness.types.action_execution

        out["action_execution"] = (
            capo_qbusiness.types.action_execution.deserialize_json(
                data["actionExecution"]
            )
        )
    if data.get("authChallengeResponse") is not None:
        import capo_qbusiness.types.auth_challenge_response

        out["auth_challenge_response"] = (
            capo_qbusiness.types.auth_challenge_response.deserialize_json(
                data["authChallengeResponse"]
            )
        )
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    if data.get("parentMessageId") is not None:
        out["parent_message_id"] = data["parentMessageId"]
    if data.get("attributeFilter") is not None:
        import capo_qbusiness.types.attribute_filter

        out["attribute_filter"] = (
            capo_qbusiness.types.attribute_filter.deserialize_json(
                data["attributeFilter"]
            )
        )
    if data.get("chatMode") is not None:
        import capo_qbusiness.types.chat_mode

        out["chat_mode"] = capo_qbusiness.types.chat_mode.deserialize_json(
            data["chatMode"]
        )
    if data.get("chatModeConfiguration") is not None:
        import capo_qbusiness.types.chat_mode_configuration

        out["chat_mode_configuration"] = (
            capo_qbusiness.types.chat_mode_configuration.deserialize_json(
                data["chatModeConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
