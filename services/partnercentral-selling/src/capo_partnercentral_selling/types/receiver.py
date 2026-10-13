"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Receiver``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.account_receiver


class _Receiver_Account(TypedDict, closed=True):
    Account: "capo_partnercentral_selling.types.account_receiver.AccountReceiver"


Receiver: TypeAlias = _Receiver_Account


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Receiver) -> dict:
    if "Account" in value:
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
        raise DeserializationError("Receiver: no recognized variant key")


def redact_sensitive(value: Receiver) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Account" in value:
        import capo_partnercentral_selling.types.account_receiver

        out["Account"] = (
            capo_partnercentral_selling.types.account_receiver.redact_sensitive(
                value["Account"]
            )
        )
    return out
