"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type
    import capo_bedrock_agentcore_control.types.secret
    import capo_bedrock_agentcore_control.types.secret_json_key_type
    import capo_bedrock_agentcore_control.types.secret_source_type


class CoinbaseCdpConfigurationOutput(TypedDict, closed=True):
    api_key_id: "capo_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type.CoinbaseCdpApiKeyIdType"
    """<p>The API key identifier provided by Coinbase Developer Platform.</p>"""
    api_key_secret_arn: "capo_bedrock_agentcore_control.types.secret.Secret"
    api_key_secret_json_key: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the API key secret value from the Amazon Web Services Secrets Manager secret.</p>"""
    api_key_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in Amazon Web Services Secrets Manager.</p>"""
    wallet_secret_arn: "capo_bedrock_agentcore_control.types.secret.Secret"
    wallet_secret_json_key: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the wallet secret value from the Amazon Web Services Secrets Manager secret.</p>"""
    wallet_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the wallet secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in Amazon Web Services Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpConfigurationOutput) -> dict:
    out: dict = {}
    out["apiKeyId"] = value["api_key_id"]
    import capo_bedrock_agentcore_control.types.secret

    out["apiKeySecretArn"] = capo_bedrock_agentcore_control.types.secret.serialize_json(
        value["api_key_secret_arn"]
    )
    if "api_key_secret_json_key" in value:
        out["apiKeySecretJsonKey"] = value["api_key_secret_json_key"]
    if "api_key_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["apiKeySecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["api_key_secret_source"]
            )
        )
    import capo_bedrock_agentcore_control.types.secret

    out["walletSecretArn"] = capo_bedrock_agentcore_control.types.secret.serialize_json(
        value["wallet_secret_arn"]
    )
    if "wallet_secret_json_key" in value:
        out["walletSecretJsonKey"] = value["wallet_secret_json_key"]
    if "wallet_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["walletSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["wallet_secret_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoinbaseCdpConfigurationOutput:
    out: CoinbaseCdpConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("apiKeyId") is not None:
        out["api_key_id"] = data["apiKeyId"]
    else:
        out["api_key_id"] = ""
    if data.get("apiKeySecretArn") is not None:
        import capo_bedrock_agentcore_control.types.secret

        out["api_key_secret_arn"] = (
            capo_bedrock_agentcore_control.types.secret.deserialize_json(
                data["apiKeySecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "CoinbaseCdpConfigurationOutput.api_key_secret_arn required"
        )
    if data.get("apiKeySecretJsonKey") is not None:
        out["api_key_secret_json_key"] = data["apiKeySecretJsonKey"]
    if data.get("apiKeySecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["api_key_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["apiKeySecretSource"]
            )
        )
    if data.get("walletSecretArn") is not None:
        import capo_bedrock_agentcore_control.types.secret

        out["wallet_secret_arn"] = (
            capo_bedrock_agentcore_control.types.secret.deserialize_json(
                data["walletSecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "CoinbaseCdpConfigurationOutput.wallet_secret_arn required"
        )
    if data.get("walletSecretJsonKey") is not None:
        out["wallet_secret_json_key"] = data["walletSecretJsonKey"]
    if data.get("walletSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["wallet_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["walletSecretSource"]
            )
        )
    return out
