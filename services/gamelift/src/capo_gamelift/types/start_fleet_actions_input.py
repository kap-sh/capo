"""Generated from Smithy shape ``com.amazonaws.gamelift#StartFleetActionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_action_list
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model


class StartFleetActionsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to restart actions on. You can use either the fleet ID or ARN value.</p>"""
    actions: NotRequired["capo_gamelift.types.fleet_action_list.FleetActionList"]
    """<p>List of actions to restart on the fleet.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location to restart fleet actions for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFleetActionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["Actions"] = capo_gamelift.types.fleet_action_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFleetActionsInput:
    out: StartFleetActionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Actions") is not None:
        import capo_gamelift.types.fleet_action_list

        out["actions"] = capo_gamelift.types.fleet_action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartFleetActionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["Actions"] = capo_gamelift.types.fleet_action_list.serialize_cbor(
            value["actions"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_cbor(data: dict) -> StartFleetActionsInput:
    out: StartFleetActionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Actions") is not None:
        import capo_gamelift.types.fleet_action_list

        out["actions"] = capo_gamelift.types.fleet_action_list.deserialize_cbor(
            data["Actions"]
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
