"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerConnectionDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_connection_detail

PlayerConnectionDetailList: TypeAlias = list[
    "capo_gamelift.types.player_connection_detail.PlayerConnectionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerConnectionDetailList) -> list:
    import capo_gamelift.types.player_connection_detail

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.player_connection_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerConnectionDetailList:
    import capo_gamelift.types.player_connection_detail

    out: PlayerConnectionDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.player_connection_detail.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: PlayerConnectionDetailList) -> list[Any]:
    import capo_gamelift.types.player_connection_detail

    return [
        capo_gamelift.types.player_connection_detail.redact_sensitive(item)
        for item in value
    ]
