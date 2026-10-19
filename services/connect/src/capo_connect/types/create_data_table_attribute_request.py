"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableAttributeRequest``."""

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


class CreateDataTableAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be one of the two available system managed aliases, $SAVED or $LATEST.</p>"""
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The name for the attribute. Must conform to Connect human readable string specification and have 1-127 characters. Must not start with the reserved case insensitive values 'connect:' and 'aws:'. Whitespace trimmed before persisting. Must be unique for the data table using case-insensitive comparison.</p>"""
    value_type: (
        "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    )
    """<p>The type of value allowed or the resultant type after the value's expression is evaluated. Must be one of TEXT, TEXT_LIST, NUMBER, NUMBER_LIST, and BOOLEAN.</p>"""
    description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description for the attribute. Must conform to Connect human readable string specification and have 0-250 characters. Whitespace trimmed before persisting.</p>"""
    primary: NotRequired["capo_connect.types.boolean.Boolean"]
    """<p>Optional boolean that defaults to false. Determines if the value is used to identify a record in the table. Values for primary attributes must not be expressions.</p>"""
    validation: NotRequired["capo_connect.types.validation.Validation"]
    """<p>Optional validation rules for the attribute. Borrows heavily from JSON Schema - Draft 2020-12. The maximum length of arrays within validations and depth of validations is 5. There are default limits that apply to all types. Customer specified limits in excess of the default limits are not permitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableAttributeRequest) -> dict:
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


def deserialize_json(data: dict) -> CreateDataTableAttributeRequest:
    out: CreateDataTableAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataTableAttributeRequest.name required")
    if data.get("ValueType") is not None:
        import capo_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            capo_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTableAttributeRequest.value_type required"
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
