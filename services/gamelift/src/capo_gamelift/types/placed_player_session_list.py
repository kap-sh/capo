"""Generated from Smithy shape ``com.amazonaws.gamelift#PlacedPlayerSessionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.placed_player_session

PlacedPlayerSessionList: TypeAlias = list[
    "capo_gamelift.types.placed_player_session.PlacedPlayerSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacedPlayerSessionList) -> list:
    import capo_gamelift.types.placed_player_session

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.placed_player_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlacedPlayerSessionList:
    import capo_gamelift.types.placed_player_session

    out: PlacedPlayerSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.placed_player_session.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: PlacedPlayerSessionList) -> list[Any]:
    import capo_gamelift.types.placed_player_session

    return [
        capo_gamelift.types.placed_player_session.redact_sensitive(item)
        for item in value
    ]
