"""Generated from Smithy shape ``com.amazonaws.ecr#StopReplicationBackfillResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.date
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_backfill_id
    import capo_ecr.types.replication_backfill_status
    import capo_ecr.types.replication_destination


class StopReplicationBackfillResponse(TypedDict, closed=True):
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
    """<p>The current status of the replication backfill. When you stop a replication backfill, its status is <code>STOPPED</code> if the backfill is stopped immediately, or <code>STOPPING</code> if there are replications still in progress that must complete before the backfill stops.</p>"""
    started_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time, in JavaScript date format, when the replication backfill was started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationBackfillResponse) -> dict:
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
    if "started_at" in value:
        import capo_ecr.types.date

        out["startedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
            value["started_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationBackfillResponse:
    out: StopReplicationBackfillResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("startedAt") is not None:
        import capo_ecr.types.date

        out["started_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    return out
