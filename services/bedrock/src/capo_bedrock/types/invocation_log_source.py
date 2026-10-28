"""Generated from Smithy shape ``com.amazonaws.bedrock#InvocationLogSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri


class InvocationLogSourceS3UriMember(TypedDict, closed=True):
    s3Uri: "capo_bedrock.types.s3_uri.S3Uri"


InvocationLogSource: TypeAlias = InvocationLogSourceS3UriMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: InvocationLogSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InvocationLogSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("InvocationLogSource: no variant present")


def deserialize_json(data: dict) -> InvocationLogSource:
    if data.get("s3Uri") is not None:
        return {"s3Uri": data["s3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("InvocationLogSource: no recognized variant key")
