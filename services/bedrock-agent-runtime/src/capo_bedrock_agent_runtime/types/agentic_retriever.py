"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetriever``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retriever_configuration


class AgenticRetriever(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the retriever's purpose.</p>"""
    configuration: "capo_bedrock_agent_runtime.types.retriever_configuration.RetrieverConfiguration"
    """<p>The configuration for this retriever.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetriever) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent_runtime.types.retriever_configuration

    out["configuration"] = (
        capo_bedrock_agent_runtime.types.retriever_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgenticRetriever:
    out: AgenticRetriever = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_bedrock_agent_runtime.types.retriever_configuration

        out["configuration"] = (
            capo_bedrock_agent_runtime.types.retriever_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: AgenticRetriever) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_bedrock_agent_runtime.types.retriever_configuration

        out["configuration"] = (
            capo_bedrock_agent_runtime.types.retriever_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
