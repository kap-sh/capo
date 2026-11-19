"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_action_list
    import capo_gamelift.types.location_state
    import capo_gamelift.types.location_update_status


class LocationAttributes(TypedDict, closed=True):
    location_state: NotRequired["capo_gamelift.types.location_state.LocationState"]
    """<p>A fleet location and its current life-cycle state.</p>"""
    stopped_actions: NotRequired[
        "capo_gamelift.types.fleet_action_list.FleetActionList"
    ]
    """<p>A list of fleet actions that have been suspended in the fleet location.</p>"""
    update_status: NotRequired[
        "capo_gamelift.types.location_update_status.LocationUpdateStatus"
    ]
    """<p>The status of fleet activity updates to the location. The status <code>PENDING_UPDATE</code> indicates that <code>StopFleetActions</code> or <code>StartFleetActions</code> has been requested but the update has not yet been completed for the location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationAttributes) -> dict:
    out: dict = {}
    if "location_state" in value:
        import capo_gamelift.types.location_state

        out["LocationState"] = (
            capo_gamelift.types.location_state.serialize_aws_json_1_1(
                value["location_state"]
            )
        )
    if "stopped_actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["StoppedActions"] = (
            capo_gamelift.types.fleet_action_list.serialize_aws_json_1_1(
                value["stopped_actions"]
            )
        )
    if "update_status" in value:
        import capo_gamelift.types.location_update_status

        out["UpdateStatus"] = (
            capo_gamelift.types.location_update_status.serialize_aws_json_1_1(
                value["update_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationAttributes:
    out: LocationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("LocationState") is not None:
        import capo_gamelift.types.location_state

        out["location_state"] = (
            capo_gamelift.types.location_state.deserialize_aws_json_1_1(
                data["LocationState"]
            )
        )
    if data.get("StoppedActions") is not None:
        import capo_gamelift.types.fleet_action_list

        out["stopped_actions"] = (
            capo_gamelift.types.fleet_action_list.deserialize_aws_json_1_1(
                data["StoppedActions"]
            )
        )
    if data.get("UpdateStatus") is not None:
        import capo_gamelift.types.location_update_status

        out["update_status"] = (
            capo_gamelift.types.location_update_status.deserialize_aws_json_1_1(
                data["UpdateStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationAttributes) -> dict:
    out: dict = {}
    if "location_state" in value:
        import capo_gamelift.types.location_state

        out["LocationState"] = capo_gamelift.types.location_state.serialize_cbor(
            value["location_state"]
        )
    if "stopped_actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["StoppedActions"] = capo_gamelift.types.fleet_action_list.serialize_cbor(
            value["stopped_actions"]
        )
    if "update_status" in value:
        import capo_gamelift.types.location_update_status

        out["UpdateStatus"] = capo_gamelift.types.location_update_status.serialize_cbor(
            value["update_status"]
        )
    return out


def deserialize_cbor(data: dict) -> LocationAttributes:
    out: LocationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("LocationState") is not None:
        import capo_gamelift.types.location_state

        out["location_state"] = capo_gamelift.types.location_state.deserialize_cbor(
            data["LocationState"]
        )
    if data.get("StoppedActions") is not None:
        import capo_gamelift.types.fleet_action_list

        out["stopped_actions"] = capo_gamelift.types.fleet_action_list.deserialize_cbor(
            data["StoppedActions"]
        )
    if data.get("UpdateStatus") is not None:
        import capo_gamelift.types.location_update_status

        out["update_status"] = (
            capo_gamelift.types.location_update_status.deserialize_cbor(
                data["UpdateStatus"]
            )
        )
    return out
