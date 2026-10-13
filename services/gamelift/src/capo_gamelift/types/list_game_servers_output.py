"""Generated from Smithy shape ``com.amazonaws.gamelift#ListGameServersOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_servers
    import capo_gamelift.types.non_zero_and_max_string


class ListGameServersOutput(TypedDict, closed=True):
    game_servers: NotRequired["capo_gamelift.types.game_servers.GameServers"]
    """<p>A collection of game server objects that match the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGameServersOutput) -> dict:
    out: dict = {}
    if "game_servers" in value:
        import capo_gamelift.types.game_servers

        out["GameServers"] = capo_gamelift.types.game_servers.serialize_aws_json_1_1(
            value["game_servers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGameServersOutput:
    out: ListGameServersOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServers") is not None:
        import capo_gamelift.types.game_servers

        out["game_servers"] = capo_gamelift.types.game_servers.deserialize_aws_json_1_1(
            data["GameServers"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListGameServersOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_servers" in value:
        import capo_gamelift.types.game_servers

        out["game_servers"] = capo_gamelift.types.game_servers.redact_sensitive(
            value["game_servers"]
        )
    return out
