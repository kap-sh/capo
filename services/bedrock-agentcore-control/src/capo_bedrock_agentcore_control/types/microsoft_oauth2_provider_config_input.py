"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MicrosoftOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_id_type
    import capo_bedrock_agentcore_control.types.default_client_secret_type
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.tenant_id_type


class MicrosoftOauth2ProviderConfigInput(TypedDict, closed=True):
    client_id: "capo_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    """<p>The client ID for the Microsoft OAuth2 provider.</p>"""
    client_secret: "capo_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the Microsoft OAuth2 provider.</p>"""
    client_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    tenant_id: NotRequired[
        "capo_bedrock_agentcore_control.types.tenant_id_type.TenantIdType"
    ]
    """<p>The Microsoft Entra ID (formerly Azure AD) tenant ID for your organization. This identifies the specific tenant within Microsoft's identity platform where your application is registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrosoftOauth2ProviderConfigInput) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value.get("client_secret", "")
    if "client_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["clientSecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["client_secret_config"]
            )
        )
    if "client_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["clientSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["client_secret_source"]
            )
        )
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    return out


def deserialize_json(data: dict) -> MicrosoftOauth2ProviderConfigInput:
    out: MicrosoftOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "MicrosoftOauth2ProviderConfigInput.client_id required"
        )
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ""
    if data.get("clientSecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["client_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["clientSecretConfig"]
            )
        )
    if data.get("clientSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["client_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["clientSecretSource"]
            )
        )
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    return out


def redact_sensitive(value: MicrosoftOauth2ProviderConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
