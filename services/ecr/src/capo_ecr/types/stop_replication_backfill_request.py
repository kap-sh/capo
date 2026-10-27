"""Generated from Smithy shape ``com.amazonaws.ecr#StopReplicationBackfillRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_backfill_id


class StopReplicationBackfillRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the replication backfill to stop. If you do not specify a registry, the default registry is assumed.</p>"""
    replication_backfill_id: (
        "capo_ecr.types.replication_backfill_id.ReplicationBackfillId"
    )
    """<p>The ID of the replication backfill to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationBackfillRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["replicationBackfillId"] = value["replication_backfill_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationBackfillRequest:
    out: StopReplicationBackfillRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("replicationBackfillId") is not None:
        out["replication_backfill_id"] = data["replicationBackfillId"]
    else:
        out["replication_backfill_id"] = ""
    return out
