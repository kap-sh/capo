"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionQueuesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeGameSessionQueuesOutput(TypedDict, closed=True):
    game_session_queues: NotRequired[
        "capo_gamelift.types.game_session_queue_list.GameSessionQueueList"
    ]
    """<p>A collection of objects that describe the requested game session queues.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionQueuesOutput) -> dict:
    out: dict = {}
    if "game_session_queues" in value:
        import capo_gamelift.types.game_session_queue_list

        out["GameSessionQueues"] = (
            capo_gamelift.types.game_session_queue_list.serialize_aws_json_1_1(
                value["game_session_queues"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionQueuesOutput:
    out: DescribeGameSessionQueuesOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionQueues") is not None:
        import capo_gamelift.types.game_session_queue_list

        out["game_session_queues"] = (
            capo_gamelift.types.game_session_queue_list.deserialize_aws_json_1_1(
                data["GameSessionQueues"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeGameSessionQueuesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session_queues" in value:
        import capo_gamelift.types.game_session_queue_list

        out["game_session_queues"] = (
            capo_gamelift.types.game_session_queue_list.redact_sensitive(
                value["game_session_queues"]
            )
        )
    return out
