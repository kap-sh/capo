"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StripePrivyConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.secret
    import capo_bedrock_agentcore_control.types.secret_json_key_type
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.stripe_privy_app_id_type
    import capo_bedrock_agentcore_control.types.stripe_privy_authorization_id_type


class StripePrivyConfigurationOutput(TypedDict, closed=True):
    app_id: "capo_bedrock_agentcore_control.types.stripe_privy_app_id_type.StripePrivyAppIdType"
    """<p>The app ID provided by Privy.</p>"""
    app_secret_arn: "capo_bedrock_agentcore_control.types.secret.Secret"
    app_secret_json_key: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the app secret value from the Amazon Web Services Secrets Manager secret.</p>"""
    app_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the app secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in Amazon Web Services Secrets Manager.</p>"""
    authorization_private_key_arn: "capo_bedrock_agentcore_control.types.secret.Secret"
    authorization_private_key_json_key: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the authorization private key value from the Amazon Web Services Secrets Manager secret.</p>"""
    authorization_private_key_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the authorization private key. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in Amazon Web Services Secrets Manager.</p>"""
    authorization_id: "capo_bedrock_agentcore_control.types.stripe_privy_authorization_id_type.StripePrivyAuthorizationIdType"
    """<p>The authorization ID for the Stripe Privy integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyConfigurationOutput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    import capo_bedrock_agentcore_control.types.secret

    out["appSecretArn"] = capo_bedrock_agentcore_control.types.secret.serialize_json(
        value["app_secret_arn"]
    )
    if "app_secret_json_key" in value:
        out["appSecretJsonKey"] = value["app_secret_json_key"]
    if "app_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["appSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["app_secret_source"]
            )
        )
    import capo_bedrock_agentcore_control.types.secret

    out["authorizationPrivateKeyArn"] = (
        capo_bedrock_agentcore_control.types.secret.serialize_json(
            value["authorization_private_key_arn"]
        )
    )
    if "authorization_private_key_json_key" in value:
        out["authorizationPrivateKeyJsonKey"] = value[
            "authorization_private_key_json_key"
        ]
    if "authorization_private_key_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["authorizationPrivateKeySource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["authorization_private_key_source"]
            )
        )
    out["authorizationId"] = value["authorization_id"]
    return out


def deserialize_json(data: dict) -> StripePrivyConfigurationOutput:
    out: StripePrivyConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appSecretArn") is not None:
        import capo_bedrock_agentcore_control.types.secret

        out["app_secret_arn"] = (
            capo_bedrock_agentcore_control.types.secret.deserialize_json(
                data["appSecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "StripePrivyConfigurationOutput.app_secret_arn required"
        )
    if data.get("appSecretJsonKey") is not None:
        out["app_secret_json_key"] = data["appSecretJsonKey"]
    if data.get("appSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["app_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["appSecretSource"]
            )
        )
    if data.get("authorizationPrivateKeyArn") is not None:
        import capo_bedrock_agentcore_control.types.secret

        out["authorization_private_key_arn"] = (
            capo_bedrock_agentcore_control.types.secret.deserialize_json(
                data["authorizationPrivateKeyArn"]
            )
        )
    else:
        raise DeserializationError(
            "StripePrivyConfigurationOutput.authorization_private_key_arn required"
        )
    if data.get("authorizationPrivateKeyJsonKey") is not None:
        out["authorization_private_key_json_key"] = data[
            "authorizationPrivateKeyJsonKey"
        ]
    if data.get("authorizationPrivateKeySource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["authorization_private_key_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["authorizationPrivateKeySource"]
            )
        )
    if data.get("authorizationId") is not None:
        out["authorization_id"] = data["authorizationId"]
    else:
        out["authorization_id"] = ""
    return out
