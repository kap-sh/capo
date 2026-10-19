"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateAgentRuntimeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_name
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
    import capo_bedrock_agentcore_control.types.tags_map


class CreateAgentRuntimeRequest(TypedDict, closed=True):
    agent_runtime_name: (
        "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    )
    """<p>The name of the AgentCore Runtime.</p>"""
    agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact"
    """<p>The artifact of the AgentCore Runtime.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>"""
    network_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the AgentCore Runtime.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the AgentCore Runtime.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the AgentCore Runtime.</p>"""
    request_header_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
    ]
    """<p>Configuration for HTTP request headers that will be passed through to the runtime.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
    ]
    lifecycle_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    """<p>The life cycle configuration for the AgentCore Runtime.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables to set in the AgentCore Runtime environment.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>"""
    capacity_provider_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
    ]
    """<p>The capacity provider configuration for the AgentCore Runtime. Use a capacity provider to run the AgentCore Runtime on the Instances compute type, which provisions Amazon Web Services managed compute in your account.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""
    platform_version: NotRequired[
        "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
    ]
    """<p>The version of the runtime platform to use for the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRuntimeRequest) -> dict:
    out: dict = {}
    out["agentRuntimeName"] = value["agent_runtime_name"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    return out


def deserialize_json(data: dict) -> CreateAgentRuntimeRequest:
    out: CreateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeName") is not None:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        out["agent_runtime_name"] = ""
    if data.get("agentRuntimeArtifact") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_artifact

        out["agent_runtime_artifact"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_artifact.deserialize_json(
                data["agentRuntimeArtifact"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["agent_runtime_artifact"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    return out


def redact_sensitive(value: CreateAgentRuntimeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
