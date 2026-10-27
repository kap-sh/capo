"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeReplicationBackfillResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.max_results
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_backfill_id
    import capo_ecr.types.replication_backfill_result_status


class DescribeReplicationBackfillResultsRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the replication backfill to describe. If you do not specify a registry, the default registry is assumed.</p>"""
    replication_backfill_id: (
        "capo_ecr.types.replication_backfill_id.ReplicationBackfillId"
    )
    """<p>The ID of the replication backfill to describe.</p>"""
    result_status_filter: NotRequired[
        "capo_ecr.types.replication_backfill_result_status.ReplicationBackfillResultStatus"
    ]
    """<p>The status used to filter the returned results. Each result has a status of <code>COMPLETE</code> or <code>FAILED</code>. If you omit this parameter, results with both statuses are returned.</p>"""
    max_results: NotRequired["capo_ecr.types.max_results.MaxResults"]
    """<p>The maximum number of replication backfill results returned by <code>DescribeReplicationBackfillResults</code> in paginated output. When this parameter is used, <code>DescribeReplicationBackfillResults</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeReplicationBackfillResults</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeReplicationBackfillResults</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeReplicationBackfillResults</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationBackfillResultsRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["replicationBackfillId"] = value["replication_backfill_id"]
    if "result_status_filter" in value:
        import capo_ecr.types.replication_backfill_result_status

        out["resultStatusFilter"] = (
            capo_ecr.types.replication_backfill_result_status.serialize_aws_json_1_1(
                value["result_status_filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationBackfillResultsRequest:
    out: DescribeReplicationBackfillResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("replicationBackfillId") is not None:
        out["replication_backfill_id"] = data["replicationBackfillId"]
    else:
        out["replication_backfill_id"] = ""
    if data.get("resultStatusFilter") is not None:
        import capo_ecr.types.replication_backfill_result_status

        out["result_status_filter"] = (
            capo_ecr.types.replication_backfill_result_status.deserialize_aws_json_1_1(
                data["resultStatusFilter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
