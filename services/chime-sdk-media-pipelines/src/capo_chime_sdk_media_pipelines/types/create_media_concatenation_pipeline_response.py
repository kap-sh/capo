"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaConcatenationPipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline


class CreateMediaConcatenationPipelineResponse(TypedDict, closed=True):
    media_concatenation_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.MediaConcatenationPipeline"
    ]
    """<p>A media concatenation pipeline object, the ID, source type, <code>MediaPipelineARN</code>, and sink of a media concatenation pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaConcatenationPipelineResponse) -> dict:
    out: dict = {}
    if "media_concatenation_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["MediaConcatenationPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.serialize_json(
                value["media_concatenation_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMediaConcatenationPipelineResponse:
    out: CreateMediaConcatenationPipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaConcatenationPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.deserialize_json(
                data["MediaConcatenationPipeline"]
            )
        )
    return out


def redact_sensitive(value: CreateMediaConcatenationPipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_concatenation_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.redact_sensitive(
                value["media_concatenation_pipeline"]
            )
        )
    return out
