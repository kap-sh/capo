"""Generated from Smithy shape ``com.amazonaws.databrew#ListSchedulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.next_token
    import capo_databrew.types.schedule_list


class ListSchedulesResponse(TypedDict, closed=True):
    schedules: "capo_databrew.types.schedule_list.ScheduleList"
    """<p>A list of schedules that are defined.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.schedule_list

    out["Schedules"] = capo_databrew.types.schedule_list.serialize_json(
        value["schedules"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchedulesResponse:
    out: ListSchedulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Schedules") is not None:
        import capo_databrew.types.schedule_list

        out["schedules"] = capo_databrew.types.schedule_list.deserialize_json(
            data["Schedules"]
        )
    else:
        out["schedules"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
