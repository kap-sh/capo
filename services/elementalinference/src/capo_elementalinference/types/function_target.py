"""Generated from Smithy shape ``com.amazonaws.elementalinference#FunctionTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError
from capo_elementalinference.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_elementalinference.types.bedrock_function_target
    import capo_elementalinference.types.passthrough_function_target


class FunctionTargetBedrockMember(TypedDict, closed=True):
    bedrock: (
        "capo_elementalinference.types.bedrock_function_target.BedrockFunctionTarget"
    )


class FunctionTargetPassthroughMember(TypedDict, closed=True):
    passthrough: "capo_elementalinference.types.passthrough_function_target.PassthroughFunctionTarget"


FunctionTarget: TypeAlias = (
    FunctionTargetBedrockMember | FunctionTargetPassthroughMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FunctionTarget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FunctionTarget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "bedrock" in value:
        import capo_elementalinference.types.bedrock_function_target

        return {
            "bedrock": capo_elementalinference.types.bedrock_function_target.serialize_json(
                value["bedrock"]
            )
        }
    elif "passthrough" in value:
        import capo_elementalinference.types.passthrough_function_target

        return {
            "passthrough": capo_elementalinference.types.passthrough_function_target.serialize_json(
                value["passthrough"]
            )
        }
    else:
        raise SerializationError("FunctionTarget: no variant present")


def deserialize_json(data: dict) -> FunctionTarget:
    if data.get("bedrock") is not None:
        import capo_elementalinference.types.bedrock_function_target

        return {
            "bedrock": capo_elementalinference.types.bedrock_function_target.deserialize_json(
                data["bedrock"]
            )
        }
    elif data.get("passthrough") is not None:
        import capo_elementalinference.types.passthrough_function_target

        return {
            "passthrough": capo_elementalinference.types.passthrough_function_target.deserialize_json(
                data["passthrough"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FunctionTarget: no recognized variant key")
