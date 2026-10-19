"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteRelationalDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name


class DeleteRelationalDatabaseRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database that you are deleting.</p>"""
    skip_final_snapshot: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Determines whether a final database snapshot is created before your database is deleted. If <code>true</code> is specified, no database snapshot is created. If <code>false</code> is specified, a database snapshot is created before your database is deleted.</p> <p>You must specify the <code>final relational database snapshot name</code> parameter if the <code>skip final snapshot</code> parameter is <code>false</code>.</p> <p>Default: <code>false</code> </p>"""
    final_relational_database_snapshot_name: NotRequired[
        "capo_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of the database snapshot created if <code>skip final snapshot</code> is <code>false</code>, which is the default value for that parameter.</p> <note> <p>Specifying this parameter and also specifying the <code>skip final snapshot</code> parameter to <code>true</code> results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRelationalDatabaseRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "skip_final_snapshot" in value:
        out["skipFinalSnapshot"] = value["skip_final_snapshot"]
    if "final_relational_database_snapshot_name" in value:
        out["finalRelationalDatabaseSnapshotName"] = value[
            "final_relational_database_snapshot_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRelationalDatabaseRequest:
    out: DeleteRelationalDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("skipFinalSnapshot") is not None:
        out["skip_final_snapshot"] = data["skipFinalSnapshot"]
    if data.get("finalRelationalDatabaseSnapshotName") is not None:
        out["final_relational_database_snapshot_name"] = data[
            "finalRelationalDatabaseSnapshotName"
        ]
    return out
