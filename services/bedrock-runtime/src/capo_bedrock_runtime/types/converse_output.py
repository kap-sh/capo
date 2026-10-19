"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseOutput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.message


class _ConverseOutput_message(TypedDict, closed=True):
    message: "capo_bedrock_runtime.types.message.Message"


ConverseOutput: TypeAlias = _ConverseOutput_message | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ConverseOutput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ConverseOutput: cannot serialize unknown variant {value.name!r}"
        )
    elif "message" in value:
        import capo_bedrock_runtime.types.message

        return {
            "message": capo_bedrock_runtime.types.message.serialize_json(
                value["message"]
            )
        }
    else:
        raise SerializationError("ConverseOutput: no variant present")


def deserialize_json(data: dict) -> ConverseOutput:
    if data.get("message") is not None:
        import capo_bedrock_runtime.types.message

        return {
            "message": capo_bedrock_runtime.types.message.deserialize_json(
                data["message"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ConverseOutput: no recognized variant key")


def redact_sensitive(value: ConverseOutput) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "message" in value:
        import capo_bedrock_runtime.types.message

        out["message"] = capo_bedrock_runtime.types.message.redact_sensitive(
            value["message"]
        )
    return out
