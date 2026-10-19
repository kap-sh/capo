"""Generated from Smithy shape ``com.amazonaws.bedrock#MetadataConfigurationForReranking``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.reranking_metadata_selection_mode
    import capo_bedrock.types.reranking_metadata_selective_mode_configuration


class MetadataConfigurationForReranking(TypedDict, closed=True):
    selection_mode: "capo_bedrock.types.reranking_metadata_selection_mode.RerankingMetadataSelectionMode"
    """<p>The mode for selecting which metadata fields to include in the reranking process. Valid values are ALL (use all available metadata fields) or SELECTIVE (use only specified fields).</p>"""
    selective_mode_configuration: NotRequired[
        "capo_bedrock.types.reranking_metadata_selective_mode_configuration.RerankingMetadataSelectiveModeConfiguration"
    ]
    """<p>Configuration for selective mode, which allows you to explicitly include or exclude specific metadata fields during reranking. This is only used when selectionMode is set to SELECTIVE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationForReranking) -> dict:
    out: dict = {}
    import capo_bedrock.types.reranking_metadata_selection_mode

    out["selectionMode"] = (
        capo_bedrock.types.reranking_metadata_selection_mode.serialize_json(
            value["selection_mode"]
        )
    )
    if "selective_mode_configuration" in value:
        import capo_bedrock.types.reranking_metadata_selective_mode_configuration

        out["selectiveModeConfiguration"] = (
            capo_bedrock.types.reranking_metadata_selective_mode_configuration.serialize_json(
                value["selective_mode_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationForReranking:
    out: MetadataConfigurationForReranking = {}  # type: ignore[typeddict-item]
    if data.get("selectionMode") is not None:
        import capo_bedrock.types.reranking_metadata_selection_mode

        out["selection_mode"] = (
            capo_bedrock.types.reranking_metadata_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        import typing

        out["selection_mode"] = typing.cast(
            "capo_bedrock.types.reranking_metadata_selection_mode.RerankingMetadataSelectionMode",
            "",
        )
    if data.get("selectiveModeConfiguration") is not None:
        import capo_bedrock.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            capo_bedrock.types.reranking_metadata_selective_mode_configuration.deserialize_json(
                data["selectiveModeConfiguration"]
            )
        )
    return out


def redact_sensitive(value: MetadataConfigurationForReranking) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "selective_mode_configuration" in value:
        import capo_bedrock.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            capo_bedrock.types.reranking_metadata_selective_mode_configuration.redact_sensitive(
                value["selective_mode_configuration"]
            )
        )
    return out
