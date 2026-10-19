"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type
    import capo_bedrock_agentcore_control.types.default_coinbase_cdp_api_key_secret_type
    import capo_bedrock_agentcore_control.types.default_coinbase_cdp_wallet_secret_type
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type


class CoinbaseCdpConfigurationInput(TypedDict, closed=True):
    api_key_id: "capo_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type.CoinbaseCdpApiKeyIdType"
    """<p>The API key identifier provided by Coinbase Developer Platform.</p>"""
    api_key_secret: "capo_bedrock_agentcore_control.types.default_coinbase_cdp_api_key_secret_type.DefaultCoinbaseCdpApiKeySecretType"
    """<p>The API key secret provided by Coinbase Developer Platform.</p>"""
    api_key_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret for the Coinbase Developer Platform. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    api_key_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key secret. This includes the secret ID and the JSON key used to extract the API key secret value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    wallet_secret: "capo_bedrock_agentcore_control.types.default_coinbase_cdp_wallet_secret_type.DefaultCoinbaseCdpWalletSecretType"
    """<p>The wallet secret provided by Coinbase Developer Platform.</p>"""
    wallet_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the wallet secret for the Coinbase Developer Platform. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    wallet_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the wallet secret. This includes the secret ID and the JSON key used to extract the wallet secret value from the secret. Required when <code>walletSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpConfigurationInput) -> dict:
    out: dict = {}
    out["apiKeyId"] = value["api_key_id"]
    out["apiKeySecret"] = value.get("api_key_secret", "")
    if "api_key_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["apiKeySecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["api_key_secret_source"]
            )
        )
    if "api_key_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["apiKeySecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["api_key_secret_config"]
            )
        )
    out["walletSecret"] = value.get("wallet_secret", "")
    if "wallet_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["walletSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["wallet_secret_source"]
            )
        )
    if "wallet_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["walletSecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["wallet_secret_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoinbaseCdpConfigurationInput:
    out: CoinbaseCdpConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("apiKeyId") is not None:
        out["api_key_id"] = data["apiKeyId"]
    else:
        out["api_key_id"] = ""
    if data.get("apiKeySecret") is not None:
        out["api_key_secret"] = data["apiKeySecret"]
    else:
        out["api_key_secret"] = ""
    if data.get("apiKeySecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["api_key_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["apiKeySecretSource"]
            )
        )
    if data.get("apiKeySecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["api_key_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["apiKeySecretConfig"]
            )
        )
    if data.get("walletSecret") is not None:
        out["wallet_secret"] = data["walletSecret"]
    else:
        out["wallet_secret"] = ""
    if data.get("walletSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["wallet_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["walletSecretSource"]
            )
        )
    if data.get("walletSecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["wallet_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["walletSecretConfig"]
            )
        )
    return out


def redact_sensitive(value: CoinbaseCdpConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key_secret" in value:
        out["api_key_secret"] = "*** Sensitive Data Redacted ***"
    if "wallet_secret" in value:
        out["wallet_secret"] = "*** Sensitive Data Redacted ***"
    return out
