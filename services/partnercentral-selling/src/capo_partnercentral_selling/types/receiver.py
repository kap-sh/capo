"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Receiver``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError
from capo_partnercentral_selling.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.account_receiver


class _Receiver_Account(TypedDict, closed=True):
    Account: "capo_partnercentral_selling.types.account_receiver.AccountReceiver"


Receiver: TypeAlias = _Receiver_Account | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Receiver) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Receiver: cannot serialize unknown variant {value.name!r}"
        )
    elif "Account" in value:
        import capo_partnercentral_selling.types.account_receiver

        return {
            "Account": capo_partnercentral_selling.types.account_receiver.serialize_aws_json_1_0(
                value["Account"]
            )
        }
    else:
        raise SerializationError("Receiver: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Receiver:
    if data.get("Account") is not None:
        import capo_partnercentral_selling.types.account_receiver

        return {
            "Account": capo_partnercentral_selling.types.account_receiver.deserialize_aws_json_1_0(
                data["Account"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Receiver: no recognized variant key")


def redact_sensitive(value: Receiver) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "Account" in value:
        import capo_partnercentral_selling.types.account_receiver

        out["Account"] = (
            capo_partnercentral_selling.types.account_receiver.redact_sensitive(
                value["Account"]
            )
        )
    return out
