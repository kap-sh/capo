"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListPackagesForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class ListPackagesForDomainRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the domain for which you want to list associated packages.</p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p>Limits results to a maximum number of packages.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesForDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesForDomainRequest:
    out: ListPackagesForDomainRequest = {}  # type: ignore[typeddict-item]
    return out
