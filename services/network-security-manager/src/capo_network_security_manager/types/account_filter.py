"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AccountFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_set


class _AccountFilter_includeAll(TypedDict, closed=True):
    includeAll: "None"


class _AccountFilter_include(TypedDict, closed=True):
    include: "capo_network_security_manager.types.account_set.AccountSet"


class _AccountFilter_exclude(TypedDict, closed=True):
    exclude: "capo_network_security_manager.types.account_set.AccountSet"


AccountFilter: TypeAlias = (
    _AccountFilter_includeAll
    | _AccountFilter_include
    | _AccountFilter_exclude
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AccountFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AccountFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "includeAll" in value:
        return {"includeAll": {}}
    elif "include" in value:
        import capo_network_security_manager.types.account_set

        return {
            "include": capo_network_security_manager.types.account_set.serialize_json(
                value["include"]
            )
        }
    elif "exclude" in value:
        import capo_network_security_manager.types.account_set

        return {
            "exclude": capo_network_security_manager.types.account_set.serialize_json(
                value["exclude"]
            )
        }
    else:
        raise SerializationError("AccountFilter: no variant present")


def deserialize_json(data: dict) -> AccountFilter:
    if data.get("includeAll") is not None:
        return {"includeAll": None}
    elif data.get("include") is not None:
        import capo_network_security_manager.types.account_set

        return {
            "include": capo_network_security_manager.types.account_set.deserialize_json(
                data["include"]
            )
        }
    elif data.get("exclude") is not None:
        import capo_network_security_manager.types.account_set

        return {
            "exclude": capo_network_security_manager.types.account_set.deserialize_json(
                data["exclude"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AccountFilter: no recognized variant key")
