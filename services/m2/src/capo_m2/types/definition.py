"""Generated from Smithy shape ``com.amazonaws.m2#Definition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.string2000
    import capo_m2.types.string_free65000


class _Definition_s3Location(TypedDict, closed=True):
    s3Location: "capo_m2.types.string2000.String2000"


class _Definition_content(TypedDict, closed=True):
    content: "capo_m2.types.string_free65000.StringFree65000"


Definition: TypeAlias = (
    _Definition_s3Location | _Definition_content | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Definition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Definition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError("Definition: no variant present")


def deserialize_json(data: dict) -> Definition:
    if data.get("s3Location") is not None:
        return {"s3Location": data["s3Location"]}
    elif data.get("content") is not None:
        return {"content": data["content"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Definition: no recognized variant key")
