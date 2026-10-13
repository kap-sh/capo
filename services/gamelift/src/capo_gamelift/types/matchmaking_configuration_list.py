"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration

MatchmakingConfigurationList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_configuration.MatchmakingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingConfigurationList) -> list:
    import capo_gamelift.types.matchmaking_configuration

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.matchmaking_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchmakingConfigurationList:
    import capo_gamelift.types.matchmaking_configuration

    out: MatchmakingConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.matchmaking_configuration.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MatchmakingConfigurationList) -> list[Any]:
    import capo_gamelift.types.matchmaking_configuration

    return [
        capo_gamelift.types.matchmaking_configuration.redact_sensitive(item)
        for item in value
    ]
