"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContextEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration
    import capo_bedrock_agent.types.context_enrichment_type


class ContextEnrichmentConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.context_enrichment_type.ContextEnrichmentType"
    """<p>The method used for context enrichment. It must be Amazon Bedrock foundation models.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.BedrockFoundationModelContextEnrichmentConfiguration"
    ]
    """<p>The configuration of the Amazon Bedrock foundation model used for context enrichment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextEnrichmentConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.context_enrichment_type

    out["type"] = capo_bedrock_agent.types.context_enrichment_type.serialize_json(
        value["type"]
    )
    if "bedrock_foundation_model_configuration" in value:
        import capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration

        out["bedrockFoundationModelConfiguration"] = (
            capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContextEnrichmentConfiguration:
    out: ContextEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.context_enrichment_type

        out["type"] = capo_bedrock_agent.types.context_enrichment_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.context_enrichment_type.ContextEnrichmentType", ""
        )
    if data.get("bedrockFoundationModelConfiguration") is not None:
        import capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration

        out["bedrock_foundation_model_configuration"] = (
            capo_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    return out
