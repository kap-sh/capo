"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerLatencyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_latency

PlayerLatencyList: TypeAlias = list["capo_gamelift.types.player_latency.PlayerLatency"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerLatencyList) -> list:
    import capo_gamelift.types.player_latency

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.player_latency.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerLatencyList:
    import capo_gamelift.types.player_latency

    out: PlayerLatencyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.player_latency.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: PlayerLatencyList) -> list[Any]:
    import capo_gamelift.types.player_latency

    return [capo_gamelift.types.player_latency.redact_sensitive(item) for item in value]
