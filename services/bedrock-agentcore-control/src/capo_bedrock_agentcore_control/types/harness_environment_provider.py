"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment


class HarnessEnvironmentProviderAgentCoreRuntimeEnvironmentMember(
    TypedDict, closed=True
):
    agentCoreRuntimeEnvironment: "capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.HarnessAgentCoreRuntimeEnvironment"


HarnessEnvironmentProvider: TypeAlias = (
    HarnessEnvironmentProviderAgentCoreRuntimeEnvironmentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessEnvironmentProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentCoreRuntimeEnvironment" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.serialize_json(
                value["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise SerializationError("HarnessEnvironmentProvider: no variant present")


def deserialize_json(data: dict) -> HarnessEnvironmentProvider:
    if data.get("agentCoreRuntimeEnvironment") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment.deserialize_json(
                data["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessEnvironmentProvider: no recognized variant key"
        )
