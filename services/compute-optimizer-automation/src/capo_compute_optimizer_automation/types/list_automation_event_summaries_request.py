"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_filter_list
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventSummariesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
    ]
    """<p> The filters to apply to the list of automation event summaries. </p>"""
    start_date_inclusive: NotRequired["str"]
    """<p>The start date for filtering automation event summaries, inclusive. Events created on or after this date will be included.</p>"""
    end_date_exclusive: NotRequired["str"]
    """<p>The end date for filtering automation event summaries, exclusive. Events created before this date will be included.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of automation event summaries to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventSummariesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "start_date_inclusive" in value:
        out["startDateInclusive"] = value["start_date_inclusive"]
    if "end_date_exclusive" in value:
        out["endDateExclusive"] = value["end_date_exclusive"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventSummariesRequest:
    out: ListAutomationEventSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("startDateInclusive") is not None:
        out["start_date_inclusive"] = data["startDateInclusive"]
    if data.get("endDateExclusive") is not None:
        out["end_date_exclusive"] = data["endDateExclusive"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationEventSummariesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.serialize_cbor(
                value["filters"]
            )
        )
    if "start_date_inclusive" in value:
        out["startDateInclusive"] = value["start_date_inclusive"]
    if "end_date_exclusive" in value:
        out["endDateExclusive"] = value["end_date_exclusive"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationEventSummariesRequest:
    out: ListAutomationEventSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("startDateInclusive") is not None:
        out["start_date_inclusive"] = data["startDateInclusive"]
    if data.get("endDateExclusive") is not None:
        out["end_date_exclusive"] = data["endDateExclusive"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
