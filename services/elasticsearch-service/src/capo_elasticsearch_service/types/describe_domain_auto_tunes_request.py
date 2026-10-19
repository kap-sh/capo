"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeDomainAutoTunesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class DescribeDomainAutoTunesRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>Specifies the domain name for which you want Auto-Tune action details.</p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainAutoTunesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainAutoTunesRequest:
    out: DescribeDomainAutoTunesRequest = {}  # type: ignore[typeddict-item]
    return out
