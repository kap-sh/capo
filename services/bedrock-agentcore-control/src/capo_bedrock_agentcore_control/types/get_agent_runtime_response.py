"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_arn
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_name
    import capo_bedrock_agentcore_control.types.agent_runtime_status
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.allowed_ports
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.capacity_provider_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
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
    import capo_bedrock_agentcore_control.types.workload_identity_details


class GetAgentRuntimeResponse(TypedDict, closed=True):
    agent_runtime_arn: (
        "capo_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    agent_runtime_name: (
        "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    )
    """<p>The name of the AgentCore Runtime.</p>"""
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    agent_runtime_version: (
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    )
    """<p>The version of the AgentCore Runtime.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was last updated.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>"""
    network_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the AgentCore Runtime.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the AgentCore Runtime.</p>"""
    lifecycle_configuration: "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    """<p>The life cycle configuration for the AgentCore Runtime.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the AgentCore Runtime is in a failed state.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the AgentCore Runtime.</p>"""
    workload_identity_details: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    """<p>The workload identity details for the AgentCore Runtime.</p>"""
    agent_runtime_artifact: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact"
    ]
    """<p>The artifact of the AgentCore Runtime.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
    ]
    """<p>The protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables set in the AgentCore Runtime environment.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the AgentCore Runtime.</p>"""
    request_header_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
    ]
    """<p>Configuration for HTTP request headers that will be passed through to the runtime.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"
    ]
    """<p>Configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations mounted into the AgentCore Runtime.</p>"""
    capacity_provider_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
    ]
    """<p>The capacity provider configuration for the AgentCore Runtime.</p>"""
    platform_version: NotRequired[
        "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
    ]
    """<p>The version of the runtime platform used by the AgentCore Runtime.</p>"""
    allowed_ports: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
    ]
    """<p>The additional ports on the AgentCore Runtime that are reachable through the runtime's session URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeResponse) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
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
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.lifecycle_configuration

    out["lifecycleConfiguration"] = (
        capo_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
            value["lifecycle_configuration"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "description" in value:
        out["description"] = value["description"]
    if "workload_identity_details" in value:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    if "agent_runtime_artifact" in value:
        import capo_bedrock_agentcore_control.types.agent_runtime_artifact

        out["agentRuntimeArtifact"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_artifact.serialize_json(
                value["agent_runtime_artifact"]
            )
        )
    if "protocol_configuration" in value:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocolConfiguration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    if "environment_variables" in value:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environmentVariables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
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
    if "metadata_configuration" in value:
        import capo_bedrock_agentcore_control.types.runtime_metadata_configuration

        out["metadataConfiguration"] = (
            capo_bedrock_agentcore_control.types.runtime_metadata_configuration.serialize_json(
                value["metadata_configuration"]
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
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeResponse:
    out: GetAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeArn") is not None:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        out["agent_runtime_arn"] = ""
    if data.get("agentRuntimeName") is not None:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        out["agent_runtime_name"] = ""
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        out["agent_runtime_id"] = ""
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        out["agent_runtime_version"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
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
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus",
            "",
        )
    if data.get("lifecycleConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentRuntimeResponse.lifecycle_configuration required"
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("workloadIdentityDetails") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if data.get("agentRuntimeArtifact") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_artifact

        out["agent_runtime_artifact"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_artifact.deserialize_json(
                data["agentRuntimeArtifact"]
            )
        )
    if data.get("protocolConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.protocol_configuration

        out["protocol_configuration"] = (
            capo_bedrock_agentcore_control.types.protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if data.get("environmentVariables") is not None:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environment_variables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
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
    if data.get("metadataConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.runtime_metadata_configuration

        out["metadata_configuration"] = (
            capo_bedrock_agentcore_control.types.runtime_metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
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
    return out


def redact_sensitive(value: GetAgentRuntimeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
