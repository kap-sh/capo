"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataConfigurationForReranking``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.reranking_metadata_selection_mode
    import capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration


class MetadataConfigurationForReranking(TypedDict, closed=True):
    selection_mode: "capo_bedrock_agent.types.reranking_metadata_selection_mode.RerankingMetadataSelectionMode"
    """<p>The mode for selecting metadata fields for reranking.</p>"""
    selective_mode_configuration: NotRequired[
        "capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration.RerankingMetadataSelectiveModeConfiguration"
    ]
    """<p>The configuration for selective metadata field inclusion or exclusion during reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationForReranking) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.reranking_metadata_selection_mode

    out["selectionMode"] = (
        capo_bedrock_agent.types.reranking_metadata_selection_mode.serialize_json(
            value["selection_mode"]
        )
    )
    if "selective_mode_configuration" in value:
        import capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration

        out["selectiveModeConfiguration"] = (
            capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration.serialize_json(
                value["selective_mode_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationForReranking:
    out: MetadataConfigurationForReranking = {}  # type: ignore[typeddict-item]
    if data.get("selectionMode") is not None:
        import capo_bedrock_agent.types.reranking_metadata_selection_mode

        out["selection_mode"] = (
            capo_bedrock_agent.types.reranking_metadata_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        raise DeserializationError(
            "MetadataConfigurationForReranking.selection_mode required"
        )
    if data.get("selectiveModeConfiguration") is not None:
        import capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration.deserialize_json(
                data["selectiveModeConfiguration"]
            )
        )
    return out


def redact_sensitive(value: MetadataConfigurationForReranking) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "selective_mode_configuration" in value:
        import capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            capo_bedrock_agent.types.reranking_metadata_selective_mode_configuration.redact_sensitive(
                value["selective_mode_configuration"]
            )
        )
    return out
