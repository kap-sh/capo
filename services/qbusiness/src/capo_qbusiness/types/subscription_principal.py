"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.group_identifier
    import capo_qbusiness.types.user_identifier


class _SubscriptionPrincipal_user(TypedDict, closed=True):
    user: "capo_qbusiness.types.user_identifier.UserIdentifier"


class _SubscriptionPrincipal_group(TypedDict, closed=True):
    group: "capo_qbusiness.types.group_identifier.GroupIdentifier"


SubscriptionPrincipal: TypeAlias = (
    _SubscriptionPrincipal_user | _SubscriptionPrincipal_group | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionPrincipal) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SubscriptionPrincipal: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError("SubscriptionPrincipal: no recognized variant key")
