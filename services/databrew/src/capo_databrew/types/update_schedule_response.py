"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.schedule_name


class UpdateScheduleResponse(TypedDict, closed=True):
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduleResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateScheduleResponse:
    out: UpdateScheduleResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
