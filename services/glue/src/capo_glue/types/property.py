"""Generated from Smithy shape ``com.amazonaws.glue#Property``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.allowed_values
    import capo_glue.types.bool
    import capo_glue.types.data_operations
    import capo_glue.types.property_description_string
    import capo_glue.types.property_location
    import capo_glue.types.property_name
    import capo_glue.types.property_types


class Property(TypedDict, closed=True):
    name: "capo_glue.types.property_name.PropertyName"
    """<p>The name of the property.</p>"""
    description: "capo_glue.types.property_description_string.PropertyDescriptionString"
    """<p>A description of the property.</p>"""
    required: "capo_glue.types.bool.Bool"
    """<p>Indicates whether the property is required.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value for the property.</p>"""
    property_types: "capo_glue.types.property_types.PropertyTypes"
    """<p>Describes the type of property.</p>"""
    allowed_values: NotRequired["capo_glue.types.allowed_values.AllowedValues"]
    """<p>A list of <code>AllowedValue</code> objects representing the values allowed for the property.</p>"""
    data_operation_scopes: NotRequired["capo_glue.types.data_operations.DataOperations"]
    """<p>Indicates which data operations are applicable to the property.</p>"""
    key_override: NotRequired["str"]
    """<p>A key name to use when sending this property in API requests, if different from the display name.</p>"""
    property_location: NotRequired["capo_glue.types.property_location.PropertyLocation"]
    """<p>Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Property) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["Required"] = value["required"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    import capo_glue.types.property_types

    out["PropertyTypes"] = capo_glue.types.property_types.serialize_aws_json_1_1(
        value.get("property_types", [])
    )
    if "allowed_values" in value:
        import capo_glue.types.allowed_values

        out["AllowedValues"] = capo_glue.types.allowed_values.serialize_aws_json_1_1(
            value["allowed_values"]
        )
    if "data_operation_scopes" in value:
        import capo_glue.types.data_operations

        out["DataOperationScopes"] = (
            capo_glue.types.data_operations.serialize_aws_json_1_1(
                value["data_operation_scopes"]
            )
        )
    if "key_override" in value:
        out["KeyOverride"] = value["key_override"]
    if "property_location" in value:
        import capo_glue.types.property_location

        out["PropertyLocation"] = (
            capo_glue.types.property_location.serialize_aws_json_1_1(
                value["property_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Property:
    out: Property = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    else:
        out["required"] = False
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("PropertyTypes") is not None:
        import capo_glue.types.property_types

        out["property_types"] = capo_glue.types.property_types.deserialize_aws_json_1_1(
            data["PropertyTypes"]
        )
    else:
        out["property_types"] = []
    if data.get("AllowedValues") is not None:
        import capo_glue.types.allowed_values

        out["allowed_values"] = capo_glue.types.allowed_values.deserialize_aws_json_1_1(
            data["AllowedValues"]
        )
    if data.get("DataOperationScopes") is not None:
        import capo_glue.types.data_operations

        out["data_operation_scopes"] = (
            capo_glue.types.data_operations.deserialize_aws_json_1_1(
                data["DataOperationScopes"]
            )
        )
    if data.get("KeyOverride") is not None:
        out["key_override"] = data["KeyOverride"]
    if data.get("PropertyLocation") is not None:
        import capo_glue.types.property_location

        out["property_location"] = (
            capo_glue.types.property_location.deserialize_aws_json_1_1(
                data["PropertyLocation"]
            )
        )
    return out
