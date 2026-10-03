"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ec2_instance_counts
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.game_server_container_group_counts
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.managed_capacity_configuration


class FleetCapacity(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet associated with the location.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    instance_type: NotRequired["capo_gamelift.types.ec2_instance_type.EC2InstanceType"]
    """<p>The Amazon EC2 instance type that is used for instances in a fleet. Instance type determines the computing resources in use, including CPU, memory, storage, and networking capacity. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions.</p>"""
    instance_counts: NotRequired[
        "capo_gamelift.types.ec2_instance_counts.EC2InstanceCounts"
    ]
    """<p>The current number of instances in the fleet, listed by instance status. Counts for pending and terminating instances might be non-zero if the fleet is adjusting to a scaling event or if access to resources is temporarily affected.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location for the instance count information, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""
    game_server_container_group_counts: NotRequired[
        "capo_gamelift.types.game_server_container_group_counts.GameServerContainerGroupCounts"
    ]
    """<p>The number and status of game server container groups deployed in a container fleet. </p>"""
    managed_capacity_configuration: NotRequired[
        "capo_gamelift.types.managed_capacity_configuration.ManagedCapacityConfiguration"
    ]
    """<p>Configuration settings for managed capacity scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetCapacity) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "instance_type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["InstanceType"] = (
            capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_counts" in value:
        import capo_gamelift.types.ec2_instance_counts

        out["InstanceCounts"] = (
            capo_gamelift.types.ec2_instance_counts.serialize_aws_json_1_1(
                value["instance_counts"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    if "game_server_container_group_counts" in value:
        import capo_gamelift.types.game_server_container_group_counts

        out["GameServerContainerGroupCounts"] = (
            capo_gamelift.types.game_server_container_group_counts.serialize_aws_json_1_1(
                value["game_server_container_group_counts"]
            )
        )
    if "managed_capacity_configuration" in value:
        import capo_gamelift.types.managed_capacity_configuration

        out["ManagedCapacityConfiguration"] = (
            capo_gamelift.types.managed_capacity_configuration.serialize_aws_json_1_1(
                value["managed_capacity_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetCapacity:
    out: FleetCapacity = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("InstanceType") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["instance_type"] = (
            capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCounts") is not None:
        import capo_gamelift.types.ec2_instance_counts

        out["instance_counts"] = (
            capo_gamelift.types.ec2_instance_counts.deserialize_aws_json_1_1(
                data["InstanceCounts"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("GameServerContainerGroupCounts") is not None:
        import capo_gamelift.types.game_server_container_group_counts

        out["game_server_container_group_counts"] = (
            capo_gamelift.types.game_server_container_group_counts.deserialize_aws_json_1_1(
                data["GameServerContainerGroupCounts"]
            )
        )
    if data.get("ManagedCapacityConfiguration") is not None:
        import capo_gamelift.types.managed_capacity_configuration

        out["managed_capacity_configuration"] = (
            capo_gamelift.types.managed_capacity_configuration.deserialize_aws_json_1_1(
                data["ManagedCapacityConfiguration"]
            )
        )
    return out
