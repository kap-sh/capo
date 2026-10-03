"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateFleetCapacityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.managed_capacity_configuration


class UpdateFleetCapacityOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that was updated.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. </p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The remote location being updated, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    managed_capacity_configuration: NotRequired[
        "capo_gamelift.types.managed_capacity_configuration.ManagedCapacityConfiguration"
    ]
    """<p>Configuration for Amazon GameLift Servers-managed capacity scaling options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location" in value:
        out["Location"] = value["location"]
    if "managed_capacity_configuration" in value:
        import capo_gamelift.types.managed_capacity_configuration

        out["ManagedCapacityConfiguration"] = (
            capo_gamelift.types.managed_capacity_configuration.serialize_aws_json_1_1(
                value["managed_capacity_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetCapacityOutput:
    out: UpdateFleetCapacityOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ManagedCapacityConfiguration") is not None:
        import capo_gamelift.types.managed_capacity_configuration

        out["managed_capacity_configuration"] = (
            capo_gamelift.types.managed_capacity_configuration.deserialize_aws_json_1_1(
                data["ManagedCapacityConfiguration"]
            )
        )
    return out
