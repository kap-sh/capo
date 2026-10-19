"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.schedule_name


class DeleteScheduleResponse(TypedDict, closed=True):
    name: "capo_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteScheduleResponse:
    out: DeleteScheduleResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
