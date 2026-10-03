"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteTeamsConfiguredTeamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.uuid


class DeleteTeamsConfiguredTeamRequest(TypedDict, closed=True):
    team_id: "capo_chatbot.types.uuid.UUID"
    """<p>The ID of the Microsoft Teams team authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTeamsConfiguredTeamRequest) -> dict:
    out: dict = {}
    out["TeamId"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> DeleteTeamsConfiguredTeamRequest:
    out: DeleteTeamsConfiguredTeamRequest = {}  # type: ignore[typeddict-item]
    if data.get("TeamId") is not None:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError("DeleteTeamsConfiguredTeamRequest.team_id required")
    return out
