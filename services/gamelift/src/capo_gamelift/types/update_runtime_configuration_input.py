"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateRuntimeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.runtime_configuration


class UpdateRuntimeConfigurationInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to update runtime configuration for. You can use either the fleet ID or ARN value.</p>"""
    runtime_configuration: NotRequired[
        "capo_gamelift.types.runtime_configuration.RuntimeConfiguration"
    ]
    """<p>Instructions for launching server processes on fleet computes. Server processes run either a custom game build executable or a Amazon GameLift Servers Realtime script. The runtime configuration lists the types of server processes to run, how to launch them, and the number of processes to run concurrently.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuntimeConfigurationInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "runtime_configuration" in value:
        import capo_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            capo_gamelift.types.runtime_configuration.serialize_aws_json_1_1(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuntimeConfigurationInput:
    out: UpdateRuntimeConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("RuntimeConfiguration") is not None:
        import capo_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            capo_gamelift.types.runtime_configuration.deserialize_aws_json_1_1(
                data["RuntimeConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateRuntimeConfigurationInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "runtime_configuration" in value:
        import capo_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            capo_gamelift.types.runtime_configuration.serialize_cbor(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateRuntimeConfigurationInput:
    out: UpdateRuntimeConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("RuntimeConfiguration") is not None:
        import capo_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            capo_gamelift.types.runtime_configuration.deserialize_cbor(
                data["RuntimeConfiguration"]
            )
        )
    return out
