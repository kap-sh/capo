"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentTokenResponseOutput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.coinbase_cdp_token_response_output
    import capo_bedrock_agentcore.types.stripe_privy_token_response_output


class _PaymentTokenResponseOutput_coinbaseCdpTokenResponse(TypedDict, closed=True):
    coinbaseCdpTokenResponse: "capo_bedrock_agentcore.types.coinbase_cdp_token_response_output.CoinbaseCdpTokenResponseOutput"


class _PaymentTokenResponseOutput_stripePrivyTokenResponse(TypedDict, closed=True):
    stripePrivyTokenResponse: "capo_bedrock_agentcore.types.stripe_privy_token_response_output.StripePrivyTokenResponseOutput"


PaymentTokenResponseOutput: TypeAlias = (
    _PaymentTokenResponseOutput_coinbaseCdpTokenResponse
    | _PaymentTokenResponseOutput_stripePrivyTokenResponse
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTokenResponseOutput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PaymentTokenResponseOutput: cannot serialize unknown variant {value.name!r}"
        )
    elif "coinbaseCdpTokenResponse" in value:
        import capo_bedrock_agentcore.types.coinbase_cdp_token_response_output

        return {
            "coinbaseCdpTokenResponse": capo_bedrock_agentcore.types.coinbase_cdp_token_response_output.serialize_json(
                value["coinbaseCdpTokenResponse"]
            )
        }
    elif "stripePrivyTokenResponse" in value:
        import capo_bedrock_agentcore.types.stripe_privy_token_response_output

        return {
            "stripePrivyTokenResponse": capo_bedrock_agentcore.types.stripe_privy_token_response_output.serialize_json(
                value["stripePrivyTokenResponse"]
            )
        }
    else:
        raise SerializationError("PaymentTokenResponseOutput: no variant present")


def deserialize_json(data: dict) -> PaymentTokenResponseOutput:
    if data.get("coinbaseCdpTokenResponse") is not None:
        import capo_bedrock_agentcore.types.coinbase_cdp_token_response_output

        return {
            "coinbaseCdpTokenResponse": capo_bedrock_agentcore.types.coinbase_cdp_token_response_output.deserialize_json(
                data["coinbaseCdpTokenResponse"]
            )
        }
    elif data.get("stripePrivyTokenResponse") is not None:
        import capo_bedrock_agentcore.types.stripe_privy_token_response_output

        return {
            "stripePrivyTokenResponse": capo_bedrock_agentcore.types.stripe_privy_token_response_output.deserialize_json(
                data["stripePrivyTokenResponse"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "PaymentTokenResponseOutput: no recognized variant key"
        )


def redact_sensitive(
    value: PaymentTokenResponseOutput,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "coinbaseCdpTokenResponse" in value:
        import capo_bedrock_agentcore.types.coinbase_cdp_token_response_output

        out["coinbaseCdpTokenResponse"] = (
            capo_bedrock_agentcore.types.coinbase_cdp_token_response_output.redact_sensitive(
                value["coinbaseCdpTokenResponse"]
            )
        )
    if "stripePrivyTokenResponse" in value:
        import capo_bedrock_agentcore.types.stripe_privy_token_response_output

        out["stripePrivyTokenResponse"] = (
            capo_bedrock_agentcore.types.stripe_privy_token_response_output.redact_sensitive(
                value["stripePrivyTokenResponse"]
            )
        )
    return out
