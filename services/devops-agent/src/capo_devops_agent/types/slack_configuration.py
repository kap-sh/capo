"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.slack_bidirectional_configuration
    import capo_devops_agent.types.slack_transmission_target


class SlackConfiguration(TypedDict, closed=True):
    workspace_id: "str"
    """<p>Associated Slack workspace ID</p>"""
    workspace_name: "str"
    """<p>Associated Slack workspace name</p>"""
    transmission_target: (
        "capo_devops_agent.types.slack_transmission_target.SlackTransmissionTarget"
    )
    """<p>Transmission targets for agent notifications</p>"""
    bidirectional: NotRequired[
        "capo_devops_agent.types.slack_bidirectional_configuration.SlackBidirectionalConfiguration"
    ]
    """<p>Optional bidirectional communication configuration. Supply this configuration and set enabled to true so you can interact with the agent directly from Slack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackConfiguration) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["workspaceName"] = value["workspace_name"]
    import capo_devops_agent.types.slack_transmission_target

    out["transmissionTarget"] = (
        capo_devops_agent.types.slack_transmission_target.serialize_json(
            value["transmission_target"]
        )
    )
    if "bidirectional" in value:
        import capo_devops_agent.types.slack_bidirectional_configuration

        out["bidirectional"] = (
            capo_devops_agent.types.slack_bidirectional_configuration.serialize_json(
                value["bidirectional"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlackConfiguration:
    out: SlackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("transmissionTarget") is not None:
        import capo_devops_agent.types.slack_transmission_target

        out["transmission_target"] = (
            capo_devops_agent.types.slack_transmission_target.deserialize_json(
                data["transmissionTarget"]
            )
        )
    else:
        raise DeserializationError("SlackConfiguration.transmission_target required")
    if data.get("bidirectional") is not None:
        import capo_devops_agent.types.slack_bidirectional_configuration

        out["bidirectional"] = (
            capo_devops_agent.types.slack_bidirectional_configuration.deserialize_json(
                data["bidirectional"]
            )
        )
    return out
