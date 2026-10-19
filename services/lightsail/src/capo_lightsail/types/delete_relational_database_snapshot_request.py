"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteRelationalDatabaseSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DeleteRelationalDatabaseSnapshotRequest(TypedDict, closed=True):
    relational_database_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database snapshot that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRelationalDatabaseSnapshotRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseSnapshotName"] = value["relational_database_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRelationalDatabaseSnapshotRequest:
    out: DeleteRelationalDatabaseSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseSnapshotName") is not None:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    else:
        out["relational_database_snapshot_name"] = ""
    return out
