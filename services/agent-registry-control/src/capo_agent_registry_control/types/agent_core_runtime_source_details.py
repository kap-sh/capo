"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentCoreRuntimeSourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.agent_core_runtime_protocol_configuration
    import capo_agent_registry_control.types.authorizer_configuration
    import capo_agent_registry_control.types.workload_identity_details


class AgentCoreRuntimeSourceDetails(TypedDict, closed=True):
    protocol_configuration: NotRequired[
        "capo_agent_registry_control.types.agent_core_runtime_protocol_configuration.AgentCoreRuntimeProtocolConfiguration"
    ]
    authorizer_configuration: NotRequired[
        "capo_agent_registry_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    workload_identity_details: NotRequired[
        "capo_agent_registry_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreRuntimeSourceDetails) -> dict:
    out: dict = {}
    if "protocol_configuration" in value:
        import capo_agent_registry_control.types.agent_core_runtime_protocol_configuration

        out["protocolConfiguration"] = (
            capo_agent_registry_control.types.agent_core_runtime_protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_agent_registry_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_agent_registry_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "workload_identity_details" in value:
        import capo_agent_registry_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            capo_agent_registry_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCoreRuntimeSourceDetails:
    out: AgentCoreRuntimeSourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("protocolConfiguration") is not None:
        import capo_agent_registry_control.types.agent_core_runtime_protocol_configuration

        out["protocol_configuration"] = (
            capo_agent_registry_control.types.agent_core_runtime_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_agent_registry_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_agent_registry_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("workloadIdentityDetails") is not None:
        import capo_agent_registry_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_agent_registry_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    return out
