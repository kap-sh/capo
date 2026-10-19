"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_reranking_configuration
    import capo_bedrock_agent_runtime.types.reranking_configuration_type


class RerankingConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.reranking_configuration_type.RerankingConfigurationType"
    """<p>The type of reranker that the configurations apply to.</p>"""
    bedrock_reranking_configuration: "capo_bedrock_agent_runtime.types.bedrock_reranking_configuration.BedrockRerankingConfiguration"
    """<p>Contains configurations for an Amazon Bedrock reranker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.reranking_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_agent_runtime.types.bedrock_reranking_configuration

    out["bedrockRerankingConfiguration"] = (
        capo_bedrock_agent_runtime.types.bedrock_reranking_configuration.serialize_json(
            value["bedrock_reranking_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RerankingConfiguration:
    out: RerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.reranking_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.reranking_configuration_type.RerankingConfigurationType",
            "",
        )
    if data.get("bedrockRerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RerankingConfiguration.bedrock_reranking_configuration required"
        )
    return out
