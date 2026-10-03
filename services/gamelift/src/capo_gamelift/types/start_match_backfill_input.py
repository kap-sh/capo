"""Generated from Smithy shape ``com.amazonaws.gamelift#StartMatchBackfillInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.matchmaking_configuration_name
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.player_list


class StartMatchBackfillInput(TypedDict, closed=True):
    ticket_id: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.</p>"""
    configuration_name: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
    ]
    """<p>Name of the matchmaker to use for this request. You can use either the configuration name or ARN value. The ARN of the matchmaker that was used with the original game session is listed in the <code>GameSession</code> object, <code>MatchmakerData</code> property.</p>"""
    game_session_arn: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. When using FlexMatch as a standalone matchmaking solution, this parameter is not needed. </p>"""
    players: NotRequired["capo_gamelift.types.player_list.PlayerList"]
    """<p>Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.</p> <p>You can include up to 199 <code>Players</code> in a <code>StartMatchBackfill</code> request.</p> <ul> <li> <p>PlayerID, PlayerAttributes, Team -- This information is maintained in the <code>GameSession</code> object, <code>MatchmakerData</code> property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data"> Match Data</a>. </p> <p>The backfill request must specify the team membership for every player. Do not specify team if you are not using backfill.</p> </li> <li> <p>LatencyInMs -- If the matchmaker uses player latency, include a latency value, in milliseconds, for the Region that the game session is currently in. Do not include latency values for any other Region.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMatchBackfillInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "game_session_arn" in value:
        out["GameSessionArn"] = value["game_session_arn"]
    if "players" in value:
        import capo_gamelift.types.player_list

        out["Players"] = capo_gamelift.types.player_list.serialize_aws_json_1_1(
            value["players"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMatchBackfillInput:
    out: StartMatchBackfillInput = {}  # type: ignore[typeddict-item]
    if data.get("TicketId") is not None:
        out["ticket_id"] = data["TicketId"]
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
    if data.get("GameSessionArn") is not None:
        out["game_session_arn"] = data["GameSessionArn"]
    if data.get("Players") is not None:
        import capo_gamelift.types.player_list

        out["players"] = capo_gamelift.types.player_list.deserialize_aws_json_1_1(
            data["Players"]
        )
    return out
