"""Generated from Smithy shape ``com.amazonaws.gamelift#StartMatchmakingInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_name
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.player_list


class StartMatchmakingInput(TypedDict, closed=True):
    ticket_id: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.</p>"""
    configuration_name: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
    ]
    """<p>Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.</p>"""
    players: NotRequired["capo_gamelift.types.player_list.PlayerList"]
    """<p>Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, <code>Player</code> objects contain the name of the team the player is assigned to.</p> <p>You can include up to 10 <code>Players</code> in a <code>StartMatchmaking</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMatchmakingInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "players" in value:
        import capo_gamelift.types.player_list

        out["Players"] = capo_gamelift.types.player_list.serialize_aws_json_1_1(
            value["players"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMatchmakingInput:
    out: StartMatchmakingInput = {}  # type: ignore[typeddict-item]
    if data.get("TicketId") is not None:
        out["ticket_id"] = data["TicketId"]
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
    if data.get("Players") is not None:
        import capo_gamelift.types.player_list

        out["players"] = capo_gamelift.types.player_list.deserialize_aws_json_1_1(
            data["Players"]
        )
    return out


def redact_sensitive(value: StartMatchmakingInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "players" in value:
        import capo_gamelift.types.player_list

        out["players"] = capo_gamelift.types.player_list.redact_sensitive(
            value["players"]
        )
    return out
