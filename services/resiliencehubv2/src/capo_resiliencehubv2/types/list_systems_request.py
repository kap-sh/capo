"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListSystemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.ou_id


class ListSystemsRequest(TypedDict, closed=True):
    ou_id: NotRequired["capo_resiliencehubv2.types.ou_id.OuId"]
    """<p>Filter systems by organizational unit (OU) identifier.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSystemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSystemsRequest:
    out: ListSystemsRequest = {}  # type: ignore[typeddict-item]
    return out
