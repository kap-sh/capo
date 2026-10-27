"""Generated from Smithy shape ``com.amazonaws.ecr#ListReplicationBackfillsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.fifty_max_results
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id


class ListReplicationBackfillsRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry for which to list replication backfills. If you do not specify a registry, the default registry is assumed.</p>"""
    max_results: NotRequired["capo_ecr.types.fifty_max_results.FiftyMaxResults"]
    """<p>The maximum number of replication backfill results returned by <code>ListReplicationBackfills</code> in paginated output. When this parameter is used, <code>ListReplicationBackfills</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListReplicationBackfills</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 50. If this parameter is not used, then <code>ListReplicationBackfills</code> returns up to 25 results and a <code>nextToken</code> value, if applicable.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListReplicationBackfills</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReplicationBackfillsRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReplicationBackfillsRequest:
    out: ListReplicationBackfillsRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
