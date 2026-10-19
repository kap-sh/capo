"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_source_type


class ListTestSourcesRequest(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test to list sources for.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    type: NotRequired["capo_resiliencehubv2.types.test_source_type.TestSourceType"]
    """<p>Filter sources by type.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestSourcesRequest:
    out: ListTestSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
