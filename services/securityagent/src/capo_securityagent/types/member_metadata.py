"""Generated from Smithy shape ``com.amazonaws.securityagent#MemberMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.group_metadata
    import capo_securityagent.types.user_metadata


class MemberMetadataUserMember(TypedDict, closed=True):
    user: "capo_securityagent.types.user_metadata.UserMetadata"


class MemberMetadataGroupMember(TypedDict, closed=True):
    group: "capo_securityagent.types.group_metadata.GroupMetadata"


MemberMetadata: TypeAlias = (
    MemberMetadataUserMember | MemberMetadataGroupMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemberMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemberMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        import capo_securityagent.types.user_metadata

        return {
            "user": capo_securityagent.types.user_metadata.serialize_json(value["user"])
        }
    elif "group" in value:
        import capo_securityagent.types.group_metadata

        return {
            "group": capo_securityagent.types.group_metadata.serialize_json(
                value["group"]
            )
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
    elif data.get("group") is not None:
        import capo_securityagent.types.group_metadata

        return {
            "group": capo_securityagent.types.group_metadata.deserialize_json(
                data["group"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MemberMetadata: no recognized variant key")
