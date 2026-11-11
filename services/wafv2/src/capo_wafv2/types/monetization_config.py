"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_configs
    import capo_wafv2.types.crypto_config
    import capo_wafv2.types.currency_mode


class MonetizationConfig(TypedDict, closed=True):
    crypto_config: NotRequired["capo_wafv2.types.crypto_config.CryptoConfig"]
    """<p>The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.</p>"""
    connected_account_configs: NotRequired[
        "capo_wafv2.types.connected_account_configs.ConnectedAccountConfigs"
    ]
    """<p>The connected account configurations for settling AI bot payments through a connected account with a supported third-party payment provider (Stripe), as an alternative to the self-managed wallets in <code>CryptoConfig</code>. You can provide <code>CryptoConfig</code>, <code>ConnectedAccountConfigs</code>, or both; however, a given blockchain network (chain) can be used by only one of them. Currently supports exactly one connected account.</p>"""
    currency_mode: NotRequired["capo_wafv2.types.currency_mode.CurrencyMode"]
    """<p>Specifies whether the configuration uses real or test currency. If not specified, defaults to <code>REAL</code>. Connected account configurations support production settlement only; <code>TEST</code> is not supported when <code>ConnectedAccountConfigs</code> is present.</p> <p>Valid values:</p> <ul> <li> <p> <code>REAL</code> - Settle payments in USDC on production blockchain networks (Base, Solana).</p> </li> <li> <p> <code>TEST</code> - Settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizationConfig) -> dict:
    out: dict = {}
    if "crypto_config" in value:
        import capo_wafv2.types.crypto_config

        out["CryptoConfig"] = capo_wafv2.types.crypto_config.serialize_aws_json_1_1(
            value["crypto_config"]
        )
    if "connected_account_configs" in value:
        import capo_wafv2.types.connected_account_configs

        out["ConnectedAccountConfigs"] = (
            capo_wafv2.types.connected_account_configs.serialize_aws_json_1_1(
                value["connected_account_configs"]
            )
        )
    if "currency_mode" in value:
        import capo_wafv2.types.currency_mode

        out["CurrencyMode"] = capo_wafv2.types.currency_mode.serialize_aws_json_1_1(
            value["currency_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonetizationConfig:
    out: MonetizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("CryptoConfig") is not None:
        import capo_wafv2.types.crypto_config

        out["crypto_config"] = capo_wafv2.types.crypto_config.deserialize_aws_json_1_1(
            data["CryptoConfig"]
        )
    if data.get("ConnectedAccountConfigs") is not None:
        import capo_wafv2.types.connected_account_configs

        out["connected_account_configs"] = (
            capo_wafv2.types.connected_account_configs.deserialize_aws_json_1_1(
                data["ConnectedAccountConfigs"]
            )
        )
    if data.get("CurrencyMode") is not None:
        import capo_wafv2.types.currency_mode

        out["currency_mode"] = capo_wafv2.types.currency_mode.deserialize_aws_json_1_1(
            data["CurrencyMode"]
        )
    return out
