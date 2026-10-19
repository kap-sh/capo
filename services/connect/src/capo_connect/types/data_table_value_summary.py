"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_attribute_value_type
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_response_set
    import capo_connect.types.region_name
    import capo_connect.types.string
    import capo_connect.types.timestamp


class DataTableValueSummary(TypedDict, closed=True):
    record_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The summary's record ID.</p>"""
    attribute_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The summary's attribute ID.</p>"""
    primary_values: (
        "capo_connect.types.primary_values_response_set.PrimaryValuesResponseSet"
    )
    """<p>The summary's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The summary's attribute name.</p>"""
    value_type: (
        "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    )
    """<p>The summary's value type.</p>"""
    value: "capo_connect.types.string.String"
    """<p>The summary's value.</p>"""
    lock_version: NotRequired[
        "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The summary's lock version.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The summary's last modified time.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The summary's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueSummary) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    import capo_connect.types.primary_values_response_set

    out["PrimaryValues"] = (
        capo_connect.types.primary_values_response_set.serialize_json(
            value["primary_values"]
        )
    )
    out["AttributeName"] = value["attribute_name"]
    import capo_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        capo_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
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


def deserialize_json(data: dict) -> DataTableValueSummary:
    out: DataTableValueSummary = {}  # type: ignore[typeddict-item]
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    if data.get("AttributeId") is not None:
        out["attribute_id"] = data["AttributeId"]
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
    if data.get("ValueType") is not None:
        import capo_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            capo_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        import typing

        out["value_type"] = typing.cast(
            "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType",
            "",
        )
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
