"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamPoolSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_id
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name


class KinesisVideoStreamPoolSummary(TypedDict, closed=True):
    pool_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name.KinesisVideoStreamPoolName"
    ]
    """<p>The name of the video stream pool.</p>"""
    pool_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_id.KinesisVideoStreamPoolId"
    ]
    """<p>The ID of the video stream pool.</p>"""
    pool_arn: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of the video stream pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamPoolSummary) -> dict:
    out: dict = {}
    if "pool_name" in value:
        out["PoolName"] = value["pool_name"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "pool_arn" in value:
        out["PoolArn"] = value["pool_arn"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamPoolSummary:
    out: KinesisVideoStreamPoolSummary = {}  # type: ignore[typeddict-item]
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("PoolArn") is not None:
        out["pool_arn"] = data["PoolArn"]
    return out


def redact_sensitive(value: KinesisVideoStreamPoolSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pool_arn" in value:
        out["pool_arn"] = "*** Sensitive Data Redacted ***"
    return out
