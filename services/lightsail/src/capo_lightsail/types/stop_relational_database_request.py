"""Generated from Smithy shape ``com.amazonaws.lightsail#StopRelationalDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class StopRelationalDatabaseRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database to stop.</p>"""
    relational_database_snapshot_name: NotRequired[
        "capo_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of your new database snapshot to be created before stopping your database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRelationalDatabaseRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "relational_database_snapshot_name" in value:
        out["relationalDatabaseSnapshotName"] = value[
            "relational_database_snapshot_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRelationalDatabaseRequest:
    out: StopRelationalDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("relationalDatabaseSnapshotName") is not None:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    return out
