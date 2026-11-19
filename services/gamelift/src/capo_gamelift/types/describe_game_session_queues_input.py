"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionQueuesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue_name_or_arn_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeGameSessionQueuesInput(TypedDict, closed=True):
    names: NotRequired[
        "capo_gamelift.types.game_session_queue_name_or_arn_list.GameSessionQueueNameOrArnList"
    ]
    """<p>A list of queue names to retrieve information for. You can use either the queue ID or ARN value. To request settings for all queues, leave this parameter empty. </p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. You can request up to 50 results.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionQueuesInput) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_gamelift.types.game_session_queue_name_or_arn_list

        out["Names"] = (
            capo_gamelift.types.game_session_queue_name_or_arn_list.serialize_aws_json_1_1(
                value["names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionQueuesInput:
    out: DescribeGameSessionQueuesInput = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_gamelift.types.game_session_queue_name_or_arn_list

        out["names"] = (
            capo_gamelift.types.game_session_queue_name_or_arn_list.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeGameSessionQueuesInput) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_gamelift.types.game_session_queue_name_or_arn_list

        out["Names"] = (
            capo_gamelift.types.game_session_queue_name_or_arn_list.serialize_cbor(
                value["names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeGameSessionQueuesInput:
    out: DescribeGameSessionQueuesInput = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_gamelift.types.game_session_queue_name_or_arn_list

        out["names"] = (
            capo_gamelift.types.game_session_queue_name_or_arn_list.deserialize_cbor(
                data["Names"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
