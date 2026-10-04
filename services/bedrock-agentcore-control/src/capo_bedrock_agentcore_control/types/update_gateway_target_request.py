"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificate_configuration_list
    import capo_bedrock_agentcore_control.types.credential_provider_configurations
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.metadata_configuration
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.target_configuration
    import capo_bedrock_agentcore_control.types.target_description
    import capo_bedrock_agentcore_control.types.target_id
    import capo_bedrock_agentcore_control.types.target_name


class UpdateGatewayTargetRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway associated with the target.</p>"""
    target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the gateway target to update.</p>"""
    name: NotRequired["capo_bedrock_agentcore_control.types.target_name.TargetName"]
    """<p>The updated name for the gateway target.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The updated description for the gateway target.</p>"""
    target_configuration: (
        "capo_bedrock_agentcore_control.types.target_configuration.TargetConfiguration"
    )
    credential_provider_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
    ]
    """<p>The updated credential provider configurations for the gateway target.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>Configuration for HTTP header and query parameter propagation to the gateway target.</p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>"""
    certificate_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.certificate_configuration_list.CertificateConfigurationList"
    ]
    """<p>The private certificate authority (CA) configurations for the gateway target. Use this to have the gateway trust a private CA when it establishes TLS connections to the target endpoint. Provide each certificate by reference to an Amazon S3 object or an Amazon Web Services Secrets Manager secret. You can specify only one certificate authority configuration in this list. To remove a previously configured certificate authority, omit this field on update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayTargetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "certificate_configurations" in value:
        import capo_bedrock_agentcore_control.types.certificate_configuration_list

        out["certificateConfigurations"] = (
            capo_bedrock_agentcore_control.types.certificate_configuration_list.serialize_json(
                value["certificate_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayTargetRequest:
    out: UpdateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targetConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.target_configuration

        out["target_configuration"] = (
            capo_bedrock_agentcore_control.types.target_configuration.deserialize_json(
                data["targetConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateGatewayTargetRequest.target_configuration required"
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
    if data.get("certificateConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.certificate_configuration_list

        out["certificate_configurations"] = (
            capo_bedrock_agentcore_control.types.certificate_configuration_list.deserialize_json(
                data["certificateConfigurations"]
            )
        )
    return out
