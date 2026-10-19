"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.document_content_blocks
    import capo_bedrock_runtime.types.s3_location


class _DocumentSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _DocumentSource_s3Location(TypedDict, closed=True):
    s3Location: "capo_bedrock_runtime.types.s3_location.S3Location"


class _DocumentSource_text(TypedDict, closed=True):
    text: "str"


class _DocumentSource_content(TypedDict, closed=True):
    content: "capo_bedrock_runtime.types.document_content_blocks.DocumentContentBlocks"


DocumentSource: TypeAlias = (
    _DocumentSource_bytes
    | _DocumentSource_s3Location
    | _DocumentSource_text
    | _DocumentSource_content
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DocumentSource: cannot serialize unknown variant {value.name!r}"
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
    elif "text" in value:
        return {"text": value["text"]}
    elif "content" in value:
        import capo_bedrock_runtime.types.document_content_blocks

        return {
            "content": capo_bedrock_runtime.types.document_content_blocks.serialize_json(
                value["content"]
            )
        }
    else:
        raise SerializationError("DocumentSource: no variant present")


def deserialize_json(data: dict) -> DocumentSource:
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
    elif data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("content") is not None:
        import capo_bedrock_runtime.types.document_content_blocks

        return {
            "content": capo_bedrock_runtime.types.document_content_blocks.deserialize_json(
                data["content"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DocumentSource: no recognized variant key")
