"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.bool
    import capo_glue.types.connector_property_key
    import capo_glue.types.list_of_string
    import capo_glue.types.property_location
    import capo_glue.types.property_name
    import capo_glue.types.property_type


class ConnectorProperty(TypedDict, closed=True):
    name: "capo_glue.types.property_name.PropertyName"
    """<p>The name of the property.</p>"""
    key_override: NotRequired[
        "capo_glue.types.connector_property_key.ConnectorPropertyKey"
    ]
    """<p>A key name to use when sending this property in API requests, if different from the display name.</p>"""
    required: "capo_glue.types.bool.Bool"
    """<p>Indicates whether the property is required.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value for the property.</p>"""
    allowed_values: NotRequired["capo_glue.types.list_of_string.ListOfString"]
    """<p>A list of <code>AllowedValue</code> objects representing the values allowed for the property.</p>"""
    property_location: NotRequired["capo_glue.types.property_location.PropertyLocation"]
    """<p>Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.</p>"""
    property_type: "capo_glue.types.property_type.PropertyType"
    """<p>The data type of this property</p>"""
    format: NotRequired["str"]
    """<p>A format template for the property value that defines how the value should be formatted before sending it in API requests. Use <code>{value}</code> as a placeholder for the actual property value (for example, <code>SSWS {value}</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorProperty) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "key_override" in value:
        out["KeyOverride"] = value["key_override"]
    out["Required"] = value["required"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "allowed_values" in value:
        import capo_glue.types.list_of_string

        out["AllowedValues"] = capo_glue.types.list_of_string.serialize_aws_json_1_1(
            value["allowed_values"]
        )
    if "property_location" in value:
        import capo_glue.types.property_location

        out["PropertyLocation"] = (
            capo_glue.types.property_location.serialize_aws_json_1_1(
                value["property_location"]
            )
        )
    import capo_glue.types.property_type

    out["PropertyType"] = capo_glue.types.property_type.serialize_aws_json_1_1(
        value["property_type"]
    )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorProperty:
    out: ConnectorProperty = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("KeyOverride") is not None:
        out["key_override"] = data["KeyOverride"]
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    else:
        out["required"] = False
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("AllowedValues") is not None:
        import capo_glue.types.list_of_string

        out["allowed_values"] = capo_glue.types.list_of_string.deserialize_aws_json_1_1(
            data["AllowedValues"]
        )
    if data.get("PropertyLocation") is not None:
        import capo_glue.types.property_location

        out["property_location"] = (
            capo_glue.types.property_location.deserialize_aws_json_1_1(
                data["PropertyLocation"]
            )
        )
    if data.get("PropertyType") is not None:
        import capo_glue.types.property_type

        out["property_type"] = capo_glue.types.property_type.deserialize_aws_json_1_1(
            data["PropertyType"]
        )
    else:
        import typing

        out["property_type"] = typing.cast(
            "capo_glue.types.property_type.PropertyType", ""
        )
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    return out
