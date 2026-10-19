"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateRelationalDatabaseSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class CreateRelationalDatabaseSnapshotRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database on which to base your new snapshot.</p>"""
    relational_database_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name for your new database snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRelationalDatabaseSnapshotRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    out["relationalDatabaseSnapshotName"] = value["relational_database_snapshot_name"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRelationalDatabaseSnapshotRequest:
    out: CreateRelationalDatabaseSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("relationalDatabaseSnapshotName") is not None:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    else:
        out["relational_database_snapshot_name"] = ""
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
