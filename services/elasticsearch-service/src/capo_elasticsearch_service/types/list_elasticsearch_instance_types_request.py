"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListElasticsearchInstanceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.elasticsearch_version_string
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class ListElasticsearchInstanceTypesRequest(TypedDict, closed=True):
    elasticsearch_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p>Version of Elasticsearch for which list of supported elasticsearch instance types are needed. </p>"""
    domain_name: NotRequired["capo_elasticsearch_service.types.domain_name.DomainName"]
    """<p>DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. </p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p> Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. </p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListElasticsearchInstanceTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListElasticsearchInstanceTypesRequest:
    out: ListElasticsearchInstanceTypesRequest = {}  # type: ignore[typeddict-item]
    return out
