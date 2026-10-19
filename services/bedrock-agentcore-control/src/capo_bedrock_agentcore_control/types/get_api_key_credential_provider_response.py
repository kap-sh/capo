"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetApiKeyCredentialProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.api_key_credential_provider_arn_type
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.secret
    import capo_bedrock_agentcore_control.types.secret_json_key_type
    import capo_bedrock_agentcore_control.types.secret_source_type


class GetApiKeyCredentialProviderResponse(TypedDict, closed=True):
    api_key_secret_arn: "capo_bedrock_agentcore_control.types.secret.Secret"
    """<p>The Amazon Resource Name (ARN) of the API key secret in Amazon Web Services Secrets Manager.</p>"""
    api_key_secret_json_key: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the API key value from the Amazon Web Services Secrets Manager secret.</p>"""
    api_key_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in Amazon Web Services Secrets Manager.</p>"""
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider.</p>"""
    credential_provider_arn: "capo_bedrock_agentcore_control.types.api_key_credential_provider_arn_type.ApiKeyCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the API key credential provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiKeyCredentialProviderResponse) -> dict:
    out: dict = {}
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
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetApiKeyCredentialProviderResponse:
    out: GetApiKeyCredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("apiKeySecretArn") is not None:
        import capo_bedrock_agentcore_control.types.secret

        out["api_key_secret_arn"] = (
            capo_bedrock_agentcore_control.types.secret.deserialize_json(
                data["apiKeySecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "GetApiKeyCredentialProviderResponse.api_key_secret_arn required"
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
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        out["credential_provider_arn"] = ""
    if data.get("createdTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
