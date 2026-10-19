"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListTimelineEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.filter_list
    import capo_ssm_incidents.types.max_results
    import capo_ssm_incidents.types.next_token
    import capo_ssm_incidents.types.sort_order
    import capo_ssm_incidents.types.timeline_event_sort


class ListTimelineEventsInput(TypedDict, closed=True):
    incident_record_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    filters: NotRequired["capo_ssm_incidents.types.filter_list.FilterList"]
    """<p>Filters the timeline events based on the provided conditional values. You can filter timeline events with the following keys:</p> <ul> <li> <p> <code>eventReference</code> </p> </li> <li> <p> <code>eventTime</code> </p> </li> <li> <p> <code>eventType</code> </p> </li> </ul> <p>Note the following when deciding how to use Filters:</p> <ul> <li> <p>If you don't specify a Filter, the response includes all timeline events.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns timeline events that match all filters.</p> </li> <li> <p>If you specify a filter with more than one value, the response returns timeline events that match any of the values provided.</p> </li> </ul>"""
    sort_by: NotRequired[
        "capo_ssm_incidents.types.timeline_event_sort.TimelineEventSort"
    ]
    """<p>Sort timeline events by the specified key value pair.</p>"""
    sort_order: NotRequired["capo_ssm_incidents.types.sort_order.SortOrder"]
    """<p>Sorts the order of timeline events by the value specified in the <code>sortBy</code> field.</p>"""
    max_results: NotRequired["capo_ssm_incidents.types.max_results.MaxResults"]
    """<p>The maximum number of results per page.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimelineEventsInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    if "filters" in value:
        import capo_ssm_incidents.types.filter_list

        out["filters"] = capo_ssm_incidents.types.filter_list.serialize_json(
            value["filters"]
        )
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTimelineEventsInput:
    out: ListTimelineEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("incidentRecordArn") is not None:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        out["incident_record_arn"] = ""
    if data.get("filters") is not None:
        import capo_ssm_incidents.types.filter_list

        out["filters"] = capo_ssm_incidents.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
