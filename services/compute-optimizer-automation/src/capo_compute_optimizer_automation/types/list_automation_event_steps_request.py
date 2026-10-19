"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.event_id
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventStepsRequest(TypedDict, closed=True):
    event_id: "capo_compute_optimizer_automation.types.event_id.EventId"
    """<p> The ID of the automation event. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of automation event steps to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventStepsRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventStepsRequest:
    out: ListAutomationEventStepsRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
