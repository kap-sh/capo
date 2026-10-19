"""Generated from Smithy shape ``com.amazonaws.connect#DataTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.data_table_description
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_level
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.data_table_status
    import capo_connect.types.data_table_version
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.time_zone
    import capo_connect.types.timestamp


class DataTable(TypedDict, closed=True):
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The human-readable name of the data table. Must be unique within the instance and conform to Connect naming standards.</p>"""
    id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Does not include version aliases.</p>"""
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the data table. Does not include version aliases.</p>"""
    time_zone: "capo_connect.types.time_zone.TimeZone"
    """<p>The IANA timezone identifier used when resolving time based dynamic values. Required even if no time slices are specified.</p>"""
    description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description of the data table's purpose and contents.</p>"""
    value_lock_level: NotRequired[
        "capo_connect.types.data_table_lock_level.DataTableLockLevel"
    ]
    """<p>The data level that concurrent value edits are locked on. One of DATA_TABLE, PRIMARY_VALUE, ATTRIBUTE, VALUE, and NONE. Determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.</p>"""
    lock_version: NotRequired[
        "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The lock version information used for optimistic locking and table versioning. Changes with each update to prevent concurrent modification conflicts.</p>"""
    version: NotRequired["capo_connect.types.data_table_version.DataTableVersion"]
    """<p>A unique identifier and alias for customer managed versions (not $LATEST or $SAVED).</p>"""
    version_description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>A description of the customer managed version.</p>"""
    status: NotRequired["capo_connect.types.data_table_status.DataTableStatus"]
    """<p>The current status of the data table. One of PUBLISHED or SAVED.</p>"""
    created_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the data table was created.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the data table or any of its properties were last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the data table was last modified, used for region replication.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>Key-value pairs for attribute based access control (TBAC or ABAC) and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTable) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    out["TimeZone"] = value["time_zone"]
    if "description" in value:
        out["Description"] = value["description"]
    if "value_lock_level" in value:
        import capo_connect.types.data_table_lock_level

        out["ValueLockLevel"] = capo_connect.types.data_table_lock_level.serialize_json(
            value["value_lock_level"]
        )
    if "lock_version" in value:
        import capo_connect.types.data_table_lock_version

        out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
            value["lock_version"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "status" in value:
        import capo_connect.types.data_table_status

        out["Status"] = capo_connect.types.data_table_status.serialize_json(
            value["status"]
        )
    if "created_time" in value:
        import capo_connect.types.timestamp

        out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DataTable:
    out: DataTable = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    else:
        out["time_zone"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ValueLockLevel") is not None:
        import capo_connect.types.data_table_lock_level

        out["value_lock_level"] = (
            capo_connect.types.data_table_lock_level.deserialize_json(
                data["ValueLockLevel"]
            )
        )
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Status") is not None:
        import capo_connect.types.data_table_status

        out["status"] = capo_connect.types.data_table_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
