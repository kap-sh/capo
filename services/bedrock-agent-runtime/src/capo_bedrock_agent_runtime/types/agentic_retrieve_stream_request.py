"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveStreamRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_messages
    import capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrievers
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.user_context


class AgenticRetrieveStreamRequest(TypedDict, closed=True):
    messages: "capo_bedrock_agent_runtime.types.agentic_retrieve_messages.AgenticRetrieveMessages"
    """<p>The list of messages for the agentic retrieval conversation.</p>"""
    retrievers: "capo_bedrock_agent_runtime.types.agentic_retrievers.AgenticRetrievers"
    """<p>The list of retrievers to use for agentic retrieval.</p>"""
    agentic_retrieve_configuration: "capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.AgenticRetrieveConfiguration"
    """<p>Configuration settings for the agentic retrieval operation.</p>"""
    policy_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.AgenticRetrievePolicyConfiguration"
    ]
    """<p>Policy configuration for guardrails and content filtering.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>Opaque continuation token for paginated results.</p>"""
    user_context: NotRequired[
        "capo_bedrock_agent_runtime.types.user_context.UserContext"
    ]
    """<p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>"""
    memory_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.AgenticRetrieveMemoryConfiguration"
    ]
    """<p>The configuration for using an Amazon Bedrock AgentCore Memory resource with this retrieval.</p>"""
    generate_response: NotRequired["bool"]
    """<p>Whether to generate a response based on the retrieved results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveStreamRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_messages

    out["messages"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_messages.serialize_json(
            value["messages"]
        )
    )
    import capo_bedrock_agent_runtime.types.agentic_retrievers

    out["retrievers"] = (
        capo_bedrock_agent_runtime.types.agentic_retrievers.serialize_json(
            value["retrievers"]
        )
    )
    import capo_bedrock_agent_runtime.types.agentic_retrieve_configuration

    out["agenticRetrieveConfiguration"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.serialize_json(
            value["agentic_retrieve_configuration"]
        )
    )
    if "policy_configuration" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration

        out["policyConfiguration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.serialize_json(
                value["policy_configuration"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "user_context" in value:
        import capo_bedrock_agent_runtime.types.user_context

        out["userContext"] = (
            capo_bedrock_agent_runtime.types.user_context.serialize_json(
                value["user_context"]
            )
        )
    if "memory_configuration" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration

        out["memoryConfiguration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.serialize_json(
                value["memory_configuration"]
            )
        )
    if "generate_response" in value:
        out["generateResponse"] = value["generate_response"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveStreamRequest:
    out: AgenticRetrieveStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_messages

        out["messages"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveStreamRequest.messages required")
    if data.get("retrievers") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrievers

        out["retrievers"] = (
            capo_bedrock_agent_runtime.types.agentic_retrievers.deserialize_json(
                data["retrievers"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveStreamRequest.retrievers required")
    if data.get("agenticRetrieveConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_configuration

        out["agentic_retrieve_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.deserialize_json(
                data["agenticRetrieveConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AgenticRetrieveStreamRequest.agentic_retrieve_configuration required"
        )
    if data.get("policyConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration

        out["policy_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.deserialize_json(
                data["policyConfiguration"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("userContext") is not None:
        import capo_bedrock_agent_runtime.types.user_context

        out["user_context"] = (
            capo_bedrock_agent_runtime.types.user_context.deserialize_json(
                data["userContext"]
            )
        )
    if data.get("memoryConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration

        out["memory_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.deserialize_json(
                data["memoryConfiguration"]
            )
        )
    if data.get("generateResponse") is not None:
        out["generate_response"] = data["generateResponse"]
    return out


def redact_sensitive(value: AgenticRetrieveStreamRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_messages

        out["messages"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_messages.redact_sensitive(
                value["messages"]
            )
        )
    if "retrievers" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrievers

        out["retrievers"] = (
            capo_bedrock_agent_runtime.types.agentic_retrievers.redact_sensitive(
                value["retrievers"]
            )
        )
    if "user_context" in value:
        out["user_context"] = "*** Sensitive Data Redacted ***"
    return out
