"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class _ImageInputSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


ImageInputSource: TypeAlias = _ImageInputSource_bytes | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ImageInputSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ImageInputSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "bytes" in value:
        import capo_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_agent_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("ImageInputSource: no variant present")


def deserialize_json(data: dict) -> ImageInputSource:
    if data.get("bytes") is not None:
        import capo_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_agent_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ImageInputSource: no recognized variant key")
