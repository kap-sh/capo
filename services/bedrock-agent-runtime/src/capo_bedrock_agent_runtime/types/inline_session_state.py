"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineSessionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.conversation_history
    import capo_bedrock_agent_runtime.types.input_files
    import capo_bedrock_agent_runtime.types.prompt_session_attributes_map
    import capo_bedrock_agent_runtime.types.return_control_invocation_results
    import capo_bedrock_agent_runtime.types.session_attributes_map


class InlineSessionState(TypedDict, closed=True):
    session_attributes: NotRequired[
        "capo_bedrock_agent_runtime.types.session_attributes_map.SessionAttributesMap"
    ]
    """<p> Contains attributes that persist across a session and the values of those attributes. </p>"""
    prompt_session_attributes: NotRequired[
        "capo_bedrock_agent_runtime.types.prompt_session_attributes_map.PromptSessionAttributesMap"
    ]
    """<p> Contains attributes that persist across a session and the values of those attributes. </p>"""
    return_control_invocation_results: NotRequired[
        "capo_bedrock_agent_runtime.types.return_control_invocation_results.ReturnControlInvocationResults"
    ]
    """<p> Contains information about the results from the action group invocation. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html">Return control to the agent developer</a>. </p> <note> <p>If you include this field in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    invocation_id: NotRequired["str"]
    """<p> The identifier of the invocation of an action. This value must match the <code>invocationId</code> returned in the <code>InvokeInlineAgent</code> response for the action whose results are provided in the <code>returnControlInvocationResults</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html">Return control to the agent developer</a>. </p>"""
    files: NotRequired["capo_bedrock_agent_runtime.types.input_files.InputFiles"]
    """<p> Contains information about the files used by code interpreter. </p>"""
    conversation_history: NotRequired[
        "capo_bedrock_agent_runtime.types.conversation_history.ConversationHistory"
    ]
    """<p> Contains the conversation history that persist across sessions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineSessionState) -> dict:
    out: dict = {}
    if "session_attributes" in value:
        import capo_bedrock_agent_runtime.types.session_attributes_map

        out["sessionAttributes"] = (
            capo_bedrock_agent_runtime.types.session_attributes_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "prompt_session_attributes" in value:
        import capo_bedrock_agent_runtime.types.prompt_session_attributes_map

        out["promptSessionAttributes"] = (
            capo_bedrock_agent_runtime.types.prompt_session_attributes_map.serialize_json(
                value["prompt_session_attributes"]
            )
        )
    if "return_control_invocation_results" in value:
        import capo_bedrock_agent_runtime.types.return_control_invocation_results

        out["returnControlInvocationResults"] = (
            capo_bedrock_agent_runtime.types.return_control_invocation_results.serialize_json(
                value["return_control_invocation_results"]
            )
        )
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    if "files" in value:
        import capo_bedrock_agent_runtime.types.input_files

        out["files"] = capo_bedrock_agent_runtime.types.input_files.serialize_json(
            value["files"]
        )
    if "conversation_history" in value:
        import capo_bedrock_agent_runtime.types.conversation_history

        out["conversationHistory"] = (
            capo_bedrock_agent_runtime.types.conversation_history.serialize_json(
                value["conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineSessionState:
    out: InlineSessionState = {}  # type: ignore[typeddict-item]
    if data.get("sessionAttributes") is not None:
        import capo_bedrock_agent_runtime.types.session_attributes_map

        out["session_attributes"] = (
            capo_bedrock_agent_runtime.types.session_attributes_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if data.get("promptSessionAttributes") is not None:
        import capo_bedrock_agent_runtime.types.prompt_session_attributes_map

        out["prompt_session_attributes"] = (
            capo_bedrock_agent_runtime.types.prompt_session_attributes_map.deserialize_json(
                data["promptSessionAttributes"]
            )
        )
    if data.get("returnControlInvocationResults") is not None:
        import capo_bedrock_agent_runtime.types.return_control_invocation_results

        out["return_control_invocation_results"] = (
            capo_bedrock_agent_runtime.types.return_control_invocation_results.deserialize_json(
                data["returnControlInvocationResults"]
            )
        )
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    if data.get("files") is not None:
        import capo_bedrock_agent_runtime.types.input_files

        out["files"] = capo_bedrock_agent_runtime.types.input_files.deserialize_json(
            data["files"]
        )
    if data.get("conversationHistory") is not None:
        import capo_bedrock_agent_runtime.types.conversation_history

        out["conversation_history"] = (
            capo_bedrock_agent_runtime.types.conversation_history.deserialize_json(
                data["conversationHistory"]
            )
        )
    return out
