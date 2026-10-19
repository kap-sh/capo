"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeReservedElasticsearchInstanceOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class DescribeReservedElasticsearchInstanceOfferingsRequest(TypedDict, closed=True):
    reserved_elasticsearch_instance_offering_id: NotRequired[
        "capo_elasticsearch_service.types.guid.GUID"
    ]
    """<p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeReservedElasticsearchInstanceOfferingsRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> DescribeReservedElasticsearchInstanceOfferingsRequest:
    out: DescribeReservedElasticsearchInstanceOfferingsRequest = {}  # type: ignore[typeddict-item]
    return out
