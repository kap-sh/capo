"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.crypto_x402_payment_input
    import capo_bedrock_agentcore.types.mpp_payment_input


class _PaymentInput_cryptoX402(TypedDict, closed=True):
    cryptoX402: (
        "capo_bedrock_agentcore.types.crypto_x402_payment_input.CryptoX402PaymentInput"
    )


class _PaymentInput_mpp(TypedDict, closed=True):
    mpp: "capo_bedrock_agentcore.types.mpp_payment_input.MppPaymentInput"


PaymentInput: TypeAlias = (
    _PaymentInput_cryptoX402 | _PaymentInput_mpp | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PaymentInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_input.serialize_json(
                value["cryptoX402"]
            )
        }
    elif "mpp" in value:
        import capo_bedrock_agentcore.types.mpp_payment_input

        return {
            "mpp": capo_bedrock_agentcore.types.mpp_payment_input.serialize_json(
                value["mpp"]
            )
        }
    else:
        raise SerializationError("PaymentInput: no variant present")


def deserialize_json(data: dict) -> PaymentInput:
    if data.get("cryptoX402") is not None:
        import capo_bedrock_agentcore.types.crypto_x402_payment_input

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_input.deserialize_json(
                data["cryptoX402"]
            )
        }
    elif data.get("mpp") is not None:
        import capo_bedrock_agentcore.types.mpp_payment_input

        return {
            "mpp": capo_bedrock_agentcore.types.mpp_payment_input.deserialize_json(
                data["mpp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PaymentInput: no recognized variant key")


def redact_sensitive(value: PaymentInput) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_input

        out["cryptoX402"] = (
            capo_bedrock_agentcore.types.crypto_x402_payment_input.redact_sensitive(
                value["cryptoX402"]
            )
        )
    return out
