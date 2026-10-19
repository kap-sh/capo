"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateRelationalDatabaseFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class CreateRelationalDatabaseFromSnapshotRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name to use for your new Lightsail database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>"""
    availability_zone: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Availability Zone in which to create your new database. Use the <code>us-east-2a</code> case-sensitive format.</p> <p>You can get a list of Availability Zones by using the <code>get regions</code> operation. Be sure to add the <code>include relational database Availability Zones</code> parameter to your request.</p>"""
    publicly_accessible: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies the accessibility options for your new database. A value of <code>true</code> specifies a database that is available to resources outside of your Lightsail account. A value of <code>false</code> specifies a database that is available only to your Lightsail resources in the same region as your database.</p>"""
    relational_database_snapshot_name: NotRequired[
        "capo_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of the database snapshot from which to create your new database.</p>"""
    relational_database_bundle_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The bundle ID for your new database. A bundle describes the performance specifications for your database.</p> <p>You can get a list of database bundle IDs by using the <code>get relational database bundles</code> operation.</p> <p>When creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.</p>"""
    source_relational_database_name: NotRequired[
        "capo_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of the source database.</p>"""
    restore_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date and time to restore your database from.</p> <p>Constraints:</p> <ul> <li> <p>Must be before the latest restorable time for the database.</p> </li> <li> <p>Cannot be specified if the <code>use latest restorable time</code> parameter is <code>true</code>.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the restore time.</p> </li> </ul>"""
    use_latest_restorable_time: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether your database is restored from the latest backup time. A value of <code>true</code> restores from the latest backup time. </p> <p>Default: <code>false</code> </p> <p>Constraints: Cannot be specified if the <code>restore time</code> parameter is provided.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRelationalDatabaseFromSnapshotRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "relational_database_snapshot_name" in value:
        out["relationalDatabaseSnapshotName"] = value[
            "relational_database_snapshot_name"
        ]
    if "relational_database_bundle_id" in value:
        out["relationalDatabaseBundleId"] = value["relational_database_bundle_id"]
    if "source_relational_database_name" in value:
        out["sourceRelationalDatabaseName"] = value["source_relational_database_name"]
    if "restore_time" in value:
        import capo_lightsail.types.iso_date

        out["restoreTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["restore_time"]
        )
    if "use_latest_restorable_time" in value:
        out["useLatestRestorableTime"] = value["use_latest_restorable_time"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRelationalDatabaseFromSnapshotRequest:
    out: CreateRelationalDatabaseFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("relationalDatabaseSnapshotName") is not None:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    if data.get("relationalDatabaseBundleId") is not None:
        out["relational_database_bundle_id"] = data["relationalDatabaseBundleId"]
    if data.get("sourceRelationalDatabaseName") is not None:
        out["source_relational_database_name"] = data["sourceRelationalDatabaseName"]
    if data.get("restoreTime") is not None:
        import capo_lightsail.types.iso_date

        out["restore_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["restoreTime"]
        )
    if data.get("useLatestRestorableTime") is not None:
        out["use_latest_restorable_time"] = data["useLatestRestorableTime"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
