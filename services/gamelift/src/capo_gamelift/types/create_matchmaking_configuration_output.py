"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingConfigurationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration


class CreateMatchmakingConfigurationOutput(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_gamelift.types.matchmaking_configuration.MatchmakingConfiguration"
    ]
    """<p>Object that describes the newly created matchmaking configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingConfigurationOutput) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_gamelift.types.matchmaking_configuration

        out["Configuration"] = (
            capo_gamelift.types.matchmaking_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingConfigurationOutput:
    out: CreateMatchmakingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_gamelift.types.matchmaking_configuration

        out["configuration"] = (
            capo_gamelift.types.matchmaking_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out


def redact_sensitive(value: CreateMatchmakingConfigurationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_gamelift.types.matchmaking_configuration

        out["configuration"] = (
            capo_gamelift.types.matchmaking_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
