"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#RecorderConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.media_source_config
    import capo_kinesis_video.types.schedule_config


class RecorderConfig(TypedDict, closed=True):
    media_source_config: (
        "capo_kinesis_video.types.media_source_config.MediaSourceConfig"
    )
    """<p>The configuration details that consist of the credentials required (<code>MediaUriSecretArn</code> and <code>MediaUriType</code>) to access the media files streamed to the camera. </p>"""
    schedule_config: NotRequired[
        "capo_kinesis_video.types.schedule_config.ScheduleConfig"
    ]
    """<p>The configuration that consists of the <code>ScheduleExpression</code> and the <code>DurationInMinutes</code> details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the <code>ScheduleExpression</code> attribute is not provided, then the Edge Agent will always be set to recording mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecorderConfig) -> dict:
    out: dict = {}
    import capo_kinesis_video.types.media_source_config

    out["MediaSourceConfig"] = (
        capo_kinesis_video.types.media_source_config.serialize_json(
            value["media_source_config"]
        )
    )
    if "schedule_config" in value:
        import capo_kinesis_video.types.schedule_config

        out["ScheduleConfig"] = capo_kinesis_video.types.schedule_config.serialize_json(
            value["schedule_config"]
        )
    return out


def deserialize_json(data: dict) -> RecorderConfig:
    out: RecorderConfig = {}  # type: ignore[typeddict-item]
    if data.get("MediaSourceConfig") is not None:
        import capo_kinesis_video.types.media_source_config

        out["media_source_config"] = (
            capo_kinesis_video.types.media_source_config.deserialize_json(
                data["MediaSourceConfig"]
            )
        )
    else:
        raise DeserializationError("RecorderConfig.media_source_config required")
    if data.get("ScheduleConfig") is not None:
        import capo_kinesis_video.types.schedule_config

        out["schedule_config"] = (
            capo_kinesis_video.types.schedule_config.deserialize_json(
                data["ScheduleConfig"]
            )
        )
    return out


def redact_sensitive(value: RecorderConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_source_config" in value:
        import capo_kinesis_video.types.media_source_config

        out["media_source_config"] = (
            capo_kinesis_video.types.media_source_config.redact_sensitive(
                value["media_source_config"]
            )
        )
    return out
