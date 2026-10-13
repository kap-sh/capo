"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryRetrieveDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content


class AgenticRetrieveMemoryRetrieveDetails(TypedDict, closed=True):
    input_query: "capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.AgenticRetrieveMessageContent"
    """<p>The query that the agent composed.</p>"""
    memory_id: "str"
    """<p>The identifier of the AgentCore Memory resource retrieved from.</p>"""
    namespace: NotRequired["str"]
    """<p>The namespace prefix retrieved from, as supplied in the request. This field is present when the request specified namespace.</p>"""
    namespace_path: NotRequired["str"]
    """<p>The parent namespace retrieved from hierarchically, as supplied in the request. This field is present when the request specified namespacePath.</p>"""
    strategy_id: NotRequired["str"]
    """<p>The extraction strategy that restricted retrieval, if the request specified one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryRetrieveDetails) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

    out["inputQuery"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.serialize_json(
            value["input_query"]
        )
    )
    out["memoryId"] = value["memory_id"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "namespace_path" in value:
        out["namespacePath"] = value["namespace_path"]
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMemoryRetrieveDetails:
    out: AgenticRetrieveMemoryRetrieveDetails = {}  # type: ignore[typeddict-item]
    if data.get("inputQuery") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

        out["input_query"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.deserialize_json(
                data["inputQuery"]
            )
        )
    else:
        raise DeserializationError(
            "AgenticRetrieveMemoryRetrieveDetails.input_query required"
        )
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        raise DeserializationError(
            "AgenticRetrieveMemoryRetrieveDetails.memory_id required"
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("namespacePath") is not None:
        out["namespace_path"] = data["namespacePath"]
    if data.get("strategyId") is not None:
        out["strategy_id"] = data["strategyId"]
    return out


def redact_sensitive(value: AgenticRetrieveMemoryRetrieveDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_query" in value:
        out["input_query"] = "*** Sensitive Data Redacted ***"
    return out
