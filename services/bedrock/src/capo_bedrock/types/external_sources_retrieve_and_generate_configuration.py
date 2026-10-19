"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSourcesRetrieveAndGenerateConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_arn
    import capo_bedrock.types.external_sources
    import capo_bedrock.types.external_sources_generation_configuration


class ExternalSourcesRetrieveAndGenerateConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a> used to generate responses. </p>"""
    sources: "capo_bedrock.types.external_sources.ExternalSources"
    """<p>The document for the external source wrapper object in the <code>retrieveAndGenerate</code> function.</p>"""
    generation_configuration: NotRequired[
        "capo_bedrock.types.external_sources_generation_configuration.ExternalSourcesGenerationConfiguration"
    ]
    """<p>Contains configurations details for response generation based on retrieved text chunks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourcesRetrieveAndGenerateConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    import capo_bedrock.types.external_sources

    out["sources"] = capo_bedrock.types.external_sources.serialize_json(
        value["sources"]
    )
    if "generation_configuration" in value:
        import capo_bedrock.types.external_sources_generation_configuration

        out["generationConfiguration"] = (
            capo_bedrock.types.external_sources_generation_configuration.serialize_json(
                value["generation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalSourcesRetrieveAndGenerateConfiguration:
    out: ExternalSourcesRetrieveAndGenerateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("sources") is not None:
        import capo_bedrock.types.external_sources

        out["sources"] = capo_bedrock.types.external_sources.deserialize_json(
            data["sources"]
        )
    else:
        out["sources"] = []
    if data.get("generationConfiguration") is not None:
        import capo_bedrock.types.external_sources_generation_configuration

        out["generation_configuration"] = (
            capo_bedrock.types.external_sources_generation_configuration.deserialize_json(
                data["generationConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: ExternalSourcesRetrieveAndGenerateConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sources" in value:
        import capo_bedrock.types.external_sources

        out["sources"] = capo_bedrock.types.external_sources.redact_sensitive(
            value["sources"]
        )
    if "generation_configuration" in value:
        import capo_bedrock.types.external_sources_generation_configuration

        out["generation_configuration"] = (
            capo_bedrock.types.external_sources_generation_configuration.redact_sensitive(
                value["generation_configuration"]
            )
        )
    return out
