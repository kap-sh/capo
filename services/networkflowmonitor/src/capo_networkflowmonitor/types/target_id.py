"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_networkflowmonitor.errors import DeserializationError, SerializationError
from capo_networkflowmonitor.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.account_id


class _TargetId_accountId(TypedDict, closed=True):
    accountId: "capo_networkflowmonitor.types.account_id.AccountId"


TargetId: TypeAlias = _TargetId_accountId | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TargetId) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TargetId: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accountId" in value:
        return {"accountId": value["accountId"]}
    else:
        raise SerializationError("TargetId: no variant present")


def deserialize_json(data: dict) -> TargetId:
    if data.get("accountId") is not None:
        return {"accountId": data["accountId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TargetId: no recognized variant key")
