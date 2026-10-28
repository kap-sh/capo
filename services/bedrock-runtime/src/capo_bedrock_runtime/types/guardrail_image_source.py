"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class GuardrailImageSourceBytesMember(TypedDict, closed=True):
    bytes: "bytes"


GuardrailImageSource: TypeAlias = GuardrailImageSourceBytesMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GuardrailImageSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "bytes" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("GuardrailImageSource: no variant present")


def deserialize_json(data: dict) -> GuardrailImageSource:
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("GuardrailImageSource: no recognized variant key")
