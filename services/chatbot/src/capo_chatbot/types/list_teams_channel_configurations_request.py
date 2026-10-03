"""Generated from Smithy shape ``com.amazonaws.chatbot#ListTeamsChannelConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.max_results
    import capo_chatbot.types.pagination_token
    import capo_chatbot.types.uuid


class ListTeamsChannelConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_chatbot.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    team_id: NotRequired["capo_chatbot.types.uuid.UUID"]
    """<p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTeamsChannelConfigurationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "team_id" in value:
        out["TeamId"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> ListTeamsChannelConfigurationsRequest:
    out: ListTeamsChannelConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TeamId") is not None:
        out["team_id"] = data["TeamId"]
    return out
