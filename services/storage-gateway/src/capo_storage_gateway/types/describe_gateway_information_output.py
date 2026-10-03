"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeGatewayInformationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cloud_watch_log_group_arn
    import capo_storage_gateway.types.deprecation_date
    import capo_storage_gateway.types.ec2_instance_id
    import capo_storage_gateway.types.ec2_instance_region
    import capo_storage_gateway.types.endpoint_type
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.gateway_capacity
    import capo_storage_gateway.types.gateway_id
    import capo_storage_gateway.types.gateway_network_interfaces
    import capo_storage_gateway.types.gateway_state
    import capo_storage_gateway.types.gateway_timezone
    import capo_storage_gateway.types.gateway_type
    import capo_storage_gateway.types.host_environment
    import capo_storage_gateway.types.host_environment_id
    import capo_storage_gateway.types.last_software_update
    import capo_storage_gateway.types.next_update_availability_date
    import capo_storage_gateway.types.software_updates_end_date
    import capo_storage_gateway.types.software_version
    import capo_storage_gateway.types.string
    import capo_storage_gateway.types.supported_gateway_capacities
    import capo_storage_gateway.types.tags


class DescribeGatewayInformationOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    gateway_id: NotRequired["capo_storage_gateway.types.gateway_id.GatewayId"]
    """<p>The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.</p>"""
    gateway_name: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The name you configured for your gateway.</p>"""
    gateway_timezone: NotRequired[
        "capo_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone configured for the gateway.</p>"""
    gateway_state: NotRequired["capo_storage_gateway.types.gateway_state.GatewayState"]
    """<p>A value that indicates the operating state of the gateway.</p>"""
    gateway_network_interfaces: NotRequired[
        "capo_storage_gateway.types.gateway_network_interfaces.GatewayNetworkInterfaces"
    ]
    """<p>A <a>NetworkInterface</a> array that contains descriptions of the gateway network interfaces.</p>"""
    gateway_type: NotRequired["capo_storage_gateway.types.gateway_type.GatewayType"]
    """<p>The type of the gateway.</p> <important> <p>Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit <a href="https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/">this blog post</a>.</p> </important>"""
    next_update_availability_date: NotRequired[
        "capo_storage_gateway.types.next_update_availability_date.NextUpdateAvailabilityDate"
    ]
    """<p>The date on which an update to the gateway is available. This date is in the time zone of the gateway. If the gateway is not available for an update this field is not returned in the response.</p>"""
    last_software_update: NotRequired[
        "capo_storage_gateway.types.last_software_update.LastSoftwareUpdate"
    ]
    """<p>The date on which the last software update was applied to the gateway. If the gateway has never been updated, this field does not return a value in the response. This only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM</p>"""
    ec2_instance_id: NotRequired[
        "capo_storage_gateway.types.ec2_instance_id.Ec2InstanceId"
    ]
    """<p>The ID of the Amazon EC2 instance that was used to launch the gateway.</p>"""
    ec2_instance_region: NotRequired[
        "capo_storage_gateway.types.ec2_instance_region.Ec2InstanceRegion"
    ]
    """<p>The Amazon Web Services Region where the Amazon EC2 instance is located.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the <code>ListTagsForResource</code> API operation.</p>"""
    vpc_endpoint: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The configuration settings for the virtual private cloud (VPC) endpoint for your gateway.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_storage_gateway.types.cloud_watch_log_group_arn.CloudWatchLogGroupARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor events in the gateway. This field only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM</p>"""
    host_environment: NotRequired[
        "capo_storage_gateway.types.host_environment.HostEnvironment"
    ]
    """<p>The type of hardware or software platform on which the gateway is running.</p> <note> <p>Tape Gateway is no longer available on Snow Family devices.</p> </note>"""
    endpoint_type: NotRequired["capo_storage_gateway.types.endpoint_type.EndpointType"]
    """<p>The type of endpoint for your gateway.</p> <p>Valid Values: <code>STANDARD</code> | <code>FIPS</code> </p>"""
    software_updates_end_date: NotRequired[
        "capo_storage_gateway.types.software_updates_end_date.SoftwareUpdatesEndDate"
    ]
    """<p>Date after which this gateway will not receive software updates for new features.</p>"""
    deprecation_date: NotRequired[
        "capo_storage_gateway.types.deprecation_date.DeprecationDate"
    ]
    """<p>Date after which this gateway will not receive software updates for new features and bug fixes.</p>"""
    gateway_capacity: NotRequired[
        "capo_storage_gateway.types.gateway_capacity.GatewayCapacity"
    ]
    """<p>Specifies the size of the gateway's metadata cache.</p>"""
    supported_gateway_capacities: NotRequired[
        "capo_storage_gateway.types.supported_gateway_capacities.SupportedGatewayCapacities"
    ]
    """<p>A list of the metadata cache sizes that the gateway can support based on its current hardware specifications.</p>"""
    host_environment_id: NotRequired[
        "capo_storage_gateway.types.host_environment_id.HostEnvironmentId"
    ]
    """<p>A unique identifier for the specific instance of the host platform running the gateway. This value is only available for certain host environments, and its format depends on the host environment type.</p>"""
    software_version: NotRequired[
        "capo_storage_gateway.types.software_version.SoftwareVersion"
    ]
    """<p>The version number of the software running on the gateway appliance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayInformationOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    if "gateway_timezone" in value:
        out["GatewayTimezone"] = value["gateway_timezone"]
    if "gateway_state" in value:
        out["GatewayState"] = value["gateway_state"]
    if "gateway_network_interfaces" in value:
        import capo_storage_gateway.types.gateway_network_interfaces

        out["GatewayNetworkInterfaces"] = (
            capo_storage_gateway.types.gateway_network_interfaces.serialize_aws_json_1_1(
                value["gateway_network_interfaces"]
            )
        )
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "next_update_availability_date" in value:
        out["NextUpdateAvailabilityDate"] = value["next_update_availability_date"]
    if "last_software_update" in value:
        out["LastSoftwareUpdate"] = value["last_software_update"]
    if "ec2_instance_id" in value:
        out["Ec2InstanceId"] = value["ec2_instance_id"]
    if "ec2_instance_region" in value:
        out["Ec2InstanceRegion"] = value["ec2_instance_region"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_endpoint" in value:
        out["VPCEndpoint"] = value["vpc_endpoint"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupARN"] = value["cloud_watch_log_group_arn"]
    if "host_environment" in value:
        import capo_storage_gateway.types.host_environment

        out["HostEnvironment"] = (
            capo_storage_gateway.types.host_environment.serialize_aws_json_1_1(
                value["host_environment"]
            )
        )
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "software_updates_end_date" in value:
        out["SoftwareUpdatesEndDate"] = value["software_updates_end_date"]
    if "deprecation_date" in value:
        out["DeprecationDate"] = value["deprecation_date"]
    if "gateway_capacity" in value:
        import capo_storage_gateway.types.gateway_capacity

        out["GatewayCapacity"] = (
            capo_storage_gateway.types.gateway_capacity.serialize_aws_json_1_1(
                value["gateway_capacity"]
            )
        )
    if "supported_gateway_capacities" in value:
        import capo_storage_gateway.types.supported_gateway_capacities

        out["SupportedGatewayCapacities"] = (
            capo_storage_gateway.types.supported_gateway_capacities.serialize_aws_json_1_1(
                value["supported_gateway_capacities"]
            )
        )
    if "host_environment_id" in value:
        out["HostEnvironmentId"] = value["host_environment_id"]
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayInformationOutput:
    out: DescribeGatewayInformationOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    if data.get("GatewayId") is not None:
        out["gateway_id"] = data["GatewayId"]
    if data.get("GatewayName") is not None:
        out["gateway_name"] = data["GatewayName"]
    if data.get("GatewayTimezone") is not None:
        out["gateway_timezone"] = data["GatewayTimezone"]
    if data.get("GatewayState") is not None:
        out["gateway_state"] = data["GatewayState"]
    if data.get("GatewayNetworkInterfaces") is not None:
        import capo_storage_gateway.types.gateway_network_interfaces

        out["gateway_network_interfaces"] = (
            capo_storage_gateway.types.gateway_network_interfaces.deserialize_aws_json_1_1(
                data["GatewayNetworkInterfaces"]
            )
        )
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    if data.get("NextUpdateAvailabilityDate") is not None:
        out["next_update_availability_date"] = data["NextUpdateAvailabilityDate"]
    if data.get("LastSoftwareUpdate") is not None:
        out["last_software_update"] = data["LastSoftwareUpdate"]
    if data.get("Ec2InstanceId") is not None:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    if data.get("Ec2InstanceRegion") is not None:
        out["ec2_instance_region"] = data["Ec2InstanceRegion"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("VPCEndpoint") is not None:
        out["vpc_endpoint"] = data["VPCEndpoint"]
    if data.get("CloudWatchLogGroupARN") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupARN"]
    if data.get("HostEnvironment") is not None:
        import capo_storage_gateway.types.host_environment

        out["host_environment"] = (
            capo_storage_gateway.types.host_environment.deserialize_aws_json_1_1(
                data["HostEnvironment"]
            )
        )
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    if data.get("SoftwareUpdatesEndDate") is not None:
        out["software_updates_end_date"] = data["SoftwareUpdatesEndDate"]
    if data.get("DeprecationDate") is not None:
        out["deprecation_date"] = data["DeprecationDate"]
    if data.get("GatewayCapacity") is not None:
        import capo_storage_gateway.types.gateway_capacity

        out["gateway_capacity"] = (
            capo_storage_gateway.types.gateway_capacity.deserialize_aws_json_1_1(
                data["GatewayCapacity"]
            )
        )
    if data.get("SupportedGatewayCapacities") is not None:
        import capo_storage_gateway.types.supported_gateway_capacities

        out["supported_gateway_capacities"] = (
            capo_storage_gateway.types.supported_gateway_capacities.deserialize_aws_json_1_1(
                data["SupportedGatewayCapacities"]
            )
        )
    if data.get("HostEnvironmentId") is not None:
        out["host_environment_id"] = data["HostEnvironmentId"]
    if data.get("SoftwareVersion") is not None:
        out["software_version"] = data["SoftwareVersion"]
    return out
