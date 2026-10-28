"""Generated from Smithy shape ``com.amazonaws.datazone#AccountSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.account_info_list
    import capo_datazone.types.custom_account_pool_handler


class AccountSourceAccountsMember(TypedDict, closed=True):
    accounts: "capo_datazone.types.account_info_list.AccountInfoList"


class AccountSourceCustomAccountPoolHandlerMember(TypedDict, closed=True):
    customAccountPoolHandler: (
        "capo_datazone.types.custom_account_pool_handler.CustomAccountPoolHandler"
    )


AccountSource: TypeAlias = (
    AccountSourceAccountsMember
    | AccountSourceCustomAccountPoolHandlerMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AccountSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AccountSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accounts" in value:
        import capo_datazone.types.account_info_list

        return {
            "accounts": capo_datazone.types.account_info_list.serialize_json(
                value["accounts"]
            )
        }
    elif "customAccountPoolHandler" in value:
        import capo_datazone.types.custom_account_pool_handler

        return {
            "customAccountPoolHandler": capo_datazone.types.custom_account_pool_handler.serialize_json(
                value["customAccountPoolHandler"]
            )
        }
    else:
        raise SerializationError("AccountSource: no variant present")


def deserialize_json(data: dict) -> AccountSource:
    if data.get("accounts") is not None:
        import capo_datazone.types.account_info_list

        return {
            "accounts": capo_datazone.types.account_info_list.deserialize_json(
                data["accounts"]
            )
        }
    elif data.get("customAccountPoolHandler") is not None:
        import capo_datazone.types.custom_account_pool_handler

        return {
            "customAccountPoolHandler": capo_datazone.types.custom_account_pool_handler.deserialize_json(
                data["customAccountPoolHandler"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AccountSource: no recognized variant key")


def redact_sensitive(value: AccountSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accounts" in value:
        import capo_datazone.types.account_info_list

        out["accounts"] = capo_datazone.types.account_info_list.redact_sensitive(
            value["accounts"]
        )
    return out
