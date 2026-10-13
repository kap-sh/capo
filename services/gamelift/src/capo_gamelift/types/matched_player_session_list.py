"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchedPlayerSessionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matched_player_session

MatchedPlayerSessionList: TypeAlias = list[
    "capo_gamelift.types.matched_player_session.MatchedPlayerSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchedPlayerSessionList) -> list:
    import capo_gamelift.types.matched_player_session

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.matched_player_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchedPlayerSessionList:
    import capo_gamelift.types.matched_player_session

    out: MatchedPlayerSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.matched_player_session.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MatchedPlayerSessionList) -> list[Any]:
    import capo_gamelift.types.matched_player_session

    return [
        capo_gamelift.types.matched_player_session.redact_sensitive(item)
        for item in value
    ]
