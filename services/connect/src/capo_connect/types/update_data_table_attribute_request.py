"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.data_table_attribute_value_type
    import capo_connect.types.data_table_description
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_name
    import capo_connect.types.instance_id
    import capo_connect.types.validation


class UpdateDataTableAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The current name of the attribute to update. Used as an identifier since attribute names can be changed.</p>"""
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The new name for the attribute. Must conform to Connect human readable string specification and be unique within the data table.</p>"""
    value_type: (
        "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    )
    """<p>The updated value type for the attribute. When changing value types, existing values are not deleted but may return default values if incompatible.</p>"""
    description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>The updated description for the attribute.</p>"""
    primary: NotRequired["capo_connect.types.boolean.Boolean"]
    """<p>Whether the attribute should be treated as a primary key. Converting to primary attribute requires existing values to maintain uniqueness.</p>"""
    validation: NotRequired["capo_connect.types.validation.Validation"]
    """<p>The updated validation rules for the attribute. Changes do not affect existing values until they are modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableAttributeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        capo_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "validation" in value:
        import capo_connect.types.validation

        out["Validation"] = capo_connect.types.validation.serialize_json(
            value["validation"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataTableAttributeRequest:
    out: UpdateDataTableAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataTableAttributeRequest.name required")
    if data.get("ValueType") is not None:
        import capo_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            capo_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableAttributeRequest.value_type required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    if data.get("Validation") is not None:
        import capo_connect.types.validation

        out["validation"] = capo_connect.types.validation.deserialize_json(
            data["Validation"]
        )
    return out
