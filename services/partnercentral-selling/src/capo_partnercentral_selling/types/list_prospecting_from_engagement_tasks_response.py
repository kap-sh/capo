"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListProspectingFromEngagementTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.prospecting_task_summary_list


class ListProspectingFromEngagementTasksResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next page of results. If this field is present, pass its value as <code>NextToken</code> in the next call. If absent or empty, there are no further pages.</p>"""
    task_summaries: "capo_partnercentral_selling.types.prospecting_task_summary_list.ProspectingTaskSummaryList"
    """<p>Prospecting task summaries matching the specified filters. Each summary includes the task identifier, name, status counters, and timing information. If no tasks match the filter criteria, the list is empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProspectingFromEngagementTasksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_partnercentral_selling.types.prospecting_task_summary_list

    out["TaskSummaries"] = (
        capo_partnercentral_selling.types.prospecting_task_summary_list.serialize_aws_json_1_0(
            value["task_summaries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProspectingFromEngagementTasksResponse:
    out: ListProspectingFromEngagementTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TaskSummaries") is not None:
        import capo_partnercentral_selling.types.prospecting_task_summary_list

        out["task_summaries"] = (
            capo_partnercentral_selling.types.prospecting_task_summary_list.deserialize_aws_json_1_0(
                data["TaskSummaries"]
            )
        )
    else:
        out["task_summaries"] = []
    return out
