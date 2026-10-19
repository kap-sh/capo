"""Generated from Smithy shape ``com.amazonaws.datazone#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.s3_permissions


class _Permissions_s3(TypedDict, closed=True):
    s3: "capo_datazone.types.s3_permissions.S3Permissions"


Permissions: TypeAlias = _Permissions_s3 | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Permissions) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Permissions: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3" in value:
        import capo_datazone.types.s3_permissions

        return {"s3": capo_datazone.types.s3_permissions.serialize_json(value["s3"])}
    else:
        raise SerializationError("Permissions: no variant present")


def deserialize_json(data: dict) -> Permissions:
    if data.get("s3") is not None:
        import capo_datazone.types.s3_permissions

        return {"s3": capo_datazone.types.s3_permissions.deserialize_json(data["s3"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Permissions: no recognized variant key")
