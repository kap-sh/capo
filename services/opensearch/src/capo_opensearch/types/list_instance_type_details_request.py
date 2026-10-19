"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInstanceTypeDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.instance_type_string
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token
    import capo_opensearch.types.version_string


class ListInstanceTypeDetailsRequest(TypedDict, closed=True):
    engine_version: "capo_opensearch.types.version_string.VersionString"
    """<p>The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>"""
    domain_name: NotRequired["capo_opensearch.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListInstanceTypeDetails</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListInstanceTypeDetails</code> operations, which returns results in the next page.</p>"""
    retrieve_a_zs: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>An optional parameter that specifies the Availability Zones for the domain.</p>"""
    instance_type: NotRequired[
        "capo_opensearch.types.instance_type_string.InstanceTypeString"
    ]
    """<p>An optional parameter that lists information for a given instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceTypeDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInstanceTypeDetailsRequest:
    out: ListInstanceTypeDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
