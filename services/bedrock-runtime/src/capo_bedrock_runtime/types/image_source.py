"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.s3_location


class _ImageSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _ImageSource_s3Location(TypedDict, closed=True):
    s3Location: "capo_bedrock_runtime.types.s3_location.S3Location"


ImageSource: TypeAlias = (
    _ImageSource_bytes | _ImageSource_s3Location | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ImageSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ImageSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
        raise SerializationError("ImageSource: no variant present")


def deserialize_json(data: dict) -> ImageSource:
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("ImageSource: no recognized variant key")
