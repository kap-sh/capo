"""Generated from Smithy shape ``com.amazonaws.scheduler#ListSchedulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.next_token
    import capo_scheduler.types.schedule_list


class ListSchedulesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_scheduler.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If the value is null, there are no more results.</p>"""
    schedules: "capo_scheduler.types.schedule_list.ScheduleList"
    """<p>The schedules that match the specified criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_scheduler.types.schedule_list

    out["Schedules"] = capo_scheduler.types.schedule_list.serialize_json(
        value["schedules"]
    )
    return out


def deserialize_json(data: dict) -> ListSchedulesOutput:
    out: ListSchedulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Schedules") is not None:
        import capo_scheduler.types.schedule_list

        out["schedules"] = capo_scheduler.types.schedule_list.deserialize_json(
            data["Schedules"]
        )
    else:
        out["schedules"] = []
    return out
