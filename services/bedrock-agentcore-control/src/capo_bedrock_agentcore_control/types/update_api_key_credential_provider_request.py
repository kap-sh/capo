"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateApiKeyCredentialProviderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.default_api_key_type
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type


class UpdateApiKeyCredentialProviderRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider to update.</p>"""
    api_key: NotRequired[
        "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
    ]
    """<p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>"""
    api_key_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    api_key_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiKeyCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "api_key" in value:
        out["apiKey"] = value["api_key"]
    if "api_key_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["apiKeySecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["api_key_secret_config"]
            )
        )
    if "api_key_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["apiKeySecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["api_key_secret_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApiKeyCredentialProviderRequest:
    out: UpdateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    if data.get("apiKeySecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["api_key_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["apiKeySecretConfig"]
            )
        )
    if data.get("apiKeySecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["api_key_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["apiKeySecretSource"]
            )
        )
    return out


def redact_sensitive(value: UpdateApiKeyCredentialProviderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
