"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockFoundationModelContextEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_model_arn
    import capo_bedrock_agent.types.enrichment_strategy_configuration


class BedrockFoundationModelContextEnrichmentConfiguration(TypedDict, closed=True):
    enrichment_strategy_configuration: "capo_bedrock_agent.types.enrichment_strategy_configuration.EnrichmentStrategyConfiguration"
    """<p>The enrichment stategy used to provide additional context. For example, Neptune GraphRAG uses Amazon Bedrock foundation models to perform chunk entity extraction.</p>"""
    model_arn: "capo_bedrock_agent.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelContextEnrichmentConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enrichment_strategy_configuration

    out["enrichmentStrategyConfiguration"] = (
        capo_bedrock_agent.types.enrichment_strategy_configuration.serialize_json(
            value["enrichment_strategy_configuration"]
        )
    )
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(
    data: dict,
) -> BedrockFoundationModelContextEnrichmentConfiguration:
    out: BedrockFoundationModelContextEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enrichmentStrategyConfiguration") is not None:
        import capo_bedrock_agent.types.enrichment_strategy_configuration

        out["enrichment_strategy_configuration"] = (
            capo_bedrock_agent.types.enrichment_strategy_configuration.deserialize_json(
                data["enrichmentStrategyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "BedrockFoundationModelContextEnrichmentConfiguration.enrichment_strategy_configuration required"
        )
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    return out
