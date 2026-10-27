"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListScheduleActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.schedule_action_list


class ListScheduleActionsResponse(TypedDict, closed=True):
    schedule_actions: (
        "capo_elementalinference.types.schedule_action_list.ScheduleActionList"
    )
    """<p>A list of the schedule actions on the feed.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the next batch of results. Elemental Inference returns it only when more results are available. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduleActionsResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.schedule_action_list

    out["scheduleActions"] = (
        capo_elementalinference.types.schedule_action_list.serialize_json(
            value["schedule_actions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScheduleActionsResponse:
    out: ListScheduleActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("scheduleActions") is not None:
        import capo_elementalinference.types.schedule_action_list

        out["schedule_actions"] = (
            capo_elementalinference.types.schedule_action_list.deserialize_json(
                data["scheduleActions"]
            )
        )
    else:
        out["schedule_actions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
