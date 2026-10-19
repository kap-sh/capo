"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayApiKeyCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_key_credential_location
    import capo_bedrock_agentcore_control.types.api_key_credential_parameter_name
    import capo_bedrock_agentcore_control.types.api_key_credential_prefix
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_arn


class GatewayApiKeyCredentialProvider(TypedDict, closed=True):
    provider_arn: "capo_bedrock_agentcore_control.types.api_key_credential_provider_arn.ApiKeyCredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the API key credential provider. This ARN identifies the provider in Amazon Web Services.</p>"""
    credential_parameter_name: NotRequired[
        "capo_bedrock_agentcore_control.types.api_key_credential_parameter_name.ApiKeyCredentialParameterName"
    ]
    """<p>The name of the credential parameter for the API key. This parameter name is used when sending the API key to the target endpoint.</p>"""
    credential_prefix: NotRequired[
        "capo_bedrock_agentcore_control.types.api_key_credential_prefix.ApiKeyCredentialPrefix"
    ]
    """<p>The prefix for the API key credential. This prefix is added to the API key when sending it to the target endpoint.</p>"""
    credential_location: NotRequired[
        "capo_bedrock_agentcore_control.types.api_key_credential_location.ApiKeyCredentialLocation"
    ]
    """<p>The location of the API key credential. This field specifies where in the request the API key should be placed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayApiKeyCredentialProvider) -> dict:
    out: dict = {}
    out["providerArn"] = value["provider_arn"]
    if "credential_parameter_name" in value:
        out["credentialParameterName"] = value["credential_parameter_name"]
    if "credential_prefix" in value:
        out["credentialPrefix"] = value["credential_prefix"]
    if "credential_location" in value:
        import capo_bedrock_agentcore_control.types.api_key_credential_location

        out["credentialLocation"] = (
            capo_bedrock_agentcore_control.types.api_key_credential_location.serialize_json(
                value["credential_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> GatewayApiKeyCredentialProvider:
    out: GatewayApiKeyCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    else:
        out["provider_arn"] = ""
    if data.get("credentialParameterName") is not None:
        out["credential_parameter_name"] = data["credentialParameterName"]
    if data.get("credentialPrefix") is not None:
        out["credential_prefix"] = data["credentialPrefix"]
    if data.get("credentialLocation") is not None:
        import capo_bedrock_agentcore_control.types.api_key_credential_location

        out["credential_location"] = (
            capo_bedrock_agentcore_control.types.api_key_credential_location.deserialize_json(
                data["credentialLocation"]
            )
        )
    return out
