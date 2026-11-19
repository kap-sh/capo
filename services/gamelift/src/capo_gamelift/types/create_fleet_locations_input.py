"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateFleetLocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_configuration_list


class CreateFleetLocationsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to add locations to. You can use either the fleet ID or ARN value.</p>"""
    locations: NotRequired[
        "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
    ]
    """<p>A list of locations to deploy additional instances to and manage as part of the fleet. You can add any Amazon GameLift Servers-supported Amazon Web Services Region as a remote location, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetLocationsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "locations" in value:
        import capo_gamelift.types.location_configuration_list

        out["Locations"] = (
            capo_gamelift.types.location_configuration_list.serialize_aws_json_1_1(
                value["locations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetLocationsInput:
    out: CreateFleetLocationsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_configuration_list

        out["locations"] = (
            capo_gamelift.types.location_configuration_list.deserialize_aws_json_1_1(
                data["Locations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateFleetLocationsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "locations" in value:
        import capo_gamelift.types.location_configuration_list

        out["Locations"] = (
            capo_gamelift.types.location_configuration_list.serialize_cbor(
                value["locations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateFleetLocationsInput:
    out: CreateFleetLocationsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_configuration_list

        out["locations"] = (
            capo_gamelift.types.location_configuration_list.deserialize_cbor(
                data["Locations"]
            )
        )
    return out
