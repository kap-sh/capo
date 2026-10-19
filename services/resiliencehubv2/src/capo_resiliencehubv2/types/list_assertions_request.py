"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListAssertionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion_source
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token


class ListAssertionsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    source: NotRequired["capo_resiliencehubv2.types.assertion_source.AssertionSource"]
    """<p>Filter assertions by source type.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssertionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssertionsRequest:
    out: ListAssertionsRequest = {}  # type: ignore[typeddict-item]
    return out
