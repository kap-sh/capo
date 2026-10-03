"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_id
    import capo_bedrock_agent_runtime.types.agent_id
    import capo_bedrock_agent_runtime.types.aws_resource_arn
    import capo_bedrock_agent_runtime.types.bedrock_model_configurations
    import capo_bedrock_agent_runtime.types.input_text
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.prompt_creation_configurations
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.session_state
    import capo_bedrock_agent_runtime.types.streaming_configurations


class InvokeAgentRequest(TypedDict, closed=True):
    session_state: NotRequired[
        "capo_bedrock_agent_runtime.types.session_state.SessionState"
    ]
    """<p>Contains parameters that specify various attributes of the session. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId"
    """<p>The unique identifier of the agent to use.</p>"""
    agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId"
    """<p>The alias of the agent to use.</p>"""
    session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The unique identifier of the session. Use the same value across requests to continue the same conversation.</p>"""
    end_session: NotRequired["bool"]
    """<p>Specifies whether to end the session with the agent or not.</p>"""
    enable_trace: NotRequired["bool"]
    """<p>Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p>"""
    input_text: NotRequired["capo_bedrock_agent_runtime.types.input_text.InputText"]
    """<p>The prompt text to send the agent.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    memory_id: NotRequired["capo_bedrock_agent_runtime.types.memory_id.MemoryId"]
    """<p>The unique identifier of the agent memory.</p>"""
    bedrock_model_configurations: NotRequired[
        "capo_bedrock_agent_runtime.types.bedrock_model_configurations.BedrockModelConfigurations"
    ]
    """<p>Model performance settings for the request.</p>"""
    streaming_configurations: NotRequired[
        "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
    ]
    """<p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>"""
    prompt_creation_configurations: NotRequired[
        "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
    ]
    """<p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>"""
    source_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.aws_resource_arn.AWSResourceARN"
    ]
    """<p>The ARN of the resource making the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAgentRequest) -> dict:
    out: dict = {}
    if "session_state" in value:
        import capo_bedrock_agent_runtime.types.session_state

        out["sessionState"] = (
            capo_bedrock_agent_runtime.types.session_state.serialize_json(
                value["session_state"]
            )
        )
    if "end_session" in value:
        out["endSession"] = value["end_session"]
    if "enable_trace" in value:
        out["enableTrace"] = value["enable_trace"]
    if "input_text" in value:
        out["inputText"] = value["input_text"]
    if "memory_id" in value:
        out["memoryId"] = value["memory_id"]
    if "bedrock_model_configurations" in value:
        import capo_bedrock_agent_runtime.types.bedrock_model_configurations

        out["bedrockModelConfigurations"] = (
            capo_bedrock_agent_runtime.types.bedrock_model_configurations.serialize_json(
                value["bedrock_model_configurations"]
            )
        )
    if "streaming_configurations" in value:
        import capo_bedrock_agent_runtime.types.streaming_configurations

        out["streamingConfigurations"] = (
            capo_bedrock_agent_runtime.types.streaming_configurations.serialize_json(
                value["streaming_configurations"]
            )
        )
    if "prompt_creation_configurations" in value:
        import capo_bedrock_agent_runtime.types.prompt_creation_configurations

        out["promptCreationConfigurations"] = (
            capo_bedrock_agent_runtime.types.prompt_creation_configurations.serialize_json(
                value["prompt_creation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvokeAgentRequest:
    out: InvokeAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionState") is not None:
        import capo_bedrock_agent_runtime.types.session_state

        out["session_state"] = (
            capo_bedrock_agent_runtime.types.session_state.deserialize_json(
                data["sessionState"]
            )
        )
    if data.get("endSession") is not None:
        out["end_session"] = data["endSession"]
    if data.get("enableTrace") is not None:
        out["enable_trace"] = data["enableTrace"]
    if data.get("inputText") is not None:
        out["input_text"] = data["inputText"]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    if data.get("bedrockModelConfigurations") is not None:
        import capo_bedrock_agent_runtime.types.bedrock_model_configurations

        out["bedrock_model_configurations"] = (
            capo_bedrock_agent_runtime.types.bedrock_model_configurations.deserialize_json(
                data["bedrockModelConfigurations"]
            )
        )
    if data.get("streamingConfigurations") is not None:
        import capo_bedrock_agent_runtime.types.streaming_configurations

        out["streaming_configurations"] = (
            capo_bedrock_agent_runtime.types.streaming_configurations.deserialize_json(
                data["streamingConfigurations"]
            )
        )
    if data.get("promptCreationConfigurations") is not None:
        import capo_bedrock_agent_runtime.types.prompt_creation_configurations

        out["prompt_creation_configurations"] = (
            capo_bedrock_agent_runtime.types.prompt_creation_configurations.deserialize_json(
                data["promptCreationConfigurations"]
            )
        )
    return out
