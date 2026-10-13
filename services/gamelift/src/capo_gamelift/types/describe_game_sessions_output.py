"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeGameSessionsOutput(TypedDict, closed=True):
    game_sessions: NotRequired["capo_gamelift.types.game_session_list.GameSessionList"]
    """<p>A collection of properties for each game session that matches the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionsOutput) -> dict:
    out: dict = {}
    if "game_sessions" in value:
        import capo_gamelift.types.game_session_list

        out["GameSessions"] = (
            capo_gamelift.types.game_session_list.serialize_aws_json_1_1(
                value["game_sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionsOutput:
    out: DescribeGameSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessions") is not None:
        import capo_gamelift.types.game_session_list

        out["game_sessions"] = (
            capo_gamelift.types.game_session_list.deserialize_aws_json_1_1(
                data["GameSessions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeGameSessionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_sessions" in value:
        import capo_gamelift.types.game_session_list

        out["game_sessions"] = capo_gamelift.types.game_session_list.redact_sensitive(
            value["game_sessions"]
        )
    return out
