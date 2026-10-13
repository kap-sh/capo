"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.concatenation_source_type
    import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration


class ConcatenationSource(TypedDict, closed=True):
    type: "capo_chime_sdk_media_pipelines.types.concatenation_source_type.ConcatenationSourceType"
    """<p>The type of concatenation source in a configuration object.</p>"""
    media_capture_pipeline_source_configuration: "capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.MediaCapturePipelineSourceConfiguration"
    """<p>The concatenation settings for the media pipeline in a configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSource) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.concatenation_source_type

    out["Type"] = (
        capo_chime_sdk_media_pipelines.types.concatenation_source_type.serialize_json(
            value["type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration

    out["MediaCapturePipelineSourceConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.serialize_json(
            value["media_capture_pipeline_source_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConcatenationSource:
    out: ConcatenationSource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_chime_sdk_media_pipelines.types.concatenation_source_type

        out["type"] = (
            capo_chime_sdk_media_pipelines.types.concatenation_source_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ConcatenationSource.type required")
    if data.get("MediaCapturePipelineSourceConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration

        out["media_capture_pipeline_source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.deserialize_json(
                data["MediaCapturePipelineSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConcatenationSource.media_capture_pipeline_source_configuration required"
        )
    return out


def redact_sensitive(value: ConcatenationSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_capture_pipeline_source_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration

        out["media_capture_pipeline_source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.redact_sensitive(
                value["media_capture_pipeline_source_configuration"]
            )
        )
    return out
