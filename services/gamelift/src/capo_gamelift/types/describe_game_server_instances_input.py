"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameServerInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.game_server_instance_ids
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeGameServerInstancesInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    instance_ids: NotRequired[
        "capo_gamelift.types.game_server_instance_ids.GameServerInstanceIds"
    ]
    """<p>The Amazon EC2 instance IDs that you want to retrieve status on. Amazon EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>. To retrieve all instances in the game server group, leave this parameter empty. </p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameServerInstancesInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "instance_ids" in value:
        import capo_gamelift.types.game_server_instance_ids

        out["InstanceIds"] = (
            capo_gamelift.types.game_server_instance_ids.serialize_aws_json_1_1(
                value["instance_ids"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameServerInstancesInput:
    out: DescribeGameServerInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("InstanceIds") is not None:
        import capo_gamelift.types.game_server_instance_ids

        out["instance_ids"] = (
            capo_gamelift.types.game_server_instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeGameServerInstancesInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "instance_ids" in value:
        import capo_gamelift.types.game_server_instance_ids

        out["InstanceIds"] = (
            capo_gamelift.types.game_server_instance_ids.serialize_cbor(
                value["instance_ids"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeGameServerInstancesInput:
    out: DescribeGameServerInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("InstanceIds") is not None:
        import capo_gamelift.types.game_server_instance_ids

        out["instance_ids"] = (
            capo_gamelift.types.game_server_instance_ids.deserialize_cbor(
                data["InstanceIds"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
