"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveRerankingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type


class AgenticRetrieveRerankingConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type.AgenticRetrieveRerankingConfigurationType"
    """<p>The type of reranking configuration.</p>"""
    bedrock_reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration.AgenticRetrieveBedrockRerankingConfiguration"
    ]
    """<p>The Bedrock reranking model configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveRerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration

        out["bedrockRerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration.serialize_json(
                value["bedrock_reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveRerankingConfiguration:
    out: AgenticRetrieveRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration_type.AgenticRetrieveRerankingConfigurationType",
            "",
        )
    if data.get("bedrockRerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    return out
