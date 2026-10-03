"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#JsonSchemaDefinition``."""

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError


class JsonSchemaDefinition(TypedDict, closed=True):
    schema: "str"
    """<p> The JSON schema to constrain the model's output. For more information, see <a href="https://json-schema.org/understanding-json-schema/reference">JSON Schema Reference</a>. </p>"""
    name: NotRequired["str"]
    """<p> The name of the JSON schema. </p>"""
    description: NotRequired["str"]
    """<p> A description of the JSON schema. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JsonSchemaDefinition) -> dict:
    out: dict = {}
    out["schema"] = value["schema"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> JsonSchemaDefinition:
    out: JsonSchemaDefinition = {}  # type: ignore[typeddict-item]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("JsonSchemaDefinition.schema required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
