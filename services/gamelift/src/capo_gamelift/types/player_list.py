"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player

PlayerList: TypeAlias = list["capo_gamelift.types.player.Player"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerList) -> list:
    import capo_gamelift.types.player

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.player.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerList:
    import capo_gamelift.types.player

    out: PlayerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.player.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: PlayerList) -> list[Any]:
    import capo_gamelift.types.player

    return [capo_gamelift.types.player.redact_sensitive(item) for item in value]
