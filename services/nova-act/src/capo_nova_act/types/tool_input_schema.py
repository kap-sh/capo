"""Generated from Smithy shape ``com.amazonaws.novaact#ToolInputSchema``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError, SerializationError
from capo_nova_act.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_nova_act.types.tool_input_schema_document


class _ToolInputSchema_json(TypedDict, closed=True):
    json: "capo_nova_act.types.tool_input_schema_document.ToolInputSchemaDocument"


ToolInputSchema: TypeAlias = _ToolInputSchema_json | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ToolInputSchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolInputSchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolInputSchema: no variant present")


def deserialize_json(data: dict) -> ToolInputSchema:
    if data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ToolInputSchema: no recognized variant key")
