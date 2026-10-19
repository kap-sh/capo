"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListPolicyEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.policy_event_type_list


class ListPolicyEventsRequest(TypedDict, closed=True):
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"
    event_types: NotRequired[
        "capo_resiliencehubv2.types.policy_event_type_list.PolicyEventTypeList"
    ]
    """<p>The type of events to include in the results.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time for filtering events.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for filtering events.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyEventsRequest:
    out: ListPolicyEventsRequest = {}  # type: ignore[typeddict-item]
    return out
