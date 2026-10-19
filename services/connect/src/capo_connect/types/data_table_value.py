"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_set
    import capo_connect.types.region_name
    import capo_connect.types.string
    import capo_connect.types.timestamp


class DataTableValue(TypedDict, closed=True):
    primary_values: NotRequired[
        "capo_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The value's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The value's attribute name.</p>"""
    value: "capo_connect.types.string.String"
    """<p>The value's value.</p>"""
    lock_version: NotRequired[
        "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The value's lock version.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The value's last modified time.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The value's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValue) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import capo_connect.types.primary_values_set

        out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    out["AttributeName"] = value["attribute_name"]
    out["Value"] = value["value"]
    if "lock_version" in value:
        import capo_connect.types.data_table_lock_version

        out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
            value["lock_version"]
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> DataTableValue:
    out: DataTableValue = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
