"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentRuntimeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.allowed_ports
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.capacity_provider_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.network_configuration
    import capo_bedrock_agentcore_control.types.platform_version
    import capo_bedrock_agentcore_control.types.protocol_configuration
    import capo_bedrock_agentcore_control.types.request_header_configuration
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.runtime_metadata_configuration


class UpdateAgentRuntimeRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime to update.</p>"""
    agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact"
    """<p>The updated artifact of the AgentCore Runtime.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>"""
    network_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The updated network configuration for the AgentCore Runtime.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The updated description of the AgentCore Runtime.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration for the AgentCore Runtime.</p>"""
    request_header_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
    ]
    """<p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
    ]
    """<p>The updated protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    """<p>The updated life cycle configuration for the AgentCore Runtime.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"
    ]
    """<p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Updated environment variables to set in the AgentCore Runtime environment.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>"""
    capacity_provider_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
    ]
    """<p>The updated capacity provider configuration for the AgentCore Runtime.</p>"""
    platform_version: NotRequired[
        "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
    ]
    """<p>The updated version of the runtime platform to use for the AgentCore Runtime.</p>"""
    allowed_ports: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
    ]
    """<p>The updated additional ports on the AgentCore Runtime that are reachable through the runtime's session URL. Specify one to five non-overlapping entries, each containing either a single port or an inclusive port range. Ports must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRuntimeRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact

    out["agentRuntimeArtifact"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_artifact.serialize_json(
            value["agent_runtime_artifact"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "network_configuration" in value:
        import capo_bedrock_agentcore_control.types.network_configuration

        out["networkConfiguration"] = (
            capo_bedrock_agentcore_control.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "request_header_configuration" in value:
        import capo_bedrock_agentcore_control.types.request_header_configuration

        out["requestHeaderConfiguration"] = (
            capo_bedrock_agentcore_control.types.request_header_configuration.serialize_json(
                value["request_header_configuration"]
            )
        )
    if "protocol_configuration" in value:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocolConfiguration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    if "lifecycle_configuration" in value:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "metadata_configuration" in value:
        import capo_bedrock_agentcore_control.types.runtime_metadata_configuration

        out["metadataConfiguration"] = (
            capo_bedrock_agentcore_control.types.runtime_metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "environment_variables" in value:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environmentVariables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "filesystem_configurations" in value:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystemConfigurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    if "capacity_provider_configuration" in value:
        import capo_bedrock_agentcore_control.types.capacity_provider_configuration

        out["capacityProviderConfiguration"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_configuration.serialize_json(
                value["capacity_provider_configuration"]
            )
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "allowed_ports" in value:
        import capo_bedrock_agentcore_control.types.allowed_ports

        out["allowedPorts"] = (
            capo_bedrock_agentcore_control.types.allowed_ports.serialize_json(
                value["allowed_ports"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAgentRuntimeRequest:
    out: UpdateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeArtifact") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_artifact

        out["agent_runtime_artifact"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_artifact.deserialize_json(
                data["agentRuntimeArtifact"]
            )
        )
    else:
        out["agent_runtime_artifact"] = {"$unknown": {"name": ""}}
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("networkConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("requestHeaderConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.request_header_configuration

        out["request_header_configuration"] = (
            capo_bedrock_agentcore_control.types.request_header_configuration.deserialize_json(
                data["requestHeaderConfiguration"]
            )
        )
    if data.get("protocolConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocol_configuration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if data.get("lifecycleConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if data.get("metadataConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.runtime_metadata_configuration

        out["metadata_configuration"] = (
            capo_bedrock_agentcore_control.types.runtime_metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if data.get("environmentVariables") is not None:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environment_variables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("filesystemConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    if data.get("capacityProviderConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_configuration

        out["capacity_provider_configuration"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_configuration.deserialize_json(
                data["capacityProviderConfiguration"]
            )
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("allowedPorts") is not None:
        import capo_bedrock_agentcore_control.types.allowed_ports

        out["allowed_ports"] = (
            capo_bedrock_agentcore_control.types.allowed_ports.deserialize_json(
                data["allowedPorts"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateAgentRuntimeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
