"""Generated from Smithy shape ``com.amazonaws.deadline#ListMeteredProductsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token


class ListMeteredProductsRequest(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID to include on the list of metered products.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMeteredProductsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMeteredProductsRequest:
    out: ListMeteredProductsRequest = {}  # type: ignore[typeddict-item]
    return out
