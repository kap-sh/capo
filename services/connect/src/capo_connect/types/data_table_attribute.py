"""Generated from Smithy shape ``com.amazonaws.connect#DataTableAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.boolean
    import capo_connect.types.data_table_attribute_value_type
    import capo_connect.types.data_table_description
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.data_table_version
    import capo_connect.types.region_name
    import capo_connect.types.timestamp
    import capo_connect.types.validation


class DataTableAttribute(TypedDict, closed=True):
    attribute_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier for the attribute within the data table.</p>"""
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The human-readable name of the attribute. Must be unique within the data table and conform to Connect naming standards.</p>"""
    value_type: (
        "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    )
    """<p>The type of value allowed for this attribute. Must be one of TEXT, TEXT_LIST, NUMBER, NUMBER_LIST, or BOOLEAN. Determines how values are validated and processed.</p>"""
    description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description explaining the purpose and usage of this attribute.</p>"""
    data_table_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier of the data table that contains this attribute.</p>"""
    data_table_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the data table that contains this attribute.</p>"""
    primary: "capo_connect.types.boolean.Boolean"
    """<p>Boolean indicating whether this attribute is used as a primary key for record identification. Primary attributes must have unique value combinations and cannot contain expressions.</p>"""
    version: NotRequired["capo_connect.types.data_table_version.DataTableVersion"]
    """<p>The version identifier for this attribute, used for versioning and change tracking.</p>"""
    lock_version: NotRequired[
        "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The lock version for this attribute, used for optimistic locking to prevent concurrent modification conflicts.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this attribute was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this attribute was last modified, used for region replication.</p>"""
    validation: NotRequired["capo_connect.types.validation.Validation"]
    """<p>The validation rules applied to values of this attribute. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations for data integrity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableAttribute) -> dict:
    out: dict = {}
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    out["Name"] = value["name"]
    import capo_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        capo_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "data_table_id" in value:
        out["DataTableId"] = value["data_table_id"]
    if "data_table_arn" in value:
        out["DataTableArn"] = value["data_table_arn"]
    out["Primary"] = value.get("primary", False)
    if "version" in value:
        out["Version"] = value["version"]
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
    if "validation" in value:
        import capo_connect.types.validation

        out["Validation"] = capo_connect.types.validation.serialize_json(
            value["validation"]
        )
    return out


def deserialize_json(data: dict) -> DataTableAttribute:
    out: DataTableAttribute = {}  # type: ignore[typeddict-item]
    if data.get("AttributeId") is not None:
        out["attribute_id"] = data["AttributeId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataTableId") is not None:
        out["data_table_id"] = data["DataTableId"]
    if data.get("DataTableArn") is not None:
        out["data_table_arn"] = data["DataTableArn"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    if data.get("Version") is not None:
        out["version"] = data["Version"]
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
    if data.get("Validation") is not None:
        import capo_connect.types.validation

        out["validation"] = capo_connect.types.validation.deserialize_json(
            data["Validation"]
        )
    return out
