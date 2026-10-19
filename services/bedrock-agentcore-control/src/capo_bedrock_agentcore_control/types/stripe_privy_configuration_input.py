"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StripePrivyConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.default_stripe_privy_app_secret_type
    import capo_bedrock_agentcore_control.types.default_stripe_privy_authorization_private_key_type
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.stripe_privy_app_id_type
    import capo_bedrock_agentcore_control.types.stripe_privy_authorization_id_type


class StripePrivyConfigurationInput(TypedDict, closed=True):
    app_id: "capo_bedrock_agentcore_control.types.stripe_privy_app_id_type.StripePrivyAppIdType"
    """<p>The app ID provided by Privy.</p>"""
    app_secret: "capo_bedrock_agentcore_control.types.default_stripe_privy_app_secret_type.DefaultStripePrivyAppSecretType"
    """<p>The app secret provided by Privy.</p>"""
    app_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the app secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    app_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the app secret. This includes the secret ID and the JSON key used to extract the app secret value from the secret. Required when <code>appSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    authorization_private_key: "capo_bedrock_agentcore_control.types.default_stripe_privy_authorization_private_key_type.DefaultStripePrivyAuthorizationPrivateKeyType"
    """<p>The authorization private key for the Stripe Privy integration.</p>"""
    authorization_private_key_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the authorization private key. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    authorization_private_key_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the authorization private key. This includes the secret ID and the JSON key used to extract the authorization private key value from the secret. Required when <code>authorizationPrivateKeySource</code> is set to <code>EXTERNAL</code>.</p>"""
    authorization_id: "capo_bedrock_agentcore_control.types.stripe_privy_authorization_id_type.StripePrivyAuthorizationIdType"
    """<p>The authorization ID for the Stripe Privy integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyConfigurationInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appSecret"] = value.get("app_secret", "")
    if "app_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["appSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["app_secret_source"]
            )
        )
    if "app_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["appSecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["app_secret_config"]
            )
        )
    out["authorizationPrivateKey"] = value.get("authorization_private_key", "")
    if "authorization_private_key_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["authorizationPrivateKeySource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["authorization_private_key_source"]
            )
        )
    if "authorization_private_key_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["authorizationPrivateKeyConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["authorization_private_key_config"]
            )
        )
    out["authorizationId"] = value["authorization_id"]
    return out


def deserialize_json(data: dict) -> StripePrivyConfigurationInput:
    out: StripePrivyConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appSecret") is not None:
        out["app_secret"] = data["appSecret"]
    else:
        out["app_secret"] = ""
    if data.get("appSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["app_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["appSecretSource"]
            )
        )
    if data.get("appSecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["app_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["appSecretConfig"]
            )
        )
    if data.get("authorizationPrivateKey") is not None:
        out["authorization_private_key"] = data["authorizationPrivateKey"]
    else:
        out["authorization_private_key"] = ""
    if data.get("authorizationPrivateKeySource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["authorization_private_key_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["authorizationPrivateKeySource"]
            )
        )
    if data.get("authorizationPrivateKeyConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["authorization_private_key_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["authorizationPrivateKeyConfig"]
            )
        )
    if data.get("authorizationId") is not None:
        out["authorization_id"] = data["authorizationId"]
    else:
        out["authorization_id"] = ""
    return out


def redact_sensitive(value: StripePrivyConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_secret" in value:
        out["app_secret"] = "*** Sensitive Data Redacted ***"
    if "authorization_private_key" in value:
        out["authorization_private_key"] = "*** Sensitive Data Redacted ***"
    return out
