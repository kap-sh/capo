"""Generated from Smithy shape ``com.amazonaws.scheduler#CreateScheduleGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.schedule_group_arn


class CreateScheduleGroupOutput(TypedDict, closed=True):
    schedule_group_arn: "capo_scheduler.types.schedule_group_arn.ScheduleGroupArn"
    """<p>The Amazon Resource Name (ARN) of the schedule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleGroupOutput) -> dict:
    out: dict = {}
    out["ScheduleGroupArn"] = value["schedule_group_arn"]
    return out


def deserialize_json(data: dict) -> CreateScheduleGroupOutput:
    out: CreateScheduleGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleGroupArn") is not None:
        out["schedule_group_arn"] = data["ScheduleGroupArn"]
    else:
        out["schedule_group_arn"] = ""
    return out
