"""Generated from Smithy shape ``com.amazonaws.gamelift#ListGameServerGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_groups
    import capo_gamelift.types.non_zero_and_max_string


class ListGameServerGroupsOutput(TypedDict, closed=True):
    game_server_groups: NotRequired[
        "capo_gamelift.types.game_server_groups.GameServerGroups"
    ]
    """<p>The game server groups' game server groups.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGameServerGroupsOutput) -> dict:
    out: dict = {}
    if "game_server_groups" in value:
        import capo_gamelift.types.game_server_groups

        out["GameServerGroups"] = (
            capo_gamelift.types.game_server_groups.serialize_aws_json_1_1(
                value["game_server_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGameServerGroupsOutput:
    out: ListGameServerGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroups") is not None:
        import capo_gamelift.types.game_server_groups

        out["game_server_groups"] = (
            capo_gamelift.types.game_server_groups.deserialize_aws_json_1_1(
                data["GameServerGroups"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGameServerGroupsOutput) -> dict:
    out: dict = {}
    if "game_server_groups" in value:
        import capo_gamelift.types.game_server_groups

        out["GameServerGroups"] = capo_gamelift.types.game_server_groups.serialize_cbor(
            value["game_server_groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGameServerGroupsOutput:
    out: ListGameServerGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroups") is not None:
        import capo_gamelift.types.game_server_groups

        out["game_server_groups"] = (
            capo_gamelift.types.game_server_groups.deserialize_cbor(
                data["GameServerGroups"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
