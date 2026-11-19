"""Generated from Smithy shape ``com.amazonaws.gamelift#ListGameServersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.sort_order


class ListGameServersInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>An identifier for the game server group to retrieve a list of game servers from. Use either the name or ARN value.</p>"""
    sort_order: NotRequired["capo_gamelift.types.sort_order.SortOrder"]
    """<p>Indicates how to sort the returned data based on game server registration timestamp. Use <code>ASCENDING</code> to retrieve oldest game servers first, or use <code>DESCENDING</code> to retrieve newest game servers first. If this parameter is left empty, game servers are returned in no particular order.</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGameServersInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "sort_order" in value:
        import capo_gamelift.types.sort_order

        out["SortOrder"] = capo_gamelift.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGameServersInput:
    out: ListGameServersInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("SortOrder") is not None:
        import capo_gamelift.types.sort_order

        out["sort_order"] = capo_gamelift.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGameServersInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "sort_order" in value:
        import capo_gamelift.types.sort_order

        out["SortOrder"] = capo_gamelift.types.sort_order.serialize_cbor(
            value["sort_order"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGameServersInput:
    out: ListGameServersInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("SortOrder") is not None:
        import capo_gamelift.types.sort_order

        out["sort_order"] = capo_gamelift.types.sort_order.deserialize_cbor(
            data["SortOrder"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
