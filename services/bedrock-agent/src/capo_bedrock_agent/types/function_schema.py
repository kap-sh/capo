"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FunctionSchema``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.functions


class FunctionSchemaFunctionsMember(TypedDict, closed=True):
    functions: "capo_bedrock_agent.types.functions.Functions"


FunctionSchema: TypeAlias = FunctionSchemaFunctionsMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FunctionSchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "functions" in value:
        import capo_bedrock_agent.types.functions

        return {
            "functions": capo_bedrock_agent.types.functions.serialize_json(
                value["functions"]
            )
        }
    else:
        raise SerializationError("FunctionSchema: no variant present")


def deserialize_json(data: dict) -> FunctionSchema:
    if data.get("functions") is not None:
        import capo_bedrock_agent.types.functions

        return {
            "functions": capo_bedrock_agent.types.functions.deserialize_json(
                data["functions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FunctionSchema: no recognized variant key")
