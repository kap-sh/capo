"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribePlayerSessionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_session_list


class DescribePlayerSessionsOutput(TypedDict, closed=True):
    player_sessions: NotRequired[
        "capo_gamelift.types.player_session_list.PlayerSessionList"
    ]
    """<p>A collection of objects containing properties for each player session that matches the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePlayerSessionsOutput) -> dict:
    out: dict = {}
    if "player_sessions" in value:
        import capo_gamelift.types.player_session_list

        out["PlayerSessions"] = (
            capo_gamelift.types.player_session_list.serialize_aws_json_1_1(
                value["player_sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePlayerSessionsOutput:
    out: DescribePlayerSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("PlayerSessions") is not None:
        import capo_gamelift.types.player_session_list

        out["player_sessions"] = (
            capo_gamelift.types.player_session_list.deserialize_aws_json_1_1(
                data["PlayerSessions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribePlayerSessionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_sessions" in value:
        import capo_gamelift.types.player_session_list

        out["player_sessions"] = (
            capo_gamelift.types.player_session_list.redact_sensitive(
                value["player_sessions"]
            )
        )
    return out
