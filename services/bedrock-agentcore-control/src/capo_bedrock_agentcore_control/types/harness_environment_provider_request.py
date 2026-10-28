"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEnvironmentProviderRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request


class HarnessEnvironmentProviderRequestAgentCoreRuntimeEnvironmentMember(
    TypedDict, closed=True
):
    agentCoreRuntimeEnvironment: "capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.HarnessAgentCoreRuntimeEnvironmentRequest"


HarnessEnvironmentProviderRequest: TypeAlias = (
    HarnessEnvironmentProviderRequestAgentCoreRuntimeEnvironmentMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEnvironmentProviderRequest) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessEnvironmentProviderRequest: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentCoreRuntimeEnvironment" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.serialize_json(
                value["agentCoreRuntimeEnvironment"]
            )
        }
    else:
        raise SerializationError(
            "HarnessEnvironmentProviderRequest: no variant present"
        )


def deserialize_json(data: dict) -> HarnessEnvironmentProviderRequest:
    if data.get("agentCoreRuntimeEnvironment") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request

        return {
            "agentCoreRuntimeEnvironment": capo_bedrock_agentcore_control.types.harness_agent_core_runtime_environment_request.deserialize_json(
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
            "HarnessEnvironmentProviderRequest: no recognized variant key"
        )
