"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkAwsGroundStationAgentEndpointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.agent_status
    import capo_groundstation.types.audit_results
    import capo_groundstation.types.downlink_dataflow_details
    import capo_groundstation.types.safe_name


class DownlinkAwsGroundStationAgentEndpointDetails(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Downlink dataflow endpoint name</p>"""
    dataflow_details: (
        "capo_groundstation.types.downlink_dataflow_details.DownlinkDataflowDetails"
    )
    """<p>Dataflow details for the downlink endpoint</p>"""
    agent_status: NotRequired["capo_groundstation.types.agent_status.AgentStatus"]
    """<p>Status of the agent associated with the downlink dataflow endpoint</p>"""
    audit_results: NotRequired["capo_groundstation.types.audit_results.AuditResults"]
    """<p>Health audit results for the downlink dataflow endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkAwsGroundStationAgentEndpointDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.downlink_dataflow_details

    out["dataflowDetails"] = (
        capo_groundstation.types.downlink_dataflow_details.serialize_json(
            value["dataflow_details"]
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


def deserialize_json(data: dict) -> DownlinkAwsGroundStationAgentEndpointDetails:
    out: DownlinkAwsGroundStationAgentEndpointDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dataflowDetails") is not None:
        import capo_groundstation.types.downlink_dataflow_details

        out["dataflow_details"] = (
            capo_groundstation.types.downlink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        import capo_groundstation.types._unknown

        out["dataflow_details"] = capo_groundstation.types._unknown.UnknownUnionMember(
            ""
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
