"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreRuntimeEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.network_configuration


class HarnessAgentCoreRuntimeEnvironment(TypedDict, closed=True):
    agent_runtime_arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    """<p>The ARN of the underlying AgentCore Runtime.</p>"""
    agent_runtime_name: "str"
    """<p>The name of the underlying AgentCore Runtime.</p>"""
    agent_runtime_id: "str"
    """<p>The ID of the underlying AgentCore Runtime.</p>"""
    lifecycle_configuration: "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    network_configuration: "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations for the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreRuntimeEnvironment) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    import capo_bedrock_agentcore_control.types.lifecycle_configuration

    out["lifecycleConfiguration"] = (
        capo_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
            value["lifecycle_configuration"]
        )
    )
    import capo_bedrock_agentcore_control.types.network_configuration

    out["networkConfiguration"] = (
        capo_bedrock_agentcore_control.types.network_configuration.serialize_json(
            value["network_configuration"]
        )
    )
    if "filesystem_configurations" in value:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystemConfigurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreRuntimeEnvironment:
    out: HarnessAgentCoreRuntimeEnvironment = {}  # type: ignore[typeddict-item]
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
    if data.get("lifecycleConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "HarnessAgentCoreRuntimeEnvironment.lifecycle_configuration required"
        )
    if data.get("networkConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "HarnessAgentCoreRuntimeEnvironment.network_configuration required"
        )
    if data.get("filesystemConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    return out
