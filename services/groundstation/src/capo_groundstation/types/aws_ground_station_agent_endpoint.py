"""Generated from Smithy shape ``com.amazonaws.groundstation#AwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.agent_status
    import capo_groundstation.types.audit_results
    import capo_groundstation.types.connection_details
    import capo_groundstation.types.ranged_connection_details
    import capo_groundstation.types.safe_name


class AwsGroundStationAgentEndpoint(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Name string associated with AgentEndpoint. Used as a human-readable identifier for AgentEndpoint.</p>"""
    egress_address: "capo_groundstation.types.connection_details.ConnectionDetails"
    """<p>The egress address of AgentEndpoint.</p>"""
    ingress_address: (
        "capo_groundstation.types.ranged_connection_details.RangedConnectionDetails"
    )
    """<p>The ingress address of AgentEndpoint.</p>"""
    agent_status: NotRequired["capo_groundstation.types.agent_status.AgentStatus"]
    """<p>The status of AgentEndpoint.</p>"""
    audit_results: NotRequired["capo_groundstation.types.audit_results.AuditResults"]
    """<p>The results of the audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.connection_details

    out["egressAddress"] = capo_groundstation.types.connection_details.serialize_json(
        value["egress_address"]
    )
    import capo_groundstation.types.ranged_connection_details

    out["ingressAddress"] = (
        capo_groundstation.types.ranged_connection_details.serialize_json(
            value["ingress_address"]
        )
    )
    if "agent_status" in value:
        import capo_groundstation.types.agent_status

        out["agentStatus"] = capo_groundstation.types.agent_status.serialize_json(
            value["agent_status"]
        )
    if "audit_results" in value:
        import capo_groundstation.types.audit_results

        out["auditResults"] = capo_groundstation.types.audit_results.serialize_json(
            value["audit_results"]
        )
    return out


def deserialize_json(data: dict) -> AwsGroundStationAgentEndpoint:
    out: AwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("egressAddress") is not None:
        import capo_groundstation.types.connection_details

        out["egress_address"] = (
            capo_groundstation.types.connection_details.deserialize_json(
                data["egressAddress"]
            )
        )
    else:
        raise DeserializationError(
            "AwsGroundStationAgentEndpoint.egress_address required"
        )
    if data.get("ingressAddress") is not None:
        import capo_groundstation.types.ranged_connection_details

        out["ingress_address"] = (
            capo_groundstation.types.ranged_connection_details.deserialize_json(
                data["ingressAddress"]
            )
        )
    else:
        raise DeserializationError(
            "AwsGroundStationAgentEndpoint.ingress_address required"
        )
    if data.get("agentStatus") is not None:
        import capo_groundstation.types.agent_status

        out["agent_status"] = capo_groundstation.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    if data.get("auditResults") is not None:
        import capo_groundstation.types.audit_results

        out["audit_results"] = capo_groundstation.types.audit_results.deserialize_json(
            data["auditResults"]
        )
    return out
