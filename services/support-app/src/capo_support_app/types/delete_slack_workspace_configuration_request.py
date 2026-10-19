"""Generated from Smithy shape ``com.amazonaws.supportapp#DeleteSlackWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.team_id


class DeleteSlackWorkspaceConfigurationRequest(TypedDict, closed=True):
    team_id: "capo_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackWorkspaceConfigurationRequest:
    out: DeleteSlackWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("teamId") is not None:
        out["team_id"] = data["teamId"]
    else:
        out["team_id"] = ""
    return out
