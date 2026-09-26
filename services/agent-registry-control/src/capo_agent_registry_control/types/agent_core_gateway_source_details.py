"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentCoreGatewaySourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.agent_core_gateway_protocol_type
    import capo_agent_registry_control.types.authorizer_configuration
    import capo_agent_registry_control.types.workload_identity_details


class AgentCoreGatewaySourceDetails(TypedDict, closed=True):
    protocol_type: NotRequired[
        "capo_agent_registry_control.types.agent_core_gateway_protocol_type.AgentCoreGatewayProtocolType"
    ]
    authorizer_type: NotRequired["str"]
    """<p>The type of authorizer configured on the AgentCore Gateway resource that the registry record was detected from.</p>"""
    authorizer_configuration: NotRequired[
        "capo_agent_registry_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    workload_identity_details: NotRequired[
        "capo_agent_registry_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreGatewaySourceDetails) -> dict:
    out: dict = {}
    if "protocol_type" in value:
        import capo_agent_registry_control.types.agent_core_gateway_protocol_type

        out["protocolType"] = (
            capo_agent_registry_control.types.agent_core_gateway_protocol_type.serialize_json(
                value["protocol_type"]
            )
        )
    if "authorizer_type" in value:
        out["authorizerType"] = value["authorizer_type"]
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


def deserialize_json(data: dict) -> AgentCoreGatewaySourceDetails:
    out: AgentCoreGatewaySourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("protocolType") is not None:
        import capo_agent_registry_control.types.agent_core_gateway_protocol_type

        out["protocol_type"] = (
            capo_agent_registry_control.types.agent_core_gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    if data.get("authorizerType") is not None:
        out["authorizer_type"] = data["authorizerType"]
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
