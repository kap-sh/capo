"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDomainsForPackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token
    import capo_opensearch.types.package_id


class ListDomainsForPackageRequest(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>The unique identifier of the package for which to list associated domains.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListDomainsForPackage</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListDomainsForPackage</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsForPackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsForPackageRequest:
    out: ListDomainsForPackageRequest = {}  # type: ignore[typeddict-item]
    return out
