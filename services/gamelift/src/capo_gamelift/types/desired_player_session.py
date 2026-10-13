"""Generated from Smithy shape ``com.amazonaws.gamelift#DesiredPlayerSession``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.player_data
    import capo_gamelift.types.player_id


class DesiredPlayerSession(TypedDict, closed=True):
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player to associate with the player session.</p>"""
    player_data: NotRequired["capo_gamelift.types.player_data.PlayerData"]
    """<p>Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DesiredPlayerSession) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_data" in value:
        out["PlayerData"] = value["player_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DesiredPlayerSession:
    out: DesiredPlayerSession = {}  # type: ignore[typeddict-item]
    if data.get("PlayerId") is not None:
        out["player_id"] = data["PlayerId"]
    if data.get("PlayerData") is not None:
        out["player_data"] = data["PlayerData"]
    return out


def redact_sensitive(value: DesiredPlayerSession) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_id" in value:
        out["player_id"] = "*** Sensitive Data Redacted ***"
    if "player_data" in value:
        out["player_data"] = "*** Sensitive Data Redacted ***"
    return out
