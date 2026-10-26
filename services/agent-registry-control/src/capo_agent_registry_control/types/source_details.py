"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#SourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError, SerializationError
from capo_agent_registry_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_agent_registry_control.types.agent_core_gateway_source_details
    import capo_agent_registry_control.types.agent_core_runtime_source_details


class _SourceDetails_agentcoreRuntime(TypedDict, closed=True):
    agentcoreRuntime: "capo_agent_registry_control.types.agent_core_runtime_source_details.AgentCoreRuntimeSourceDetails"


class _SourceDetails_agentcoreGateway(TypedDict, closed=True):
    agentcoreGateway: "capo_agent_registry_control.types.agent_core_gateway_source_details.AgentCoreGatewaySourceDetails"


SourceDetails: TypeAlias = (
    _SourceDetails_agentcoreRuntime
    | _SourceDetails_agentcoreGateway
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentcoreRuntime" in value:
        import capo_agent_registry_control.types.agent_core_runtime_source_details

        return {
            "agentcoreRuntime": capo_agent_registry_control.types.agent_core_runtime_source_details.serialize_json(
                value["agentcoreRuntime"]
            )
        }
    elif "agentcoreGateway" in value:
        import capo_agent_registry_control.types.agent_core_gateway_source_details

        return {
            "agentcoreGateway": capo_agent_registry_control.types.agent_core_gateway_source_details.serialize_json(
                value["agentcoreGateway"]
            )
        }
    else:
        raise SerializationError("SourceDetails: no variant present")


def deserialize_json(data: dict) -> SourceDetails:
    if data.get("agentcoreRuntime") is not None:
        import capo_agent_registry_control.types.agent_core_runtime_source_details

        return {
            "agentcoreRuntime": capo_agent_registry_control.types.agent_core_runtime_source_details.deserialize_json(
                data["agentcoreRuntime"]
            )
        }
    elif data.get("agentcoreGateway") is not None:
        import capo_agent_registry_control.types.agent_core_gateway_source_details

        return {
            "agentcoreGateway": capo_agent_registry_control.types.agent_core_gateway_source_details.deserialize_json(
                data["agentcoreGateway"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceDetails: no recognized variant key")
