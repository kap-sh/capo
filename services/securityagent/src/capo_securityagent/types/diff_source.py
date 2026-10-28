"""Generated from Smithy shape ``com.amazonaws.securityagent#DiffSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember


class DiffSourceS3UriMember(TypedDict, closed=True):
    s3Uri: "str"


DiffSource: TypeAlias = DiffSourceS3UriMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: DiffSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DiffSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("DiffSource: no variant present")


def deserialize_json(data: dict) -> DiffSource:
    if data.get("s3Uri") is not None:
        return {"s3Uri": data["s3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DiffSource: no recognized variant key")
