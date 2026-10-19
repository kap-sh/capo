"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.s3_location


class _VideoSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _VideoSource_s3Location(TypedDict, closed=True):
    s3Location: "capo_bedrock_runtime.types.s3_location.S3Location"


VideoSource: TypeAlias = (
    _VideoSource_bytes | _VideoSource_s3Location | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VideoSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VideoSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "bytes" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    elif "s3Location" in value:
        import capo_bedrock_runtime.types.s3_location

        return {
            "s3Location": capo_bedrock_runtime.types.s3_location.serialize_json(
                value["s3Location"]
            )
        }
    else:
        raise SerializationError("VideoSource: no variant present")


def deserialize_json(data: dict) -> VideoSource:
    if data.get("bytes") is not None:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    elif data.get("s3Location") is not None:
        import capo_bedrock_runtime.types.s3_location

        return {
            "s3Location": capo_bedrock_runtime.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("VideoSource: no recognized variant key")
