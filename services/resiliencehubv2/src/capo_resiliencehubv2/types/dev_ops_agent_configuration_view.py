"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentConfigurationView``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.dev_ops_agent_connection_status
    import capo_resiliencehubv2.types.dev_ops_agent_region
    import capo_resiliencehubv2.types.dev_ops_agent_space_arn
    import capo_resiliencehubv2.types.dev_ops_agent_space_id


class DevOpsAgentConfigurationView(TypedDict, closed=True):
    agent_space_arn: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_space_arn.DevOpsAgentSpaceArn"
    ]
    """<p>The ARN of the linked DevOps Agent Agent Space.</p>"""
    agent_space_id: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_space_id.DevOpsAgentSpaceId"
    ]
    """<p>The identifier of the linked DevOps Agent Agent Space.</p>"""
    region: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_region.DevOpsAgentRegion"
    ]
    """<p>The AWS Region of the linked DevOps Agent Agent Space.</p>"""
    status: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_connection_status.DevOpsAgentConnectionStatus"
    ]
    """<p>The connection status of the DevOps Agent integration for this service. Valid values:</p> <ul> <li> <p>CONNECTING - The service is being connected to the Agent Space.</p> </li> <li> <p>CONNECTED - The service is connected to the Agent Space.</p> </li> <li> <p>DISCONNECTED - The service is not connected to an Agent Space.</p> </li> <li> <p>FAILED - The connection attempt failed. See statusReason for details.</p> </li> </ul>"""
    operator_app_url: NotRequired["str"]
    """<p>The URL of the DevOps Agent Operator App for the linked Agent Space. This URL is present when the connection status is CONNECTED.</p>"""
    connected_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service successfully connected to the DevOps Agent Agent Space.</p>"""
    status_reason: NotRequired["str"]
    """<p>A human-readable explanation of the current connection status. This field explains the status when the connection fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentConfigurationView) -> dict:
    out: dict = {}
    if "agent_space_arn" in value:
        out["agentSpaceArn"] = value["agent_space_arn"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "status" in value:
        import capo_resiliencehubv2.types.dev_ops_agent_connection_status

        out["status"] = (
            capo_resiliencehubv2.types.dev_ops_agent_connection_status.serialize_json(
                value["status"]
            )
        )
    if "operator_app_url" in value:
        out["operatorAppUrl"] = value["operator_app_url"]
    if "connected_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["connectedAt"] = (
            capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["connected_at"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DevOpsAgentConfigurationView:
    out: DevOpsAgentConfigurationView = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceArn") is not None:
        out["agent_space_arn"] = data["agentSpaceArn"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.dev_ops_agent_connection_status

        out["status"] = (
            capo_resiliencehubv2.types.dev_ops_agent_connection_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("operatorAppUrl") is not None:
        out["operator_app_url"] = data["operatorAppUrl"]
    if data.get("connectedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["connected_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["connectedAt"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
