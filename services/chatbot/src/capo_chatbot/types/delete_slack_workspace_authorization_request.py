"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteSlackWorkspaceAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.slack_team_id


class DeleteSlackWorkspaceAuthorizationRequest(TypedDict, closed=True):
    slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with AWS Chatbot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackWorkspaceAuthorizationRequest) -> dict:
    out: dict = {}
    out["SlackTeamId"] = value["slack_team_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackWorkspaceAuthorizationRequest:
    out: DeleteSlackWorkspaceAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SlackTeamId") is not None:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        out["slack_team_id"] = ""
    return out
