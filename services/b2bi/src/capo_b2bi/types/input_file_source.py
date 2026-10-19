"""Generated from Smithy shape ``com.amazonaws.b2bi#InputFileSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember


class _InputFileSource_fileContent(TypedDict, closed=True):
    fileContent: "str"


InputFileSource: TypeAlias = _InputFileSource_fileContent | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputFileSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"InputFileSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "fileContent" in value:
        return {"fileContent": value["fileContent"]}
    else:
        raise SerializationError("InputFileSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> InputFileSource:
    if data.get("fileContent") is not None:
        return {"fileContent": data["fileContent"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("InputFileSource: no recognized variant key")
