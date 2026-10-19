"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_id


class ListTestRunEventsRequest(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the test run to list events for.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test run belongs to.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>Return events at or after this timestamp.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>Return events at or before this timestamp.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestRunEventsRequest:
    out: ListTestRunEventsRequest = {}  # type: ignore[typeddict-item]
    return out
