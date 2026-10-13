"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_allowed_tools
    import capo_bedrock_agentcore.types.harness_arn
    import capo_bedrock_agentcore.types.harness_endpoint_name
    import capo_bedrock_agentcore.types.harness_messages
    import capo_bedrock_agentcore.types.harness_model_configuration
    import capo_bedrock_agentcore.types.harness_skills
    import capo_bedrock_agentcore.types.harness_system_prompt
    import capo_bedrock_agentcore.types.harness_tools
    import capo_bedrock_agentcore.types.session_id


class InvokeHarnessRequest(TypedDict, closed=True):
    harness_arn: "capo_bedrock_agentcore.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness to invoke.</p>"""
    qualifier: NotRequired[
        "capo_bedrock_agentcore.types.harness_endpoint_name.HarnessEndpointName"
    ]
    """<p>The endpoint name to invoke. If omitted, the DEFAULT endpoint is used.</p>"""
    runtime_session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The session ID for the invocation. Use the same session ID across requests to continue a conversation.</p>"""
    runtime_user_id: NotRequired["str"]
    """<p>An identifier for the end user making the request. This value is passed through to the runtime container.</p>"""
    trace_parent: NotRequired["str"]
    """<p>W3C trace context parent header containing version, trace ID, parent span ID, and trace flags.</p>"""
    trace_state: NotRequired["str"]
    """<p>W3C trace context state header for vendor-specific trace information.</p>"""
    trace_id: NotRequired["str"]
    """<p>Trace ID for maintaining observability through the operation.</p>"""
    baggage: NotRequired["str"]
    """<p>W3C Baggage header for user-defined context propagation. Format: key1=value1,key2=value2</p>"""
    messages: "capo_bedrock_agentcore.types.harness_messages.HarnessMessages"
    """<p>The messages to send to the agent.</p>"""
    model: NotRequired[
        "capo_bedrock_agentcore.types.harness_model_configuration.HarnessModelConfiguration"
    ]
    """<p>The model configuration to use for this invocation. If specified, overrides the harness default.</p>"""
    system_prompt: NotRequired[
        "capo_bedrock_agentcore.types.harness_system_prompt.HarnessSystemPrompt"
    ]
    """<p>The system prompt to use for this invocation. If specified, overrides the harness default.</p>"""
    tools: NotRequired["capo_bedrock_agentcore.types.harness_tools.HarnessTools"]
    """<p>The tools available to the agent for this invocation. If specified, overrides the harness default.</p>"""
    skills: NotRequired["capo_bedrock_agentcore.types.harness_skills.HarnessSkills"]
    """<p>The skills available to the agent for this invocation. If specified, overrides the harness default.</p>"""
    allowed_tools: NotRequired[
        "capo_bedrock_agentcore.types.harness_allowed_tools.HarnessAllowedTools"
    ]
    """<p>The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.</p>"""
    actor_id: NotRequired["str"]
    """<p>The actor ID for memory operations. Overrides the actor ID configured on the harness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeHarnessRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.harness_messages

    out["messages"] = capo_bedrock_agentcore.types.harness_messages.serialize_json(
        value["messages"]
    )
    if "model" in value:
        import capo_bedrock_agentcore.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore.types.harness_model_configuration.serialize_json(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import capo_bedrock_agentcore.types.harness_system_prompt

        out["systemPrompt"] = (
            capo_bedrock_agentcore.types.harness_system_prompt.serialize_json(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import capo_bedrock_agentcore.types.harness_tools

        out["tools"] = capo_bedrock_agentcore.types.harness_tools.serialize_json(
            value["tools"]
        )
    if "skills" in value:
        import capo_bedrock_agentcore.types.harness_skills

        out["skills"] = capo_bedrock_agentcore.types.harness_skills.serialize_json(
            value["skills"]
        )
    if "allowed_tools" in value:
        import capo_bedrock_agentcore.types.harness_allowed_tools

        out["allowedTools"] = (
            capo_bedrock_agentcore.types.harness_allowed_tools.serialize_json(
                value["allowed_tools"]
            )
        )
    if "max_iterations" in value:
        out["maxIterations"] = value["max_iterations"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    return out


def deserialize_json(data: dict) -> InvokeHarnessRequest:
    out: InvokeHarnessRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_agentcore.types.harness_messages

        out["messages"] = (
            capo_bedrock_agentcore.types.harness_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("InvokeHarnessRequest.messages required")
    if data.get("model") is not None:
        import capo_bedrock_agentcore.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    if data.get("systemPrompt") is not None:
        import capo_bedrock_agentcore.types.harness_system_prompt

        out["system_prompt"] = (
            capo_bedrock_agentcore.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    if data.get("tools") is not None:
        import capo_bedrock_agentcore.types.harness_tools

        out["tools"] = capo_bedrock_agentcore.types.harness_tools.deserialize_json(
            data["tools"]
        )
    if data.get("skills") is not None:
        import capo_bedrock_agentcore.types.harness_skills

        out["skills"] = capo_bedrock_agentcore.types.harness_skills.deserialize_json(
            data["skills"]
        )
    if data.get("allowedTools") is not None:
        import capo_bedrock_agentcore.types.harness_allowed_tools

        out["allowed_tools"] = (
            capo_bedrock_agentcore.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    if data.get("maxIterations") is not None:
        out["max_iterations"] = data["maxIterations"]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    return out


def redact_sensitive(value: InvokeHarnessRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_bedrock_agentcore.types.harness_messages

        out["messages"] = (
            capo_bedrock_agentcore.types.harness_messages.redact_sensitive(
                value["messages"]
            )
        )
    if "model" in value:
        import capo_bedrock_agentcore.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore.types.harness_model_configuration.redact_sensitive(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import capo_bedrock_agentcore.types.harness_system_prompt

        out["system_prompt"] = (
            capo_bedrock_agentcore.types.harness_system_prompt.redact_sensitive(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import capo_bedrock_agentcore.types.harness_tools

        out["tools"] = capo_bedrock_agentcore.types.harness_tools.redact_sensitive(
            value["tools"]
        )
    return out
