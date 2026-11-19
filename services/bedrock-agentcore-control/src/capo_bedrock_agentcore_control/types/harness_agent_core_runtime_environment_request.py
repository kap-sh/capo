"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreRuntimeEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.network_configuration


class HarnessAgentCoreRuntimeEnvironmentRequest(TypedDict, closed=True):
    lifecycle_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    """<p>The lifecycle configuration for the harness's runtime environment. For a harness, <code>idleRuntimeSessionTimeout</code> and <code>maxLifetime</code> each accept a value between 60 and 28800 seconds (8 hours), and <code>idleRuntimeSessionTimeout</code> must be less than or equal to <code>maxLifetime</code>. Values above 28800 seconds are rejected with a <code>ValidationException</code>.</p>"""
    network_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    ]
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations for the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreRuntimeEnvironmentRequest) -> dict:
    out: dict = {}
    if "lifecycle_configuration" in value:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "network_configuration" in value:
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


def deserialize_json(data: dict) -> HarnessAgentCoreRuntimeEnvironmentRequest:
    out: HarnessAgentCoreRuntimeEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("filesystemConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    return out
