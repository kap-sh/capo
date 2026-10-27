"""Generated from Smithy shape ``com.amazonaws.connect#GetTrafficDistributionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.acgr_traffic_distribution_group_arn
    import capo_connect.types.acgr_traffic_distribution_group_id
    import capo_connect.types.agent_config
    import capo_connect.types.sign_in_config
    import capo_connect.types.telephony_config
    import capo_connect.types.timestamp


class GetTrafficDistributionResponse(TypedDict, closed=True):
    telephony_config: NotRequired["capo_connect.types.telephony_config.TelephonyConfig"]
    """<p>The distribution of traffic between the instance and its replicas.</p>"""
    id: NotRequired[
        "capo_connect.types.acgr_traffic_distribution_group_id.ACGRTrafficDistributionGroupId"
    ]
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.</p>"""
    arn: NotRequired[
        "capo_connect.types.acgr_traffic_distribution_group_arn.ACGRTrafficDistributionGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic distribution group.</p>"""
    sign_in_config: NotRequired["capo_connect.types.sign_in_config.SignInConfig"]
    """<p>The distribution that determines which Amazon Web Services Regions should be used to sign in agents in to both the instance and its replica(s).</p>"""
    agent_config: NotRequired["capo_connect.types.agent_config.AgentConfig"]
    """<p>The distribution of agents between the instance and its replica(s).</p>"""
    last_failover_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp of the most recent failover for the traffic distribution group. This value is updated each time <code>UpdateTrafficDistribution</code> is called to change the traffic distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrafficDistributionResponse) -> dict:
    out: dict = {}
    if "telephony_config" in value:
        import capo_connect.types.telephony_config

        out["TelephonyConfig"] = capo_connect.types.telephony_config.serialize_json(
            value["telephony_config"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "sign_in_config" in value:
        import capo_connect.types.sign_in_config

        out["SignInConfig"] = capo_connect.types.sign_in_config.serialize_json(
            value["sign_in_config"]
        )
    if "agent_config" in value:
        import capo_connect.types.agent_config

        out["AgentConfig"] = capo_connect.types.agent_config.serialize_json(
            value["agent_config"]
        )
    if "last_failover_time" in value:
        import capo_connect.types.timestamp

        out["LastFailoverTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_failover_time"]
        )
    return out


def deserialize_json(data: dict) -> GetTrafficDistributionResponse:
    out: GetTrafficDistributionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TelephonyConfig") is not None:
        import capo_connect.types.telephony_config

        out["telephony_config"] = capo_connect.types.telephony_config.deserialize_json(
            data["TelephonyConfig"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("SignInConfig") is not None:
        import capo_connect.types.sign_in_config

        out["sign_in_config"] = capo_connect.types.sign_in_config.deserialize_json(
            data["SignInConfig"]
        )
    if data.get("AgentConfig") is not None:
        import capo_connect.types.agent_config

        out["agent_config"] = capo_connect.types.agent_config.deserialize_json(
            data["AgentConfig"]
        )
    if data.get("LastFailoverTime") is not None:
        import capo_connect.types.timestamp

        out["last_failover_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastFailoverTime"]
        )
    return out
