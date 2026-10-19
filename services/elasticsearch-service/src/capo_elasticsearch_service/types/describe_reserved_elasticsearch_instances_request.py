"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeReservedElasticsearchInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class DescribeReservedElasticsearchInstancesRequest(TypedDict, closed=True):
    reserved_elasticsearch_instance_id: NotRequired[
        "capo_elasticsearch_service.types.guid.GUID"
    ]
    """<p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.</p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservedElasticsearchInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReservedElasticsearchInstancesRequest:
    out: DescribeReservedElasticsearchInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
