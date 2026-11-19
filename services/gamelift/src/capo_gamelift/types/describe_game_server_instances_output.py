"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameServerInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_instances
    import capo_gamelift.types.non_zero_and_max_string


class DescribeGameServerInstancesOutput(TypedDict, closed=True):
    game_server_instances: NotRequired[
        "capo_gamelift.types.game_server_instances.GameServerInstances"
    ]
    """<p>The collection of requested game server instances.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameServerInstancesOutput) -> dict:
    out: dict = {}
    if "game_server_instances" in value:
        import capo_gamelift.types.game_server_instances

        out["GameServerInstances"] = (
            capo_gamelift.types.game_server_instances.serialize_aws_json_1_1(
                value["game_server_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameServerInstancesOutput:
    out: DescribeGameServerInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerInstances") is not None:
        import capo_gamelift.types.game_server_instances

        out["game_server_instances"] = (
            capo_gamelift.types.game_server_instances.deserialize_aws_json_1_1(
                data["GameServerInstances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeGameServerInstancesOutput) -> dict:
    out: dict = {}
    if "game_server_instances" in value:
        import capo_gamelift.types.game_server_instances

        out["GameServerInstances"] = (
            capo_gamelift.types.game_server_instances.serialize_cbor(
                value["game_server_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeGameServerInstancesOutput:
    out: DescribeGameServerInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerInstances") is not None:
        import capo_gamelift.types.game_server_instances

        out["game_server_instances"] = (
            capo_gamelift.types.game_server_instances.deserialize_cbor(
                data["GameServerInstances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
