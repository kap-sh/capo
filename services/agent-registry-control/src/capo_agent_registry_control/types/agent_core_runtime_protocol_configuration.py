"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentCoreRuntimeProtocolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.agent_core_runtime_server_protocol


class AgentCoreRuntimeProtocolConfiguration(TypedDict, closed=True):
    server_protocol: NotRequired[
        "capo_agent_registry_control.types.agent_core_runtime_server_protocol.AgentCoreRuntimeServerProtocol"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreRuntimeProtocolConfiguration) -> dict:
    out: dict = {}
    if "server_protocol" in value:
        import capo_agent_registry_control.types.agent_core_runtime_server_protocol

        out["serverProtocol"] = (
            capo_agent_registry_control.types.agent_core_runtime_server_protocol.serialize_json(
                value["server_protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCoreRuntimeProtocolConfiguration:
    out: AgentCoreRuntimeProtocolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serverProtocol") is not None:
        import capo_agent_registry_control.types.agent_core_runtime_server_protocol

        out["server_protocol"] = (
            capo_agent_registry_control.types.agent_core_runtime_server_protocol.deserialize_json(
                data["serverProtocol"]
            )
        )
    return out
