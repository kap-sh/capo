"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueSuccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_response_set
    import capo_connect.types.region_name
    import capo_connect.types.string
    import capo_connect.types.timestamp


class BatchDescribeDataTableValueSuccessResult(TypedDict, closed=True):
    record_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The result's record ID.</p>"""
    attribute_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The result's attribute ID.</p>"""
    primary_values: (
        "capo_connect.types.primary_values_response_set.PrimaryValuesResponseSet"
    )
    """<p>The result's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    value: NotRequired["capo_connect.types.string.String"]
    """<p>The result's value.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The result's lock version.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The result's last modified time.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The result's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueSuccessResult) -> dict:
    out: dict = {}
    out["RecordId"] = value["record_id"]
    out["AttributeId"] = value["attribute_id"]
    import capo_connect.types.primary_values_response_set

    out["PrimaryValues"] = (
        capo_connect.types.primary_values_response_set.serialize_json(
            value["primary_values"]
        )
    )
    out["AttributeName"] = value["attribute_name"]
    if "value" in value:
        out["Value"] = value["value"]
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


def deserialize_json(data: dict) -> BatchDescribeDataTableValueSuccessResult:
    out: BatchDescribeDataTableValueSuccessResult = {}  # type: ignore[typeddict-item]
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    else:
        out["record_id"] = ""
    if data.get("AttributeId") is not None:
        out["attribute_id"] = data["AttributeId"]
    else:
        out["attribute_id"] = ""
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_response_set

        out["primary_values"] = (
            capo_connect.types.primary_values_response_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        out["primary_values"] = []
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.lock_version required"
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
