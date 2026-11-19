"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateFleetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_attributes
    import capo_gamelift.types.location_state_list


class CreateFleetOutput(TypedDict, closed=True):
    fleet_attributes: NotRequired[
        "capo_gamelift.types.fleet_attributes.FleetAttributes"
    ]
    """<p>The properties for the new fleet, including the current status. All fleets are placed in <code>NEW</code> status on creation. </p>"""
    location_states: NotRequired[
        "capo_gamelift.types.location_state_list.LocationStateList"
    ]
    """<p>The fleet's locations and life-cycle status of each location. For new fleets, the status of all locations is set to <code>NEW</code>. During fleet creation, Amazon GameLift Servers updates each location status as instances are deployed there and prepared for game hosting. This list includes an entry for the fleet's home Region. For fleets with no remote locations, only one entry, representing the home Region, is returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetOutput) -> dict:
    out: dict = {}
    if "fleet_attributes" in value:
        import capo_gamelift.types.fleet_attributes

        out["FleetAttributes"] = (
            capo_gamelift.types.fleet_attributes.serialize_aws_json_1_1(
                value["fleet_attributes"]
            )
        )
    if "location_states" in value:
        import capo_gamelift.types.location_state_list

        out["LocationStates"] = (
            capo_gamelift.types.location_state_list.serialize_aws_json_1_1(
                value["location_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetOutput:
    out: CreateFleetOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetAttributes") is not None:
        import capo_gamelift.types.fleet_attributes

        out["fleet_attributes"] = (
            capo_gamelift.types.fleet_attributes.deserialize_aws_json_1_1(
                data["FleetAttributes"]
            )
        )
    if data.get("LocationStates") is not None:
        import capo_gamelift.types.location_state_list

        out["location_states"] = (
            capo_gamelift.types.location_state_list.deserialize_aws_json_1_1(
                data["LocationStates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateFleetOutput) -> dict:
    out: dict = {}
    if "fleet_attributes" in value:
        import capo_gamelift.types.fleet_attributes

        out["FleetAttributes"] = capo_gamelift.types.fleet_attributes.serialize_cbor(
            value["fleet_attributes"]
        )
    if "location_states" in value:
        import capo_gamelift.types.location_state_list

        out["LocationStates"] = capo_gamelift.types.location_state_list.serialize_cbor(
            value["location_states"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateFleetOutput:
    out: CreateFleetOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetAttributes") is not None:
        import capo_gamelift.types.fleet_attributes

        out["fleet_attributes"] = capo_gamelift.types.fleet_attributes.deserialize_cbor(
            data["FleetAttributes"]
        )
    if data.get("LocationStates") is not None:
        import capo_gamelift.types.location_state_list

        out["location_states"] = (
            capo_gamelift.types.location_state_list.deserialize_cbor(
                data["LocationStates"]
            )
        )
    return out
