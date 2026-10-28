"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.embedded_crypto_wallet


class PaymentInstrumentDetailsEmbeddedCryptoWalletMember(TypedDict, closed=True):
    embeddedCryptoWallet: (
        "capo_bedrock_agentcore.types.embedded_crypto_wallet.EmbeddedCryptoWallet"
    )


PaymentInstrumentDetails: TypeAlias = (
    PaymentInstrumentDetailsEmbeddedCryptoWalletMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrumentDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PaymentInstrumentDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "embeddedCryptoWallet" in value:
        import capo_bedrock_agentcore.types.embedded_crypto_wallet

        return {
            "embeddedCryptoWallet": capo_bedrock_agentcore.types.embedded_crypto_wallet.serialize_json(
                value["embeddedCryptoWallet"]
            )
        }
    else:
        raise SerializationError("PaymentInstrumentDetails: no variant present")


def deserialize_json(data: dict) -> PaymentInstrumentDetails:
    if data.get("embeddedCryptoWallet") is not None:
        import capo_bedrock_agentcore.types.embedded_crypto_wallet

        return {
            "embeddedCryptoWallet": capo_bedrock_agentcore.types.embedded_crypto_wallet.deserialize_json(
                data["embeddedCryptoWallet"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PaymentInstrumentDetails: no recognized variant key"
        )


def redact_sensitive(value: PaymentInstrumentDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "embeddedCryptoWallet" in value:
        import capo_bedrock_agentcore.types.embedded_crypto_wallet

        out["embeddedCryptoWallet"] = (
            capo_bedrock_agentcore.types.embedded_crypto_wallet.redact_sensitive(
                value["embeddedCryptoWallet"]
            )
        )
    return out
