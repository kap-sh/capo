"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CountTokensInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.converse_tokens_request
    import capo_bedrock_runtime.types.invoke_model_tokens_request


class _CountTokensInput_invokeModel(TypedDict, closed=True):
    invokeModel: "capo_bedrock_runtime.types.invoke_model_tokens_request.InvokeModelTokensRequest"


class _CountTokensInput_converse(TypedDict, closed=True):
    converse: "capo_bedrock_runtime.types.converse_tokens_request.ConverseTokensRequest"


CountTokensInput: TypeAlias = (
    _CountTokensInput_invokeModel | _CountTokensInput_converse | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CountTokensInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CountTokensInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "invokeModel" in value:
        import capo_bedrock_runtime.types.invoke_model_tokens_request

        return {
            "invokeModel": capo_bedrock_runtime.types.invoke_model_tokens_request.serialize_json(
                value["invokeModel"]
            )
        }
    elif "converse" in value:
        import capo_bedrock_runtime.types.converse_tokens_request

        return {
            "converse": capo_bedrock_runtime.types.converse_tokens_request.serialize_json(
                value["converse"]
            )
        }
    else:
        raise SerializationError("CountTokensInput: no variant present")


def deserialize_json(data: dict) -> CountTokensInput:
    if data.get("invokeModel") is not None:
        import capo_bedrock_runtime.types.invoke_model_tokens_request

        return {
            "invokeModel": capo_bedrock_runtime.types.invoke_model_tokens_request.deserialize_json(
                data["invokeModel"]
            )
        }
    elif data.get("converse") is not None:
        import capo_bedrock_runtime.types.converse_tokens_request

        return {
            "converse": capo_bedrock_runtime.types.converse_tokens_request.deserialize_json(
                data["converse"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CountTokensInput: no recognized variant key")


def redact_sensitive(value: CountTokensInput) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "invokeModel" in value:
        import capo_bedrock_runtime.types.invoke_model_tokens_request

        out["invokeModel"] = (
            capo_bedrock_runtime.types.invoke_model_tokens_request.redact_sensitive(
                value["invokeModel"]
            )
        )
    if "converse" in value:
        import capo_bedrock_runtime.types.converse_tokens_request

        out["converse"] = (
            capo_bedrock_runtime.types.converse_tokens_request.redact_sensitive(
                value["converse"]
            )
        )
    return out
