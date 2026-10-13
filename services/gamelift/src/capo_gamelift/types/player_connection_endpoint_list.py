"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerConnectionEndpointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_connection_endpoint

PlayerConnectionEndpointList: TypeAlias = list[
    "capo_gamelift.types.player_connection_endpoint.PlayerConnectionEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerConnectionEndpointList) -> list:
    import capo_gamelift.types.player_connection_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.player_connection_endpoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerConnectionEndpointList:
    import capo_gamelift.types.player_connection_endpoint

    out: PlayerConnectionEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.player_connection_endpoint.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: PlayerConnectionEndpointList) -> list[Any]:
    import capo_gamelift.types.player_connection_endpoint

    return [
        capo_gamelift.types.player_connection_endpoint.redact_sensitive(item)
        for item in value
    ]
