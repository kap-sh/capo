"""Generated from Smithy shape ``com.amazonaws.identitystore#MemberId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError, SerializationError
from capo_identitystore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_identitystore.types.resource_id


class _MemberId_UserId(TypedDict, closed=True):
    UserId: "capo_identitystore.types.resource_id.ResourceId"


MemberId: TypeAlias = _MemberId_UserId | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberId) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MemberId: cannot serialize unknown variant {value.name!r}"
        )
    elif "UserId" in value:
        return {"UserId": value["UserId"]}
    else:
        raise SerializationError("MemberId: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MemberId:
    if data.get("UserId") is not None:
        return {"UserId": data["UserId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MemberId: no recognized variant key")
