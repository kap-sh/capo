"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ScheduleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.duration_in_seconds
    import capo_kinesis_video.types.schedule_expression


class ScheduleConfig(TypedDict, closed=True):
    schedule_expression: (
        "capo_kinesis_video.types.schedule_expression.ScheduleExpression"
    )
    """<p>The Quartz cron expression that takes care of scheduling jobs to record from the camera, or local media file, onto the Edge Agent. If the <code>ScheduleExpression</code> is not provided for the <code>RecorderConfig</code>, then the Edge Agent will always be set to recording mode.</p> <p>For more information about Quartz, refer to the <a href="https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html"> <i>Cron Trigger Tutorial</i> </a> page to understand the valid expressions and its use.</p>"""
    duration_in_seconds: (
        "capo_kinesis_video.types.duration_in_seconds.DurationInSeconds"
    )
    """<p>The total duration to record the media. If the <code>ScheduleExpression</code> attribute is provided, then the <code>DurationInSeconds</code> attribute should also be specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfig) -> dict:
    out: dict = {}
    out["ScheduleExpression"] = value["schedule_expression"]
    out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> ScheduleConfig:
    out: ScheduleConfig = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        raise DeserializationError("ScheduleConfig.schedule_expression required")
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError("ScheduleConfig.duration_in_seconds required")
    return out
