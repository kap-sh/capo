"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token


class ListTestsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service to list tests for.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTestsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestsRequest:
    out: ListTestsRequest = {}  # type: ignore[typeddict-item]
    return out
