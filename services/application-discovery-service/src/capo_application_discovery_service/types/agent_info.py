"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_id
    import capo_application_discovery_service.types.agent_network_info_list
    import capo_application_discovery_service.types.agent_status
    import capo_application_discovery_service.types.string


class AgentInfo(TypedDict, closed=True):
    agent_id: NotRequired["capo_application_discovery_service.types.agent_id.AgentId"]
    """<p>The agent or collector ID.</p>"""
    host_name: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>The name of the host where the agent or collector resides. The host can be a server or virtual machine.</p>"""
    agent_network_info_list: NotRequired[
        "capo_application_discovery_service.types.agent_network_info_list.AgentNetworkInfoList"
    ]
    """<p>Network details about the host where the agent or collector resides.</p>"""
    connector_id: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>The ID of the connector.</p>"""
    version: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>The agent or collector version.</p>"""
    health: NotRequired[
        "capo_application_discovery_service.types.agent_status.AgentStatus"
    ]
    """<p>The health of the agent.</p>"""
    last_health_ping_time: NotRequired[
        "capo_application_discovery_service.types.string.String"
    ]
    """<p>Time since agent health was reported.</p>"""
    collection_status: NotRequired[
        "capo_application_discovery_service.types.string.String"
    ]
    """<p>Status of the collection process for an agent.</p>"""
    agent_type: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>Type of agent.</p>"""
    registered_time: NotRequired[
        "capo_application_discovery_service.types.string.String"
    ]
    """<p>Agent's first registration timestamp in UTC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentInfo) -> dict:
    out: dict = {}
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "agent_network_info_list" in value:
        import capo_application_discovery_service.types.agent_network_info_list

        out["agentNetworkInfoList"] = (
            capo_application_discovery_service.types.agent_network_info_list.serialize_aws_json_1_1(
                value["agent_network_info_list"]
            )
        )
    if "connector_id" in value:
        out["connectorId"] = value["connector_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "health" in value:
        import capo_application_discovery_service.types.agent_status

        out["health"] = (
            capo_application_discovery_service.types.agent_status.serialize_aws_json_1_1(
                value["health"]
            )
        )
    if "last_health_ping_time" in value:
        out["lastHealthPingTime"] = value["last_health_ping_time"]
    if "collection_status" in value:
        out["collectionStatus"] = value["collection_status"]
    if "agent_type" in value:
        out["agentType"] = value["agent_type"]
    if "registered_time" in value:
        out["registeredTime"] = value["registered_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentInfo:
    out: AgentInfo = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    if data.get("hostName") is not None:
        out["host_name"] = data["hostName"]
    if data.get("agentNetworkInfoList") is not None:
        import capo_application_discovery_service.types.agent_network_info_list

        out["agent_network_info_list"] = (
            capo_application_discovery_service.types.agent_network_info_list.deserialize_aws_json_1_1(
                data["agentNetworkInfoList"]
            )
        )
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("health") is not None:
        import capo_application_discovery_service.types.agent_status

        out["health"] = (
            capo_application_discovery_service.types.agent_status.deserialize_aws_json_1_1(
                data["health"]
            )
        )
    if data.get("lastHealthPingTime") is not None:
        out["last_health_ping_time"] = data["lastHealthPingTime"]
    if data.get("collectionStatus") is not None:
        out["collection_status"] = data["collectionStatus"]
    if data.get("agentType") is not None:
        out["agent_type"] = data["agentType"]
    if data.get("registeredTime") is not None:
        out["registered_time"] = data["registeredTime"]
    return out


def redact_sensitive(value: AgentInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_network_info_list" in value:
        import capo_application_discovery_service.types.agent_network_info_list

        out["agent_network_info_list"] = (
            capo_application_discovery_service.types.agent_network_info_list.redact_sensitive(
                value["agent_network_info_list"]
            )
        )
    return out
