"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceLaunchTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.capacity_option_type
    import capo_ecs.types.capacity_reservation_request
    import capo_ecs.types.instance_requirements_request
    import capo_ecs.types.managed_instances_local_storage_configuration
    import capo_ecs.types.managed_instances_monitoring_options
    import capo_ecs.types.managed_instances_network_configuration
    import capo_ecs.types.managed_instances_storage_configuration
    import capo_ecs.types.string


class InstanceLaunchTemplate(TypedDict, closed=True):
    ec2_instance_profile_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the instance profile that Amazon ECS applies to Amazon ECS Managed Instances. This instance profile must include the necessary permissions for your tasks to access Amazon Web Services services and resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html">Amazon ECS instance profile for Managed Instances</a> in the <i>Amazon ECS Developer Guide</i>. </p>"""
    network_configuration: "capo_ecs.types.managed_instances_network_configuration.ManagedInstancesNetworkConfiguration"
    """<p>The network configuration for Amazon ECS Managed Instances. This specifies the subnets and security groups that instances use for network connectivity.</p>"""
    storage_configuration: NotRequired[
        "capo_ecs.types.managed_instances_storage_configuration.ManagedInstancesStorageConfiguration"
    ]
    """<p>The storage configuration for Amazon ECS Managed Instances. This defines the data volume properties for the instances.</p>"""
    local_storage_configuration: NotRequired[
        "capo_ecs.types.managed_instances_local_storage_configuration.ManagedInstancesLocalStorageConfiguration"
    ]
    """<p>The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses instance store volumes available on the container instance.</p>"""
    monitoring: NotRequired[
        "capo_ecs.types.managed_instances_monitoring_options.ManagedInstancesMonitoringOptions"
    ]
    """<p>CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html">Detailed monitoring for Amazon ECS Managed Instances</a> in the Amazon ECS Developer Guide.</p>"""
    capacity_option_type: NotRequired[
        "capo_ecs.types.capacity_option_type.CapacityOptionType"
    ]
    """<p>The capacity option type. This determines whether Amazon ECS launches On-Demand, Spot or Capacity Reservation Instances for your managed instance capacity provider.</p> <p>Valid values are:</p> <ul> <li> <p> <code>ON_DEMAND</code> - Launches standard On-Demand Instances. On-Demand Instances provide predictable pricing and availability.</p> </li> <li> <p> <code>SPOT</code> - Launches Spot Instances that use spare Amazon EC2 capacity at reduced cost. Spot Instances can be interrupted by Amazon EC2 with a two-minute notification when the capacity is needed back.</p> </li> <li> <p> <code>RESERVED</code> - Launches Instances using Amazon EC2 Capacity Reservations. Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone.</p> </li> </ul> <p>The default is On-Demand</p> <p>For more information about Amazon EC2 capacity options, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html">Instance purchasing options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_metadata_tags_propagation: NotRequired[
        "capo_ecs.types.boxed_boolean.BoxedBoolean"
    ]
    r"""<p>Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.</p> <p>Disable this setting if your tags contain characters that are not compatible with IMDS, such as <code>/</code>. IMDS requires tag keys to match the pattern <code>[0-9a-zA-Z\-_+=,.@:]{1,255}</code>.</p> <p>The default value is <code>true</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS">Work with instance tags in instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_requirements: NotRequired[
        "capo_ecs.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The instance requirements. You can specify:</p> <ul> <li> <p>The instance types</p> </li> <li> <p>Instance requirements such as vCPU count, memory, network performance, and accelerator specifications</p> </li> </ul> <p>Amazon ECS automatically selects the instances that match the specified criteria.</p>"""
    fips_enabled: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether to enable FIPS 140-2 validated cryptographic modules on EC2 instances launched by the capacity provider. If <code>true</code>, instances use FIPS-compliant cryptographic algorithms and modules for enhanced security compliance. If <code>false</code>, instances use standard cryptographic implementations.</p> <p>If not specified, instances are launched with FIPS enabled in Amazon Web Services GovCloud (US) regions and FIPS disabled in other regions.</p>"""
    capacity_reservations: NotRequired[
        "capo_ecs.types.capacity_reservation_request.CapacityReservationRequest"
    ]
    """<p>Capacity reservation specifications. You can specify:</p> <ul> <li> <p>Capacity reservation preference</p> </li> <li> <p>Reservation resource group to be used for targeted capacity reservations</p> </li> </ul> <p>Amazon ECS will launch instances according to the specified criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceLaunchTemplate) -> dict:
    out: dict = {}
    out["ec2InstanceProfileArn"] = value["ec2_instance_profile_arn"]
    import capo_ecs.types.managed_instances_network_configuration

    out["networkConfiguration"] = (
        capo_ecs.types.managed_instances_network_configuration.serialize_aws_json_1_1(
            value["network_configuration"]
        )
    )
    if "storage_configuration" in value:
        import capo_ecs.types.managed_instances_storage_configuration

        out["storageConfiguration"] = (
            capo_ecs.types.managed_instances_storage_configuration.serialize_aws_json_1_1(
                value["storage_configuration"]
            )
        )
    if "local_storage_configuration" in value:
        import capo_ecs.types.managed_instances_local_storage_configuration

        out["localStorageConfiguration"] = (
            capo_ecs.types.managed_instances_local_storage_configuration.serialize_aws_json_1_1(
                value["local_storage_configuration"]
            )
        )
    if "monitoring" in value:
        import capo_ecs.types.managed_instances_monitoring_options

        out["monitoring"] = (
            capo_ecs.types.managed_instances_monitoring_options.serialize_aws_json_1_1(
                value["monitoring"]
            )
        )
    if "capacity_option_type" in value:
        import capo_ecs.types.capacity_option_type

        out["capacityOptionType"] = (
            capo_ecs.types.capacity_option_type.serialize_aws_json_1_1(
                value["capacity_option_type"]
            )
        )
    if "instance_metadata_tags_propagation" in value:
        out["instanceMetadataTagsPropagation"] = value[
            "instance_metadata_tags_propagation"
        ]
    if "instance_requirements" in value:
        import capo_ecs.types.instance_requirements_request

        out["instanceRequirements"] = (
            capo_ecs.types.instance_requirements_request.serialize_aws_json_1_1(
                value["instance_requirements"]
            )
        )
    if "fips_enabled" in value:
        out["fipsEnabled"] = value["fips_enabled"]
    if "capacity_reservations" in value:
        import capo_ecs.types.capacity_reservation_request

        out["capacityReservations"] = (
            capo_ecs.types.capacity_reservation_request.serialize_aws_json_1_1(
                value["capacity_reservations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceLaunchTemplate:
    out: InstanceLaunchTemplate = {}  # type: ignore[typeddict-item]
    if data.get("ec2InstanceProfileArn") is not None:
        out["ec2_instance_profile_arn"] = data["ec2InstanceProfileArn"]
    else:
        raise DeserializationError(
            "InstanceLaunchTemplate.ec2_instance_profile_arn required"
        )
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.managed_instances_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.managed_instances_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InstanceLaunchTemplate.network_configuration required"
        )
    if data.get("storageConfiguration") is not None:
        import capo_ecs.types.managed_instances_storage_configuration

        out["storage_configuration"] = (
            capo_ecs.types.managed_instances_storage_configuration.deserialize_aws_json_1_1(
                data["storageConfiguration"]
            )
        )
    if data.get("localStorageConfiguration") is not None:
        import capo_ecs.types.managed_instances_local_storage_configuration

        out["local_storage_configuration"] = (
            capo_ecs.types.managed_instances_local_storage_configuration.deserialize_aws_json_1_1(
                data["localStorageConfiguration"]
            )
        )
    if data.get("monitoring") is not None:
        import capo_ecs.types.managed_instances_monitoring_options

        out["monitoring"] = (
            capo_ecs.types.managed_instances_monitoring_options.deserialize_aws_json_1_1(
                data["monitoring"]
            )
        )
    if data.get("capacityOptionType") is not None:
        import capo_ecs.types.capacity_option_type

        out["capacity_option_type"] = (
            capo_ecs.types.capacity_option_type.deserialize_aws_json_1_1(
                data["capacityOptionType"]
            )
        )
    if data.get("instanceMetadataTagsPropagation") is not None:
        out["instance_metadata_tags_propagation"] = data[
            "instanceMetadataTagsPropagation"
        ]
    if data.get("instanceRequirements") is not None:
        import capo_ecs.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_ecs.types.instance_requirements_request.deserialize_aws_json_1_1(
                data["instanceRequirements"]
            )
        )
    if data.get("fipsEnabled") is not None:
        out["fips_enabled"] = data["fipsEnabled"]
    if data.get("capacityReservations") is not None:
        import capo_ecs.types.capacity_reservation_request

        out["capacity_reservations"] = (
            capo_ecs.types.capacity_reservation_request.deserialize_aws_json_1_1(
                data["capacityReservations"]
            )
        )
    return out
