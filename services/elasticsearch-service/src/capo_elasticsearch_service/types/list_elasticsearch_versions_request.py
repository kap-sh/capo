"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListElasticsearchVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class ListElasticsearchVersionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p> Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. </p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListElasticsearchVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListElasticsearchVersionsRequest:
    out: ListElasticsearchVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
