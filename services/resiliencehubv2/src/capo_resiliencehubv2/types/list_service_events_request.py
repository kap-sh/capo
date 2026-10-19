"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.service_event_type_list


class ListServiceEventsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    event_types: NotRequired[
        "capo_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
    ]
    """<p>The type of events to include in the results.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time for filtering events.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for filtering events.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceEventsRequest:
    out: ListServiceEventsRequest = {}  # type: ignore[typeddict-item]
    return out
