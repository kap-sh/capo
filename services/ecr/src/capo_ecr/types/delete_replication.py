"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteReplication``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.delete_replication_flag


class DeleteReplication(TypedDict, closed=True):
    enabled: "capo_ecr.types.delete_replication_flag.DeleteReplicationFlag"
    """<p>Specifies whether delete replication is enabled. If set to <code>true</code>, the service replicates image deletions and image tag removals from the source registry to each replication destination. If set to <code>false</code>, the service does not replicate image deletions or image tag removals.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplication) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplication:
    out: DeleteReplication = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
