"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteFleetLocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_state_list


class DeleteFleetLocationsOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that location attributes are being deleted for.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    location_states: NotRequired[
        "capo_gamelift.types.location_state_list.LocationStateList"
    ]
    """<p>The remote locations that are being deleted, with each location status set to <code>DELETING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetLocationsOutput) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetLocationsOutput:
    out: DeleteFleetLocationsOutput = {}  # type: ignore[typeddict-item]
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
