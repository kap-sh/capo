"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillProgress``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.non_negative_integer
    import capo_ecr.types.replication_error_list


class ReplicationBackfillProgress(TypedDict, closed=True):
    total_replication_count: "capo_ecr.types.non_negative_integer.NonNegativeInteger"
    """<p>The total number of replications that the backfill will perform. Each image and tag combination is counted as a single replication.</p>"""
    completed_replication_count: (
        "capo_ecr.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The number of replications that have completed successfully.</p>"""
    failed_replication_count: "capo_ecr.types.non_negative_integer.NonNegativeInteger"
    """<p>The number of replications that have failed.</p>"""
    failure_codes: "capo_ecr.types.replication_error_list.ReplicationErrorList"
    """<p>The distinct failure codes for the replications that have failed. Each failure code appears at most once, regardless of how many replications failed with that code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillProgress) -> dict:
    out: dict = {}
    out["totalReplicationCount"] = value["total_replication_count"]
    out["completedReplicationCount"] = value["completed_replication_count"]
    out["failedReplicationCount"] = value["failed_replication_count"]
    import capo_ecr.types.replication_error_list

    out["failureCodes"] = capo_ecr.types.replication_error_list.serialize_aws_json_1_1(
        value["failure_codes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationBackfillProgress:
    out: ReplicationBackfillProgress = {}  # type: ignore[typeddict-item]
    if data.get("totalReplicationCount") is not None:
        out["total_replication_count"] = data["totalReplicationCount"]
    else:
        out["total_replication_count"] = 0
    if data.get("completedReplicationCount") is not None:
        out["completed_replication_count"] = data["completedReplicationCount"]
    else:
        out["completed_replication_count"] = 0
    if data.get("failedReplicationCount") is not None:
        out["failed_replication_count"] = data["failedReplicationCount"]
    else:
        out["failed_replication_count"] = 0
    if data.get("failureCodes") is not None:
        import capo_ecr.types.replication_error_list

        out["failure_codes"] = (
            capo_ecr.types.replication_error_list.deserialize_aws_json_1_1(
                data["failureCodes"]
            )
        )
    else:
        out["failure_codes"] = []
    return out
