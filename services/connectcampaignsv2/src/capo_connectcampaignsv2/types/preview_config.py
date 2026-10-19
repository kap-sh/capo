"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PreviewConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agent_actions
    import capo_connectcampaignsv2.types.bandwidth_allocation
    import capo_connectcampaignsv2.types.timeout_config


class PreviewConfig(TypedDict, closed=True):
    bandwidth_allocation: (
        "capo_connectcampaignsv2.types.bandwidth_allocation.BandwidthAllocation"
    )
    timeout_config: "capo_connectcampaignsv2.types.timeout_config.TimeoutConfig"
    agent_actions: NotRequired[
        "capo_connectcampaignsv2.types.agent_actions.AgentActions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PreviewConfig) -> dict:
    out: dict = {}
    out["bandwidthAllocation"] = (
        "NaN"
        if value["bandwidth_allocation"] != value["bandwidth_allocation"]
        else "Infinity"
        if value["bandwidth_allocation"] == float("inf")
        else "-Infinity"
        if value["bandwidth_allocation"] == float("-inf")
        else value["bandwidth_allocation"]
    )
    import capo_connectcampaignsv2.types.timeout_config

    out["timeoutConfig"] = capo_connectcampaignsv2.types.timeout_config.serialize_json(
        value["timeout_config"]
    )
    if "agent_actions" in value:
        import capo_connectcampaignsv2.types.agent_actions

        out["agentActions"] = (
            capo_connectcampaignsv2.types.agent_actions.serialize_json(
                value["agent_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PreviewConfig:
    out: PreviewConfig = {}  # type: ignore[typeddict-item]
    if data.get("bandwidthAllocation") is not None:
        out["bandwidth_allocation"] = float(data["bandwidthAllocation"])
    else:
        out["bandwidth_allocation"] = 0.0
    if data.get("timeoutConfig") is not None:
        import capo_connectcampaignsv2.types.timeout_config

        out["timeout_config"] = (
            capo_connectcampaignsv2.types.timeout_config.deserialize_json(
                data["timeoutConfig"]
            )
        )
    else:
        raise DeserializationError("PreviewConfig.timeout_config required")
    if data.get("agentActions") is not None:
        import capo_connectcampaignsv2.types.agent_actions

        out["agent_actions"] = (
            capo_connectcampaignsv2.types.agent_actions.deserialize_json(
                data["agentActions"]
            )
        )
    return out
