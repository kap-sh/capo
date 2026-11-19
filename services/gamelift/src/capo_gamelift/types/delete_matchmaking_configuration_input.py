"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteMatchmakingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_name


class DeleteMatchmakingConfigurationInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
    ]
    """<p>A unique identifier for the matchmaking configuration. You can use either the configuration name or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMatchmakingConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMatchmakingConfigurationInput:
    out: DeleteMatchmakingConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteMatchmakingConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> DeleteMatchmakingConfigurationInput:
    out: DeleteMatchmakingConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
