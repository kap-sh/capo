"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupPortMappingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name
    import capo_gamelift.types.container_group_definition_arn
    import capo_gamelift.types.container_group_port_mapping_list
    import capo_gamelift.types.container_group_type
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.instance_id
    import capo_gamelift.types.location_string_model


class DescribeContainerGroupPortMappingsOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the container fleet.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. In a GameLift fleet ARN, the resource ID matches the <code>FleetId</code> value.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The location of the fleet instance, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    container_group_definition_arn: NotRequired[
        "capo_gamelift.types.container_group_definition_arn.ContainerGroupDefinitionArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to the container group definition. The ARN value also identifies the specific container group definition version in use.</p>"""
    container_group_type: NotRequired[
        "capo_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group that was specified in the request. Valid values are <code>GAME_SERVER</code> or <code>PER_INSTANCE</code>.</p>"""
    compute_name: NotRequired["capo_gamelift.types.compute_name.ComputeName"]
    """<p>A unique identifier for the compute resource running the game server container group. Returned when <code>ContainerGroupType</code> is <code>GAME_SERVER</code>.</p>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the fleet instance. For <code>GAME_SERVER</code> requests, this is the instance running the specified compute. For <code>PER_INSTANCE</code> requests, this is the instance specified in the request.</p>"""
    container_group_port_mappings: NotRequired[
        "capo_gamelift.types.container_group_port_mapping_list.ContainerGroupPortMappingList"
    ]
    """<p>A list of <code>ContainerGroupPortMapping</code> objects that describe the port mappings for each container in the container group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupPortMappingsOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location" in value:
        out["Location"] = value["location"]
    if "container_group_definition_arn" in value:
        out["ContainerGroupDefinitionArn"] = value["container_group_definition_arn"]
    if "container_group_type" in value:
        import capo_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            capo_gamelift.types.container_group_type.serialize_aws_json_1_1(
                value["container_group_type"]
            )
        )
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "container_group_port_mappings" in value:
        import capo_gamelift.types.container_group_port_mapping_list

        out["ContainerGroupPortMappings"] = (
            capo_gamelift.types.container_group_port_mapping_list.serialize_aws_json_1_1(
                value["container_group_port_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupPortMappingsOutput:
    out: DescribeContainerGroupPortMappingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ContainerGroupDefinitionArn") is not None:
        out["container_group_definition_arn"] = data["ContainerGroupDefinitionArn"]
    if data.get("ContainerGroupType") is not None:
        import capo_gamelift.types.container_group_type

        out["container_group_type"] = (
            capo_gamelift.types.container_group_type.deserialize_aws_json_1_1(
                data["ContainerGroupType"]
            )
        )
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContainerGroupPortMappings") is not None:
        import capo_gamelift.types.container_group_port_mapping_list

        out["container_group_port_mappings"] = (
            capo_gamelift.types.container_group_port_mapping_list.deserialize_aws_json_1_1(
                data["ContainerGroupPortMappings"]
            )
        )
    return out
