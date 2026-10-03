"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.conversation_history
    import capo_bedrock_agent_runtime.types.input_files
    import capo_bedrock_agent_runtime.types.knowledge_base_configurations
    import capo_bedrock_agent_runtime.types.prompt_session_attributes_map
    import capo_bedrock_agent_runtime.types.return_control_invocation_results
    import capo_bedrock_agent_runtime.types.session_attributes_map


class SessionState(TypedDict, closed=True):
    session_attributes: NotRequired[
        "capo_bedrock_agent_runtime.types.session_attributes_map.SessionAttributesMap"
    ]
    """<p>Contains attributes that persist across a session and the values of those attributes. If <code>sessionAttributes</code> are passed to a supervisor agent in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html">multi-agent collaboration</a>, it will be forwarded to all agent collaborators.</p>"""
    prompt_session_attributes: NotRequired[
        "capo_bedrock_agent_runtime.types.prompt_session_attributes_map.PromptSessionAttributesMap"
    ]
    """<p>Contains attributes that persist across a prompt and the values of those attributes. </p> <ul> <li> <p>In orchestration prompt template, these attributes replace the $prompt_session_attributes$ placeholder variable. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html">Prompt template placeholder variables</a>.</p> </li> <li> <p>In <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html">multi-agent collaboration</a>, the <code>promptSessionAttributes</code> will only be used by supervisor agent when $prompt_session_attributes$ is present in prompt template. </p> </li> </ul>"""
    return_control_invocation_results: NotRequired[
        "capo_bedrock_agent_runtime.types.return_control_invocation_results.ReturnControlInvocationResults"
    ]
    """<p>Contains information about the results from the action group invocation. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html">Return control to the agent developer</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p> <note> <p>If you include this field, the <code>inputText</code> field will be ignored.</p> </note>"""
    invocation_id: NotRequired["str"]
    """<p>The identifier of the invocation of an action. This value must match the <code>invocationId</code> returned in the <code>InvokeAgent</code> response for the action whose results are provided in the <code>returnControlInvocationResults</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html">Return control to the agent developer</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p>"""
    files: NotRequired["capo_bedrock_agent_runtime.types.input_files.InputFiles"]
    """<p>Contains information about the files used by code interpreter.</p>"""
    knowledge_base_configurations: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_configurations.KnowledgeBaseConfigurations"
    ]
    """<p>An array of configurations, each of which applies to a knowledge base attached to the agent.</p>"""
    conversation_history: NotRequired[
        "capo_bedrock_agent_runtime.types.conversation_history.ConversationHistory"
    ]
    """<p>The state's conversation history.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionState) -> dict:
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
    if "knowledge_base_configurations" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_configurations

        out["knowledgeBaseConfigurations"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_configurations.serialize_json(
                value["knowledge_base_configurations"]
            )
        )
    if "conversation_history" in value:
        import capo_bedrock_agent_runtime.types.conversation_history

        out["conversationHistory"] = (
            capo_bedrock_agent_runtime.types.conversation_history.serialize_json(
                value["conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionState:
    out: SessionState = {}  # type: ignore[typeddict-item]
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
    if data.get("knowledgeBaseConfigurations") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_configurations

        out["knowledge_base_configurations"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_configurations.deserialize_json(
                data["knowledgeBaseConfigurations"]
            )
        )
    if data.get("conversationHistory") is not None:
        import capo_bedrock_agent_runtime.types.conversation_history

        out["conversation_history"] = (
            capo_bedrock_agent_runtime.types.conversation_history.deserialize_json(
                data["conversationHistory"]
            )
        )
    return out
