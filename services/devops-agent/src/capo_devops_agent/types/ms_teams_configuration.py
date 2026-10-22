"""Generated from Smithy shape ``com.amazonaws.devopsagent#MSTeamsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.guid
    import capo_devops_agent.types.ms_teams_transmission_target


class MSTeamsConfiguration(TypedDict, closed=True):
    team_id: "capo_devops_agent.types.guid.Guid"
    """<p>The identifier of the Microsoft Teams team to connect to the DevOps Agent service.</p>"""
    team_name: "str"
    """<p>The name of the Microsoft Teams team to connect to the DevOps Agent service.</p>"""
    transmission_target: (
        "capo_devops_agent.types.ms_teams_transmission_target.MSTeamsTransmissionTarget"
    )
    """<p>The Microsoft Teams channels that receive agent notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MSTeamsConfiguration) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["teamName"] = value["team_name"]
    import capo_devops_agent.types.ms_teams_transmission_target

    out["transmissionTarget"] = (
        capo_devops_agent.types.ms_teams_transmission_target.serialize_json(
            value["transmission_target"]
        )
    )
    return out


def deserialize_json(data: dict) -> MSTeamsConfiguration:
    out: MSTeamsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("teamId") is not None:
        out["team_id"] = data["teamId"]
    else:
        out["team_id"] = ""
    if data.get("teamName") is not None:
        out["team_name"] = data["teamName"]
    else:
        out["team_name"] = ""
    if data.get("transmissionTarget") is not None:
        import capo_devops_agent.types.ms_teams_transmission_target

        out["transmission_target"] = (
            capo_devops_agent.types.ms_teams_transmission_target.deserialize_json(
                data["transmissionTarget"]
            )
        )
    else:
        raise DeserializationError("MSTeamsConfiguration.transmission_target required")
    return out
