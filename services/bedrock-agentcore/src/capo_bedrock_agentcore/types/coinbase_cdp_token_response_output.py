"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CoinbaseCdpTokenResponseOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type


class CoinbaseCdpTokenResponseOutput(TypedDict, closed=True):
    bearer_token: "capo_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type.CoinbaseCdpPaymentJwtTokenType"
    """<p>Bearer Token for Authorization header.</p>"""
    wallet_auth_token: NotRequired[
        "capo_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type.CoinbaseCdpPaymentJwtTokenType"
    ]
    """<p>Wallet Auth Token for X-Wallet-Auth header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpTokenResponseOutput) -> dict:
    out: dict = {}
    out["bearerToken"] = value["bearer_token"]
    if "wallet_auth_token" in value:
        out["walletAuthToken"] = value["wallet_auth_token"]
    return out


def deserialize_json(data: dict) -> CoinbaseCdpTokenResponseOutput:
    out: CoinbaseCdpTokenResponseOutput = {}  # type: ignore[typeddict-item]
    if data.get("bearerToken") is not None:
        out["bearer_token"] = data["bearerToken"]
    else:
        raise DeserializationError(
            "CoinbaseCdpTokenResponseOutput.bearer_token required"
        )
    if data.get("walletAuthToken") is not None:
        out["wallet_auth_token"] = data["walletAuthToken"]
    return out


def redact_sensitive(value: CoinbaseCdpTokenResponseOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bearer_token" in value:
        out["bearer_token"] = "*** Sensitive Data Redacted ***"
    if "wallet_auth_token" in value:
        out["wallet_auth_token"] = "*** Sensitive Data Redacted ***"
    return out
