"""Generated from Smithy shape ``com.amazonaws.gamelift#ClaimGameServerInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.claim_filter_option
    import capo_gamelift.types.game_server_data
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.game_server_id


class ClaimGameServerInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group where the game server is running. If you are not specifying a game server to claim, this value identifies where you want Amazon GameLift Servers FleetIQ to look for an available game server to claim. </p>"""
    game_server_id: NotRequired["capo_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server to claim. If this parameter is left empty, Amazon GameLift Servers FleetIQ searches for an available game server in the specified game server group.</p>"""
    game_server_data: NotRequired["capo_gamelift.types.game_server_data.GameServerData"]
    """<p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>"""
    filter_option: NotRequired[
        "capo_gamelift.types.claim_filter_option.ClaimFilterOption"
    ]
    """<p>Object that restricts how a claimed game server is chosen.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClaimGameServerInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    if "game_server_data" in value:
        out["GameServerData"] = value["game_server_data"]
    if "filter_option" in value:
        import capo_gamelift.types.claim_filter_option

        out["FilterOption"] = (
            capo_gamelift.types.claim_filter_option.serialize_aws_json_1_1(
                value["filter_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClaimGameServerInput:
    out: ClaimGameServerInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("GameServerId") is not None:
        out["game_server_id"] = data["GameServerId"]
    if data.get("GameServerData") is not None:
        out["game_server_data"] = data["GameServerData"]
    if data.get("FilterOption") is not None:
        import capo_gamelift.types.claim_filter_option

        out["filter_option"] = (
            capo_gamelift.types.claim_filter_option.deserialize_aws_json_1_1(
                data["FilterOption"]
            )
        )
    return out


def redact_sensitive(value: ClaimGameServerInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_server_data" in value:
        out["game_server_data"] = "*** Sensitive Data Redacted ***"
    return out
