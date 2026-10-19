"""Generated from Smithy shape ``com.amazonaws.scheduler#ListScheduleGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.next_token
    import capo_scheduler.types.schedule_group_list


class ListScheduleGroupsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_scheduler.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If the value is null, there are no more results.</p>"""
    schedule_groups: "capo_scheduler.types.schedule_group_list.ScheduleGroupList"
    """<p>The schedule groups that match the specified criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduleGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_scheduler.types.schedule_group_list

    out["ScheduleGroups"] = capo_scheduler.types.schedule_group_list.serialize_json(
        value["schedule_groups"]
    )
    return out


def deserialize_json(data: dict) -> ListScheduleGroupsOutput:
    out: ListScheduleGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScheduleGroups") is not None:
        import capo_scheduler.types.schedule_group_list

        out["schedule_groups"] = (
            capo_scheduler.types.schedule_group_list.deserialize_json(
                data["ScheduleGroups"]
            )
        )
    else:
        out["schedule_groups"] = []
    return out
