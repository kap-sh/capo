"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicationGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_status
    import capo_keyspaces.types.region
    import capo_keyspaces.types.tables_replication_progress


class ReplicationGroupStatus(TypedDict, closed=True):
    region: "capo_keyspaces.types.region.region"
    """<p> The name of the Region that was added to the keyspace. </p>"""
    keyspace_status: "capo_keyspaces.types.keyspace_status.KeyspaceStatus"
    """<p> The status of the keyspace. </p>"""
    tables_replication_progress: NotRequired[
        "capo_keyspaces.types.tables_replication_progress.TablesReplicationProgress"
    ]
    """<p> This shows the replication progress of tables in the keyspace. The value is expressed as a percentage of the newly replicated tables with status <code>Active</code> compared to the total number of tables in the keyspace. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupStatus) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["keyspaceStatus"] = value["keyspace_status"]
    if "tables_replication_progress" in value:
        out["tablesReplicationProgress"] = value["tables_replication_progress"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationGroupStatus:
    out: ReplicationGroupStatus = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("keyspaceStatus") is not None:
        out["keyspace_status"] = data["keyspaceStatus"]
    else:
        out["keyspace_status"] = ""
    if data.get("tablesReplicationProgress") is not None:
        out["tables_replication_progress"] = data["tablesReplicationProgress"]
    return out
