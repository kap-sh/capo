"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class _GuardrailConverseImageSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


GuardrailConverseImageSource: TypeAlias = (
    _GuardrailConverseImageSource_bytes | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseImageSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GuardrailConverseImageSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "bytes" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("GuardrailConverseImageSource: no variant present")


def deserialize_json(data: dict) -> GuardrailConverseImageSource:
    if data.get("bytes") is not None:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "GuardrailConverseImageSource: no recognized variant key"
        )
