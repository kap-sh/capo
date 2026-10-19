"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SchemaDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.required_properties
    import capo_bedrock_agentcore_control.types.schema_definition
    import capo_bedrock_agentcore_control.types.schema_properties
    import capo_bedrock_agentcore_control.types.schema_type


class SchemaDefinition(TypedDict, closed=True):
    type: "capo_bedrock_agentcore_control.types.schema_type.SchemaType"
    """<p>The type of the schema definition. This field specifies the data type of the schema.</p>"""
    properties: NotRequired[
        "capo_bedrock_agentcore_control.types.schema_properties.SchemaProperties"
    ]
    """<p>The properties of the schema definition. These properties define the fields in the schema.</p>"""
    required: NotRequired[
        "capo_bedrock_agentcore_control.types.required_properties.RequiredProperties"
    ]
    """<p>The required fields in the schema definition. These fields must be provided when using the schema.</p>"""
    items: NotRequired[
        "capo_bedrock_agentcore_control.types.schema_definition.SchemaDefinition"
    ]
    """<p>The items in the schema definition. This field is used for array types to define the structure of the array elements.</p>"""
    description: NotRequired["str"]
    """<p>The description of the schema definition. This description provides information about the purpose and usage of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaDefinition) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.schema_type

    out["type"] = capo_bedrock_agentcore_control.types.schema_type.serialize_json(
        value["type"]
    )
    if "properties" in value:
        import capo_bedrock_agentcore_control.types.schema_properties

        out["properties"] = (
            capo_bedrock_agentcore_control.types.schema_properties.serialize_json(
                value["properties"]
            )
        )
    if "required" in value:
        import capo_bedrock_agentcore_control.types.required_properties

        out["required"] = (
            capo_bedrock_agentcore_control.types.required_properties.serialize_json(
                value["required"]
            )
        )
    if "items" in value:
        import capo_bedrock_agentcore_control.types.schema_definition

        out["items"] = (
            capo_bedrock_agentcore_control.types.schema_definition.serialize_json(
                value["items"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SchemaDefinition:
    out: SchemaDefinition = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.schema_type

        out["type"] = capo_bedrock_agentcore_control.types.schema_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.schema_type.SchemaType", ""
        )
    if data.get("properties") is not None:
        import capo_bedrock_agentcore_control.types.schema_properties

        out["properties"] = (
            capo_bedrock_agentcore_control.types.schema_properties.deserialize_json(
                data["properties"]
            )
        )
    if data.get("required") is not None:
        import capo_bedrock_agentcore_control.types.required_properties

        out["required"] = (
            capo_bedrock_agentcore_control.types.required_properties.deserialize_json(
                data["required"]
            )
        )
    if data.get("items") is not None:
        import capo_bedrock_agentcore_control.types.schema_definition

        out["items"] = (
            capo_bedrock_agentcore_control.types.schema_definition.deserialize_json(
                data["items"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
