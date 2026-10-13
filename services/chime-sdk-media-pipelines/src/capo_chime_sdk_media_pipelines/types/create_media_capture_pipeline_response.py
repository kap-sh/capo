"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaCapturePipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_capture_pipeline


class CreateMediaCapturePipelineResponse(TypedDict, closed=True):
    media_capture_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_capture_pipeline.MediaCapturePipeline"
    ]
    """<p>A media pipeline object, the ID, source type, source ARN, sink type, and sink ARN of a media pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaCapturePipelineResponse) -> dict:
    out: dict = {}
    if "media_capture_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["MediaCapturePipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.serialize_json(
                value["media_capture_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMediaCapturePipelineResponse:
    out: CreateMediaCapturePipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaCapturePipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.deserialize_json(
                data["MediaCapturePipeline"]
            )
        )
    return out


def redact_sensitive(value: CreateMediaCapturePipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_capture_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.redact_sensitive(
                value["media_capture_pipeline"]
            )
        )
    return out
