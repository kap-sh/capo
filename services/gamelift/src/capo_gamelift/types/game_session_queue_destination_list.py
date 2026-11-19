"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue_destination

GameSessionQueueDestinationList: TypeAlias = list[
    "capo_gamelift.types.game_session_queue_destination.GameSessionQueueDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueDestinationList) -> list:
    import capo_gamelift.types.game_session_queue_destination

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.game_session_queue_destination.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionQueueDestinationList:
    import capo_gamelift.types.game_session_queue_destination

    out: GameSessionQueueDestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.game_session_queue_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameSessionQueueDestinationList) -> list:
    import capo_gamelift.types.game_session_queue_destination

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.game_session_queue_destination.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> GameSessionQueueDestinationList:
    import capo_gamelift.types.game_session_queue_destination

    out: GameSessionQueueDestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.game_session_queue_destination.deserialize_cbor(item)
        )
    return out
