"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ManagedSearchRerankingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration
    import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type


class ManagedSearchRerankingConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type.ManagedSearchRerankingConfigurationType"
    """<p>The type of reranking configuration.</p>"""
    bedrock_reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration.ManagedSearchBedrockRerankingConfiguration"
    ]
    """<p>The Bedrock reranking model configuration for managed search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSearchRerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration

        out["bedrockRerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration.serialize_json(
                value["bedrock_reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedSearchRerankingConfiguration:
    out: ManagedSearchRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.managed_search_reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ManagedSearchRerankingConfiguration.type required")
    if data.get("bedrockRerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ManagedSearchRerankingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bedrock_reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_configuration.redact_sensitive(
                value["bedrock_reranking_configuration"]
            )
        )
    return out
