"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EmbeddedCryptoWallet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.crypto_wallet_network
    import capo_bedrock_agentcore.types.linked_account_list


class EmbeddedCryptoWallet(TypedDict, closed=True):
    network: "capo_bedrock_agentcore.types.crypto_wallet_network.CryptoWalletNetwork"
    """<p>The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.</p>"""
    linked_accounts: (
        "capo_bedrock_agentcore.types.linked_account_list.LinkedAccountList"
    )
    """<p>List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.</p>"""
    wallet_address: NotRequired["str"]
    """<p>The wallet address on the specified blockchain network.</p>"""
    redirect_url: NotRequired["str"]
    """<p>URL for the end user to complete a provider-specific action such as wallet linking or onboarding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedCryptoWallet) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.crypto_wallet_network

    out["network"] = capo_bedrock_agentcore.types.crypto_wallet_network.serialize_json(
        value["network"]
    )
    import capo_bedrock_agentcore.types.linked_account_list

    out["linkedAccounts"] = (
        capo_bedrock_agentcore.types.linked_account_list.serialize_json(
            value["linked_accounts"]
        )
    )
    if "wallet_address" in value:
        out["walletAddress"] = value["wallet_address"]
    if "redirect_url" in value:
        out["redirectUrl"] = value["redirect_url"]
    return out


def deserialize_json(data: dict) -> EmbeddedCryptoWallet:
    out: EmbeddedCryptoWallet = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        import capo_bedrock_agentcore.types.crypto_wallet_network

        out["network"] = (
            capo_bedrock_agentcore.types.crypto_wallet_network.deserialize_json(
                data["network"]
            )
        )
    else:
        raise DeserializationError("EmbeddedCryptoWallet.network required")
    if data.get("linkedAccounts") is not None:
        import capo_bedrock_agentcore.types.linked_account_list

        out["linked_accounts"] = (
            capo_bedrock_agentcore.types.linked_account_list.deserialize_json(
                data["linkedAccounts"]
            )
        )
    else:
        raise DeserializationError("EmbeddedCryptoWallet.linked_accounts required")
    if data.get("walletAddress") is not None:
        out["wallet_address"] = data["walletAddress"]
    if data.get("redirectUrl") is not None:
        out["redirect_url"] = data["redirectUrl"]
    return out


def redact_sensitive(value: EmbeddedCryptoWallet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "linked_accounts" in value:
        import capo_bedrock_agentcore.types.linked_account_list

        out["linked_accounts"] = (
            capo_bedrock_agentcore.types.linked_account_list.redact_sensitive(
                value["linked_accounts"]
            )
        )
    return out
