"""Generated from Smithy shape ``com.amazonaws.securityagent#MemberMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.user_metadata


class _MemberMetadata_user(TypedDict, closed=True):
    user: "capo_securityagent.types.user_metadata.UserMetadata"


MemberMetadata: TypeAlias = _MemberMetadata_user | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MemberMetadata) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MemberMetadata: cannot serialize unknown variant {value.name!r}"
        )
    elif "user" in value:
        import capo_securityagent.types.user_metadata

        return {
            "user": capo_securityagent.types.user_metadata.serialize_json(value["user"])
        }
    else:
        raise SerializationError("MemberMetadata: no variant present")


def deserialize_json(data: dict) -> MemberMetadata:
    if data.get("user") is not None:
        import capo_securityagent.types.user_metadata

        return {
            "user": capo_securityagent.types.user_metadata.deserialize_json(
                data["user"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MemberMetadata: no recognized variant key")
