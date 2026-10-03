"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.credential_provider_configurations
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.metadata_configuration
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.target_configuration
    import capo_bedrock_agentcore_control.types.target_description
    import capo_bedrock_agentcore_control.types.target_name


class CreateGatewayTargetRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to create a target for.</p>"""
    name: NotRequired["capo_bedrock_agentcore_control.types.target_name.TargetName"]
    """<p>The name of the gateway target. The name must be unique within the gateway.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The description of the gateway target.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    target_configuration: (
        "capo_bedrock_agentcore_control.types.target_configuration.TargetConfiguration"
    )
    """<p>The configuration settings for the target, including endpoint information and schema definitions.</p>"""
    credential_provider_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
    ]
    """<p>The credential provider configurations for the target. These configurations specify how the gateway authenticates with the target endpoint.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>Optional configuration for HTTP header and query parameter propagation to and from the gateway target.</p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayTargetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agentcore_control.types.target_configuration

    out["targetConfiguration"] = (
        capo_bedrock_agentcore_control.types.target_configuration.serialize_json(
            value["target_configuration"]
        )
    )
    if "credential_provider_configurations" in value:
        import capo_bedrock_agentcore_control.types.credential_provider_configurations

        out["credentialProviderConfigurations"] = (
            capo_bedrock_agentcore_control.types.credential_provider_configurations.serialize_json(
                value["credential_provider_configurations"]
            )
        )
    if "metadata_configuration" in value:
        import capo_bedrock_agentcore_control.types.metadata_configuration

        out["metadataConfiguration"] = (
            capo_bedrock_agentcore_control.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "private_endpoint" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayTargetRequest:
    out: CreateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("targetConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.target_configuration

        out["target_configuration"] = (
            capo_bedrock_agentcore_control.types.target_configuration.deserialize_json(
                data["targetConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateGatewayTargetRequest.target_configuration required"
        )
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.credential_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credential_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    if data.get("metadataConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.metadata_configuration

        out["metadata_configuration"] = (
            capo_bedrock_agentcore_control.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if data.get("privateEndpoint") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    return out
