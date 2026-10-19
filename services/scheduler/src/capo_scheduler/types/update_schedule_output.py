"""Generated from Smithy shape ``com.amazonaws.scheduler#UpdateScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.schedule_arn


class UpdateScheduleOutput(TypedDict, closed=True):
    schedule_arn: "capo_scheduler.types.schedule_arn.ScheduleArn"
    """<p>The Amazon Resource Name (ARN) of the schedule that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduleOutput) -> dict:
    out: dict = {}
    out["ScheduleArn"] = value["schedule_arn"]
    return out


def deserialize_json(data: dict) -> UpdateScheduleOutput:
    out: UpdateScheduleOutput = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleArn") is not None:
        out["schedule_arn"] = data["ScheduleArn"]
    else:
        out["schedule_arn"] = ""
    return out
