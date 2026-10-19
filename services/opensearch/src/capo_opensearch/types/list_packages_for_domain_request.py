"""Generated from Smithy shape ``com.amazonaws.opensearch#ListPackagesForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class ListPackagesForDomainRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain for which you want to list associated packages.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListPackagesForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPackagesForDomain</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesForDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesForDomainRequest:
    out: ListPackagesForDomainRequest = {}  # type: ignore[typeddict-item]
    return out
