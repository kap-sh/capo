"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDomainMaintenancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.maintenance_status
    import capo_opensearch.types.maintenance_type
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class ListDomainMaintenancesRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    action: NotRequired["capo_opensearch.types.maintenance_type.MaintenanceType"]
    """<p>The name of the action.</p>"""
    status: NotRequired["capo_opensearch.types.maintenance_status.MaintenanceStatus"]
    """<p>The status of the action.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListDomainMaintenances</code> operation returns a <code>nextToken</code>, include the returned <code>nextToken</code> in subsequent <code>ListDomainMaintenances</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainMaintenancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainMaintenancesRequest:
    out: ListDomainMaintenancesRequest = {}  # type: ignore[typeddict-item]
    return out
