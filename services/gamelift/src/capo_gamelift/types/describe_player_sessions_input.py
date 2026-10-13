"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribePlayerSessionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_id
    import capo_gamelift.types.player_session_id
    import capo_gamelift.types.positive_integer


class DescribePlayerSessionsInput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions to retrieve player sessions for. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player to retrieve player sessions for.</p>"""
    player_session_id: NotRequired[
        "capo_gamelift.types.player_session_id.PlayerSessionId"
    ]
    """<p>A unique identifier for a player session to retrieve.</p>"""
    player_session_status_filter: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Player session status to filter results on. Note that when a PlayerSessionId or PlayerId is provided in a DescribePlayerSessions request, then the PlayerSessionStatusFilter has no effect on the response.</p> <p>Possible player session statuses include the following:</p> <ul> <li> <p> <b>RESERVED</b> -- The player session request has been received, but the player has not yet connected to the server process and/or been validated. </p> </li> <li> <p> <b>ACTIVE</b> -- The player has been validated by the server process and is currently connected.</p> </li> <li> <p> <b>COMPLETED</b> -- The player connection has been dropped.</p> </li> <li> <p> <b>TIMEDOUT</b> -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).</p> </li> </ul>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePlayerSessionsInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_session_id" in value:
        out["PlayerSessionId"] = value["player_session_id"]
    if "player_session_status_filter" in value:
        out["PlayerSessionStatusFilter"] = value["player_session_status_filter"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePlayerSessionsInput:
    out: DescribePlayerSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("PlayerId") is not None:
        out["player_id"] = data["PlayerId"]
    if data.get("PlayerSessionId") is not None:
        out["player_session_id"] = data["PlayerSessionId"]
    if data.get("PlayerSessionStatusFilter") is not None:
        out["player_session_status_filter"] = data["PlayerSessionStatusFilter"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribePlayerSessionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_id" in value:
        out["player_id"] = "*** Sensitive Data Redacted ***"
    return out
