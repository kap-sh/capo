"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.group_identifier
    import capo_qbusiness.types.user_identifier


class SubscriptionPrincipalUserMember(TypedDict, closed=True):
    user: "capo_qbusiness.types.user_identifier.UserIdentifier"


class SubscriptionPrincipalGroupMember(TypedDict, closed=True):
    group: "capo_qbusiness.types.group_identifier.GroupIdentifier"


SubscriptionPrincipal: TypeAlias = (
    SubscriptionPrincipalUserMember
    | SubscriptionPrincipalGroupMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionPrincipal) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SubscriptionPrincipal: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        return {"user": value["user"]}
    elif "group" in value:
        return {"group": value["group"]}
    else:
        raise SerializationError("SubscriptionPrincipal: no variant present")


def deserialize_json(data: dict) -> SubscriptionPrincipal:
    if data.get("user") is not None:
        return {"user": data["user"]}
    elif data.get("group") is not None:
        return {"group": data["group"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SubscriptionPrincipal: no recognized variant key")
