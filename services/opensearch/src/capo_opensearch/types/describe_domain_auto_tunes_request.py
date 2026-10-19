"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainAutoTunesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class DescribeDomainAutoTunesRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain that you want Auto-Tune details about.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>DescribeDomainAutoTunes</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeDomainAutoTunes</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainAutoTunesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainAutoTunesRequest:
    out: DescribeDomainAutoTunesRequest = {}  # type: ignore[typeddict-item]
    return out
