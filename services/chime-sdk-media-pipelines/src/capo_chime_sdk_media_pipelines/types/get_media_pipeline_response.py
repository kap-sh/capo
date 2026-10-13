"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_pipeline


class GetMediaPipelineResponse(TypedDict, closed=True):
    media_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline.MediaPipeline"
    ]
    """<p>The media pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineResponse) -> dict:
    out: dict = {}
    if "media_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline

        out["MediaPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline.serialize_json(
                value["media_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaPipelineResponse:
    out: GetMediaPipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline

        out["media_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline.deserialize_json(
                data["MediaPipeline"]
            )
        )
    return out


def redact_sensitive(value: GetMediaPipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline

        out["media_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline.redact_sensitive(
                value["media_pipeline"]
            )
        )
    return out
