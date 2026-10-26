"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentityCenterPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.group_id
    import capo_account_access.types.user_id


class _IdentityCenterPrincipal_userId(TypedDict, closed=True):
    userId: "capo_account_access.types.user_id.UserId"


class _IdentityCenterPrincipal_groupId(TypedDict, closed=True):
    groupId: "capo_account_access.types.group_id.GroupId"


IdentityCenterPrincipal: TypeAlias = (
    _IdentityCenterPrincipal_userId
    | _IdentityCenterPrincipal_groupId
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterPrincipal) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IdentityCenterPrincipal: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "userId" in value:
        return {"userId": value["userId"]}
    elif "groupId" in value:
        return {"groupId": value["groupId"]}
    else:
        raise SerializationError("IdentityCenterPrincipal: no variant present")


def deserialize_json(data: dict) -> IdentityCenterPrincipal:
    if data.get("userId") is not None:
        return {"userId": data["userId"]}
    elif data.get("groupId") is not None:
        return {"groupId": data["groupId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IdentityCenterPrincipal: no recognized variant key")
