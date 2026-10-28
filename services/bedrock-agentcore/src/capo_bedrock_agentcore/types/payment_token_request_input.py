"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentTokenRequestInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.coinbase_cdp_token_request_input
    import capo_bedrock_agentcore.types.stripe_privy_token_request_input


class PaymentTokenRequestInputCoinbaseCdpTokenRequestMember(TypedDict, closed=True):
    coinbaseCdpTokenRequest: "capo_bedrock_agentcore.types.coinbase_cdp_token_request_input.CoinbaseCdpTokenRequestInput"


class PaymentTokenRequestInputStripePrivyTokenRequestMember(TypedDict, closed=True):
    stripePrivyTokenRequest: "capo_bedrock_agentcore.types.stripe_privy_token_request_input.StripePrivyTokenRequestInput"


PaymentTokenRequestInput: TypeAlias = (
    PaymentTokenRequestInputCoinbaseCdpTokenRequestMember
    | PaymentTokenRequestInputStripePrivyTokenRequestMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTokenRequestInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PaymentTokenRequestInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "coinbaseCdpTokenRequest" in value:
        import capo_bedrock_agentcore.types.coinbase_cdp_token_request_input

        return {
            "coinbaseCdpTokenRequest": capo_bedrock_agentcore.types.coinbase_cdp_token_request_input.serialize_json(
                value["coinbaseCdpTokenRequest"]
            )
        }
    elif "stripePrivyTokenRequest" in value:
        import capo_bedrock_agentcore.types.stripe_privy_token_request_input

        return {
            "stripePrivyTokenRequest": capo_bedrock_agentcore.types.stripe_privy_token_request_input.serialize_json(
                value["stripePrivyTokenRequest"]
            )
        }
    else:
        raise SerializationError("PaymentTokenRequestInput: no variant present")


def deserialize_json(data: dict) -> PaymentTokenRequestInput:
    if data.get("coinbaseCdpTokenRequest") is not None:
        import capo_bedrock_agentcore.types.coinbase_cdp_token_request_input

        return {
            "coinbaseCdpTokenRequest": capo_bedrock_agentcore.types.coinbase_cdp_token_request_input.deserialize_json(
                data["coinbaseCdpTokenRequest"]
            )
        }
    elif data.get("stripePrivyTokenRequest") is not None:
        import capo_bedrock_agentcore.types.stripe_privy_token_request_input

        return {
            "stripePrivyTokenRequest": capo_bedrock_agentcore.types.stripe_privy_token_request_input.deserialize_json(
                data["stripePrivyTokenRequest"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PaymentTokenRequestInput: no recognized variant key"
        )


def redact_sensitive(value: PaymentTokenRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stripePrivyTokenRequest" in value:
        import capo_bedrock_agentcore.types.stripe_privy_token_request_input

        out["stripePrivyTokenRequest"] = (
            capo_bedrock_agentcore.types.stripe_privy_token_request_input.redact_sensitive(
                value["stripePrivyTokenRequest"]
            )
        )
    return out
