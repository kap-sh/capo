"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateFleetLocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_state_list


class CreateFleetLocationsOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that was updated with new locations.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. </p>"""
    location_states: NotRequired[
        "capo_gamelift.types.location_state_list.LocationStateList"
    ]
    """<p>The remote locations that are being added to the fleet, and the life-cycle status of each location. For new locations, the status is set to <code>NEW</code>. During location creation, Amazon GameLift Servers updates each location's status as instances are deployed there and prepared for game hosting. This list does not include the fleet home Region or any remote locations that were already added to the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetLocationsOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location_states" in value:
        import capo_gamelift.types.location_state_list

        out["LocationStates"] = (
            capo_gamelift.types.location_state_list.serialize_aws_json_1_1(
                value["location_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetLocationsOutput:
    out: CreateFleetLocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("LocationStates") is not None:
        import capo_gamelift.types.location_state_list

        out["location_states"] = (
            capo_gamelift.types.location_state_list.deserialize_aws_json_1_1(
                data["LocationStates"]
            )
        )
    return out
