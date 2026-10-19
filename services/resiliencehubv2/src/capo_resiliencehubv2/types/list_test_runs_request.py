"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_id


class ListTestRunsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service to list test runs for.</p>"""
    test_id: NotRequired["capo_resiliencehubv2.types.test_id.TestId"]
    """<p>Filter test runs by test identifier.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestRunsRequest:
    out: ListTestRunsRequest = {}  # type: ignore[typeddict-item]
    return out
