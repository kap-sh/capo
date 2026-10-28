"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormatStructure``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.json_schema_definition


class OutputFormatStructureJsonSchemaMember(TypedDict, closed=True):
    jsonSchema: "capo_bedrock_runtime.types.json_schema_definition.JsonSchemaDefinition"


OutputFormatStructure: TypeAlias = (
    OutputFormatStructureJsonSchemaMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormatStructure) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OutputFormatStructure: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "jsonSchema" in value:
        import capo_bedrock_runtime.types.json_schema_definition

        return {
            "jsonSchema": capo_bedrock_runtime.types.json_schema_definition.serialize_json(
                value["jsonSchema"]
            )
        }
    else:
        raise SerializationError("OutputFormatStructure: no variant present")


def deserialize_json(data: dict) -> OutputFormatStructure:
    if data.get("jsonSchema") is not None:
        import capo_bedrock_runtime.types.json_schema_definition

        return {
            "jsonSchema": capo_bedrock_runtime.types.json_schema_definition.deserialize_json(
                data["jsonSchema"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OutputFormatStructure: no recognized variant key")
