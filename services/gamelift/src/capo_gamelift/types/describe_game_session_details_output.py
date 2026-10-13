"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionDetailsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_detail_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeGameSessionDetailsOutput(TypedDict, closed=True):
    game_session_details: NotRequired[
        "capo_gamelift.types.game_session_detail_list.GameSessionDetailList"
    ]
    """<p>A collection of properties for each game session that matches the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionDetailsOutput) -> dict:
    out: dict = {}
    if "game_session_details" in value:
        import capo_gamelift.types.game_session_detail_list

        out["GameSessionDetails"] = (
            capo_gamelift.types.game_session_detail_list.serialize_aws_json_1_1(
                value["game_session_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionDetailsOutput:
    out: DescribeGameSessionDetailsOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionDetails") is not None:
        import capo_gamelift.types.game_session_detail_list

        out["game_session_details"] = (
            capo_gamelift.types.game_session_detail_list.deserialize_aws_json_1_1(
                data["GameSessionDetails"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeGameSessionDetailsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session_details" in value:
        import capo_gamelift.types.game_session_detail_list

        out["game_session_details"] = (
            capo_gamelift.types.game_session_detail_list.redact_sensitive(
                value["game_session_details"]
            )
        )
    return out
