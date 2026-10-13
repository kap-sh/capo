"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineKinesisVideoStreamPoolResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration


class GetMediaPipelineKinesisVideoStreamPoolResponse(TypedDict, closed=True):
    kinesis_video_stream_pool_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.KinesisVideoStreamPoolConfiguration"
    ]
    """<p>The video stream pool configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineKinesisVideoStreamPoolResponse) -> dict:
    out: dict = {}
    if "kinesis_video_stream_pool_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["KinesisVideoStreamPoolConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.serialize_json(
                value["kinesis_video_stream_pool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaPipelineKinesisVideoStreamPoolResponse:
    out: GetMediaPipelineKinesisVideoStreamPoolResponse = {}  # type: ignore[typeddict-item]
    if data.get("KinesisVideoStreamPoolConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["kinesis_video_stream_pool_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.deserialize_json(
                data["KinesisVideoStreamPoolConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: GetMediaPipelineKinesisVideoStreamPoolResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kinesis_video_stream_pool_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["kinesis_video_stream_pool_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.redact_sensitive(
                value["kinesis_video_stream_pool_configuration"]
            )
        )
    return out
