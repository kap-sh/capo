"""Generated from Smithy shape ``com.amazonaws.datazone#MemberDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.group_details
    import capo_datazone.types.user_details


class MemberDetailsUserMember(TypedDict, closed=True):
    user: "capo_datazone.types.user_details.UserDetails"


class MemberDetailsGroupMember(TypedDict, closed=True):
    group: "capo_datazone.types.group_details.GroupDetails"


MemberDetails: TypeAlias = (
    MemberDetailsUserMember | MemberDetailsGroupMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemberDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemberDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        import capo_datazone.types.user_details

        return {"user": capo_datazone.types.user_details.serialize_json(value["user"])}
    elif "group" in value:
        import capo_datazone.types.group_details

        return {
            "group": capo_datazone.types.group_details.serialize_json(value["group"])
        }
    else:
        raise SerializationError("MemberDetails: no variant present")


def deserialize_json(data: dict) -> MemberDetails:
    if data.get("user") is not None:
        import capo_datazone.types.user_details

        return {"user": capo_datazone.types.user_details.deserialize_json(data["user"])}
    elif data.get("group") is not None:
        import capo_datazone.types.group_details

        return {
            "group": capo_datazone.types.group_details.deserialize_json(data["group"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MemberDetails: no recognized variant key")
