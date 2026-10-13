"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaStreamPipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_stream_pipeline


class CreateMediaStreamPipelineResponse(TypedDict, closed=True):
    media_stream_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_stream_pipeline.MediaStreamPipeline"
    ]
    """<p>The requested media pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaStreamPipelineResponse) -> dict:
    out: dict = {}
    if "media_stream_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["MediaStreamPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.serialize_json(
                value["media_stream_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMediaStreamPipelineResponse:
    out: CreateMediaStreamPipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaStreamPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["media_stream_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.deserialize_json(
                data["MediaStreamPipeline"]
            )
        )
    return out


def redact_sensitive(value: CreateMediaStreamPipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_stream_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["media_stream_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.redact_sensitive(
                value["media_stream_pipeline"]
            )
        )
    return out
