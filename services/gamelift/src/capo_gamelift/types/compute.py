"""Generated from Smithy shape ``com.amazonaws.gamelift#Compute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_arn
    import capo_gamelift.types.compute_name
    import capo_gamelift.types.compute_status
    import capo_gamelift.types.container_attributes
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.game_lift_agent_endpoint_output
    import capo_gamelift.types.game_lift_service_sdk_endpoint_output
    import capo_gamelift.types.instance_id
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.operating_system
    import capo_gamelift.types.timestamp


class Compute(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that the compute belongs to.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (ARN) of the fleet that the compute belongs to.</p>"""
    compute_name: NotRequired["capo_gamelift.types.compute_name.ComputeName"]
    """<p>A descriptive label for the compute resource. For instances in a managed EC2 fleet, the compute name is the same value as the <code>InstanceId</code> ID.</p>"""
    compute_arn: NotRequired["capo_gamelift.types.compute_arn.ComputeArn"]
    """<p>The ARN that is assigned to a compute resource and uniquely identifies it. ARNs are unique across locations. Instances in managed EC2 fleets are not assigned a Compute ARN.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of a compute resource. Amazon GameLift Servers requires a DNS name or IP address for a compute.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS name of a compute resource. Amazon GameLift Servers requires a DNS name or IP address for a compute.</p>"""
    compute_status: NotRequired["capo_gamelift.types.compute_status.ComputeStatus"]
    """<p>Current status of the compute. A compute must have an <code>ACTIVE</code> status to host game sessions. Valid values include <code>PENDING</code>, <code>ACTIVE</code>, <code>TERMINATING</code>, and <code>IMPAIRED</code>.</p> <note> <p>While the ComputeStatus enum type is valid for Container based servers, the result may also include other non-enumerated string values such as "Active" for fleets which are not Container-based.</p> </note>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The name of the custom location you added to the fleet that this compute resource resides in.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>The type of operating system on the compute resource.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    type: NotRequired["capo_gamelift.types.ec2_instance_type.EC2InstanceType"]
    """<p>The Amazon EC2 instance type that the fleet uses. For registered computes in an Amazon GameLift Servers Anywhere fleet, this property is empty. </p>"""
    game_lift_service_sdk_endpoint: NotRequired[
        "capo_gamelift.types.game_lift_service_sdk_endpoint_output.GameLiftServiceSdkEndpointOutput"
    ]
    """<p>The Amazon GameLift Servers SDK endpoint connection for a registered compute resource in an Anywhere fleet. The game servers on the compute use this endpoint to connect to the Amazon GameLift Servers service.</p>"""
    game_lift_agent_endpoint: NotRequired[
        "capo_gamelift.types.game_lift_agent_endpoint_output.GameLiftAgentEndpointOutput"
    ]
    """<p> The endpoint of the Amazon GameLift Servers Agent. </p>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p> The <code>InstanceID</code> of the EC2 instance that is hosting the compute. </p>"""
    container_attributes: NotRequired[
        "capo_gamelift.types.container_attributes.ContainerAttributes"
    ]
    """<p>A set of attributes for each container in the compute. </p>"""
    game_server_container_group_definition_arn: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The game server container group definition for the compute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Compute) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "compute_arn" in value:
        out["ComputeArn"] = value["compute_arn"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "compute_status" in value:
        import capo_gamelift.types.compute_status

        out["ComputeStatus"] = (
            capo_gamelift.types.compute_status.serialize_aws_json_1_1(
                value["compute_status"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "operating_system" in value:
        import capo_gamelift.types.operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["Type"] = capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "game_lift_service_sdk_endpoint" in value:
        out["GameLiftServiceSdkEndpoint"] = value["game_lift_service_sdk_endpoint"]
    if "game_lift_agent_endpoint" in value:
        out["GameLiftAgentEndpoint"] = value["game_lift_agent_endpoint"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "container_attributes" in value:
        import capo_gamelift.types.container_attributes

        out["ContainerAttributes"] = (
            capo_gamelift.types.container_attributes.serialize_aws_json_1_1(
                value["container_attributes"]
            )
        )
    if "game_server_container_group_definition_arn" in value:
        out["GameServerContainerGroupDefinitionArn"] = value[
            "game_server_container_group_definition_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> Compute:
    out: Compute = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("ComputeArn") is not None:
        out["compute_arn"] = data["ComputeArn"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("ComputeStatus") is not None:
        import capo_gamelift.types.compute_status

        out["compute_status"] = (
            capo_gamelift.types.compute_status.deserialize_aws_json_1_1(
                data["ComputeStatus"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.operating_system

        out["operating_system"] = (
            capo_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("Type") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["type"] = capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("GameLiftServiceSdkEndpoint") is not None:
        out["game_lift_service_sdk_endpoint"] = data["GameLiftServiceSdkEndpoint"]
    if data.get("GameLiftAgentEndpoint") is not None:
        out["game_lift_agent_endpoint"] = data["GameLiftAgentEndpoint"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContainerAttributes") is not None:
        import capo_gamelift.types.container_attributes

        out["container_attributes"] = (
            capo_gamelift.types.container_attributes.deserialize_aws_json_1_1(
                data["ContainerAttributes"]
            )
        )
    if data.get("GameServerContainerGroupDefinitionArn") is not None:
        out["game_server_container_group_definition_arn"] = data[
            "GameServerContainerGroupDefinitionArn"
        ]
    return out
