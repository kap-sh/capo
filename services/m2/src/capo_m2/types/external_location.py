"""Generated from Smithy shape ``com.amazonaws.m2#ExternalLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.string2000


class _ExternalLocation_s3Location(TypedDict, closed=True):
    s3Location: "capo_m2.types.string2000.String2000"


ExternalLocation: TypeAlias = _ExternalLocation_s3Location | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ExternalLocation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExternalLocation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    else:
        raise SerializationError("ExternalLocation: no variant present")


def deserialize_json(data: dict) -> ExternalLocation:
    if data.get("s3Location") is not None:
        return {"s3Location": data["s3Location"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExternalLocation: no recognized variant key")
