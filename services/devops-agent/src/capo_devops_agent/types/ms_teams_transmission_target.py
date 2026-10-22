"""Generated from Smithy shape ``com.amazonaws.devopsagent#MSTeamsTransmissionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.ms_teams_channel


class MSTeamsTransmissionTarget(TypedDict, closed=True):
    ops_oncall_target: NotRequired[
        "capo_devops_agent.types.ms_teams_channel.MSTeamsChannel"
    ]
    """<p>The Microsoft Teams channel that receives notifications from the On-call Agent.</p>"""
    ops_sre_target: NotRequired[
        "capo_devops_agent.types.ms_teams_channel.MSTeamsChannel"
    ]
    """<p>The Microsoft Teams channel that receives notifications from the SRE Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MSTeamsTransmissionTarget) -> dict:
    out: dict = {}
    if "ops_oncall_target" in value:
        import capo_devops_agent.types.ms_teams_channel

        out["opsOncallTarget"] = (
            capo_devops_agent.types.ms_teams_channel.serialize_json(
                value["ops_oncall_target"]
            )
        )
    if "ops_sre_target" in value:
        import capo_devops_agent.types.ms_teams_channel

        out["opsSRETarget"] = capo_devops_agent.types.ms_teams_channel.serialize_json(
            value["ops_sre_target"]
        )
    return out


def deserialize_json(data: dict) -> MSTeamsTransmissionTarget:
    out: MSTeamsTransmissionTarget = {}  # type: ignore[typeddict-item]
    if data.get("opsOncallTarget") is not None:
        import capo_devops_agent.types.ms_teams_channel

        out["ops_oncall_target"] = (
            capo_devops_agent.types.ms_teams_channel.deserialize_json(
                data["opsOncallTarget"]
            )
        )
    if data.get("opsSRETarget") is not None:
        import capo_devops_agent.types.ms_teams_channel

        out["ops_sre_target"] = (
            capo_devops_agent.types.ms_teams_channel.deserialize_json(
                data["opsSRETarget"]
            )
        )
    return out
