"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeReplicationBackfillResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.date
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_backfill_error
    import capo_ecr.types.replication_backfill_id
    import capo_ecr.types.replication_backfill_progress
    import capo_ecr.types.replication_backfill_result_list
    import capo_ecr.types.replication_backfill_status
    import capo_ecr.types.replication_destination


class DescribeReplicationBackfillResultsResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    replication_backfill_id: NotRequired[
        "capo_ecr.types.replication_backfill_id.ReplicationBackfillId"
    ]
    """<p>The ID of the replication backfill.</p>"""
    destination: NotRequired[
        "capo_ecr.types.replication_destination.ReplicationDestination"
    ]
    """<p>The destination Region and registry to which the images are replicated.</p>"""
    status: NotRequired[
        "capo_ecr.types.replication_backfill_status.ReplicationBackfillStatus"
    ]
    """<p>The current status of the replication backfill.</p>"""
    failure_code: NotRequired[
        "capo_ecr.types.replication_backfill_error.ReplicationBackfillError"
    ]
    """<p>The failure code for a replication backfill that has failed.</p>"""
    progress: NotRequired[
        "capo_ecr.types.replication_backfill_progress.ReplicationBackfillProgress"
    ]
    """<p>The progress of the replication backfill, including the total, completed, and failed replication counts. This value is <code>null</code> until the replication backfill finishes preparing the set of images to replicate. It is therefore <code>null</code> while the replication backfill is <code>PREPARING</code>, and remains <code>null</code> if the replication backfill is stopped before preparation completes.</p>"""
    results: NotRequired[
        "capo_ecr.types.replication_backfill_result_list.ReplicationBackfillResultList"
    ]
    """<p>The per-image results for the replication backfill. Results are available only after the replication backfill reaches a terminal status.</p>"""
    started_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time, in JavaScript date format, when the replication backfill was started.</p>"""
    ended_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time, in JavaScript date format, when the replication backfill ended. This value is <code>null</code> while the replication backfill is still in progress.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeReplicationBackfillResults</code> request. When the results of a <code>DescribeReplicationBackfillResults</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationBackfillResultsResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "replication_backfill_id" in value:
        out["replicationBackfillId"] = value["replication_backfill_id"]
    if "destination" in value:
        import capo_ecr.types.replication_destination

        out["destination"] = (
            capo_ecr.types.replication_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "status" in value:
        import capo_ecr.types.replication_backfill_status

        out["status"] = (
            capo_ecr.types.replication_backfill_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "progress" in value:
        import capo_ecr.types.replication_backfill_progress

        out["progress"] = (
            capo_ecr.types.replication_backfill_progress.serialize_aws_json_1_1(
                value["progress"]
            )
        )
    if "results" in value:
        import capo_ecr.types.replication_backfill_result_list

        out["results"] = (
            capo_ecr.types.replication_backfill_result_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "started_at" in value:
        import capo_ecr.types.date

        out["startedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_ecr.types.date

        out["endedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(value["ended_at"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationBackfillResultsResponse:
    out: DescribeReplicationBackfillResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("replicationBackfillId") is not None:
        out["replication_backfill_id"] = data["replicationBackfillId"]
    if data.get("destination") is not None:
        import capo_ecr.types.replication_destination

        out["destination"] = (
            capo_ecr.types.replication_destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if data.get("status") is not None:
        import capo_ecr.types.replication_backfill_status

        out["status"] = (
            capo_ecr.types.replication_backfill_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    if data.get("progress") is not None:
        import capo_ecr.types.replication_backfill_progress

        out["progress"] = (
            capo_ecr.types.replication_backfill_progress.deserialize_aws_json_1_1(
                data["progress"]
            )
        )
    if data.get("results") is not None:
        import capo_ecr.types.replication_backfill_result_list

        out["results"] = (
            capo_ecr.types.replication_backfill_result_list.deserialize_aws_json_1_1(
                data["results"]
            )
        )
    if data.get("startedAt") is not None:
        import capo_ecr.types.date

        out["started_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_ecr.types.date

        out["ended_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(data["endedAt"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
