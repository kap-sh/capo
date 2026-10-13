"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_session

PlayerSessionList: TypeAlias = list["capo_gamelift.types.player_session.PlayerSession"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerSessionList) -> list:
    import capo_gamelift.types.player_session

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.player_session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerSessionList:
    import capo_gamelift.types.player_session

    out: PlayerSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.player_session.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: PlayerSessionList) -> list[Any]:
    import capo_gamelift.types.player_session

    return [capo_gamelift.types.player_session.redact_sensitive(item) for item in value]
