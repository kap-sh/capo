"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentOutput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.crypto_x402_payment_output
    import capo_bedrock_agentcore.types.mpp_payment_output


class _PaymentOutput_cryptoX402(TypedDict, closed=True):
    cryptoX402: "capo_bedrock_agentcore.types.crypto_x402_payment_output.CryptoX402PaymentOutput"


class _PaymentOutput_mpp(TypedDict, closed=True):
    mpp: "capo_bedrock_agentcore.types.mpp_payment_output.MppPaymentOutput"


PaymentOutput: TypeAlias = (
    _PaymentOutput_cryptoX402 | _PaymentOutput_mpp | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PaymentOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_output

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_output.serialize_json(
                value["cryptoX402"]
            )
        }
    elif "mpp" in value:
        import capo_bedrock_agentcore.types.mpp_payment_output

        return {
            "mpp": capo_bedrock_agentcore.types.mpp_payment_output.serialize_json(
                value["mpp"]
            )
        }
    else:
        raise SerializationError("PaymentOutput: no variant present")


def deserialize_json(data: dict) -> PaymentOutput:
    if data.get("cryptoX402") is not None:
        import capo_bedrock_agentcore.types.crypto_x402_payment_output

        return {
            "cryptoX402": capo_bedrock_agentcore.types.crypto_x402_payment_output.deserialize_json(
                data["cryptoX402"]
            )
        }
    elif data.get("mpp") is not None:
        import capo_bedrock_agentcore.types.mpp_payment_output

        return {
            "mpp": capo_bedrock_agentcore.types.mpp_payment_output.deserialize_json(
                data["mpp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PaymentOutput: no recognized variant key")


def redact_sensitive(value: PaymentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cryptoX402" in value:
        import capo_bedrock_agentcore.types.crypto_x402_payment_output

        out["cryptoX402"] = (
            capo_bedrock_agentcore.types.crypto_x402_payment_output.redact_sensitive(
                value["cryptoX402"]
            )
        )
    if "mpp" in value:
        import capo_bedrock_agentcore.types.mpp_payment_output

        out["mpp"] = capo_bedrock_agentcore.types.mpp_payment_output.redact_sensitive(
            value["mpp"]
        )
    return out
