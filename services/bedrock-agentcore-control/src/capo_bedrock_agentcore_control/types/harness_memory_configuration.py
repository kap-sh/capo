"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessMemoryConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration


class HarnessMemoryConfigurationAgentCoreMemoryConfigurationMember(
    TypedDict, closed=True
):
    agentCoreMemoryConfiguration: "capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.HarnessAgentCoreMemoryConfiguration"


class HarnessMemoryConfigurationManagedMemoryConfigurationMember(
    TypedDict, closed=True
):
    managedMemoryConfiguration: "capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.HarnessManagedMemoryConfiguration"


class HarnessMemoryConfigurationDisabledMember(TypedDict, closed=True):
    disabled: "capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.HarnessDisabledMemoryConfiguration"


HarnessMemoryConfiguration: TypeAlias = (
    HarnessMemoryConfigurationAgentCoreMemoryConfigurationMember
    | HarnessMemoryConfigurationManagedMemoryConfigurationMember
    | HarnessMemoryConfigurationDisabledMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMemoryConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessMemoryConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentCoreMemoryConfiguration" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.serialize_json(
                value["agentCoreMemoryConfiguration"]
            )
        }
    elif "managedMemoryConfiguration" in value:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration

        return {
            "managedMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.serialize_json(
                value["managedMemoryConfiguration"]
            )
        }
    elif "disabled" in value:
        import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration

        return {
            "disabled": capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.serialize_json(
                value["disabled"]
            )
        }
    else:
        raise SerializationError("HarnessMemoryConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessMemoryConfiguration:
    if data.get("agentCoreMemoryConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.deserialize_json(
                data["agentCoreMemoryConfiguration"]
            )
        }
    elif data.get("managedMemoryConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration

        return {
            "managedMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.deserialize_json(
                data["managedMemoryConfiguration"]
            )
        }
    elif data.get("disabled") is not None:
        import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration

        return {
            "disabled": capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.deserialize_json(
                data["disabled"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessMemoryConfiguration: no recognized variant key"
        )
