"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestRunSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_source_type


class ListTestRunSourcesRequest(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the test run to list sources for.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test run belongs to.</p>"""
    type: NotRequired[
        "capo_resiliencehubv2.types.test_run_source_type.TestRunSourceType"
    ]
    """<p>Filter sources by type.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRunSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestRunSourcesRequest:
    out: ListTestRunSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
