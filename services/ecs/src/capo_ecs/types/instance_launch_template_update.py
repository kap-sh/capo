"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceLaunchTemplateUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.capacity_reservation_request
    import capo_ecs.types.instance_requirements_request
    import capo_ecs.types.managed_instances_local_storage_configuration
    import capo_ecs.types.managed_instances_monitoring_options
    import capo_ecs.types.managed_instances_network_configuration
    import capo_ecs.types.managed_instances_storage_configuration
    import capo_ecs.types.string


class InstanceLaunchTemplateUpdate(TypedDict, closed=True):
    ec2_instance_profile_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The updated Amazon Resource Name (ARN) of the instance profile. The new instance profile must have the necessary permissions for your tasks.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html">Amazon ECS instance profile for Managed Instances</a> in the <i>Amazon ECS Developer Guide</i>. </p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.managed_instances_network_configuration.ManagedInstancesNetworkConfiguration"
    ]
    """<p>The updated network configuration for Amazon ECS Managed Instances. Changes to subnets and security groups affect new instances launched after the update.</p>"""
    storage_configuration: NotRequired[
        "capo_ecs.types.managed_instances_storage_configuration.ManagedInstancesStorageConfiguration"
    ]
    """<p>The updated storage configuration for Amazon ECS Managed Instances. Changes to storage settings apply to new instances launched after the update.</p>"""
    instance_metadata_tags_propagation: NotRequired[
        "capo_ecs.types.boxed_boolean.BoxedBoolean"
    ]
    r"""<p>Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.</p> <p>Disable this setting if your tags contain characters that are not compatible with IMDS, such as <code>/</code>. IMDS requires tag keys to match the pattern <code>[0-9a-zA-Z\-_+=,.@:]{1,255}</code>.</p> <p>The default value is <code>true</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS">Work with instance tags in instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    local_storage_configuration: NotRequired[
        "capo_ecs.types.managed_instances_local_storage_configuration.ManagedInstancesLocalStorageConfiguration"
    ]
    """<p>The updated local storage configuration for Amazon ECS Managed Instances. Changes to local storage settings apply to new instances launched after the update.</p>"""
    monitoring: NotRequired[
        "capo_ecs.types.managed_instances_monitoring_options.ManagedInstancesMonitoringOptions"
    ]
    """<p>CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html">Detailed monitoring for Amazon ECS Managed Instances</a> in the Amazon ECS Developer Guide.</p>"""
    instance_requirements: NotRequired[
        "capo_ecs.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The updated instance requirements for attribute-based instance type selection. Changes to instance requirements affect which instance types Amazon ECS selects for new instances.</p>"""
    capacity_reservations: NotRequired[
        "capo_ecs.types.capacity_reservation_request.CapacityReservationRequest"
    ]
    """<p>The updated capacity reservations specifications for Amazon ECS Managed Instances. Changes to capacity reservations settings apply to new instances launched after the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceLaunchTemplateUpdate) -> dict:
    out: dict = {}
    if "ec2_instance_profile_arn" in value:
        out["ec2InstanceProfileArn"] = value["ec2_instance_profile_arn"]
    if "network_configuration" in value:
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
    if "instance_metadata_tags_propagation" in value:
        out["instanceMetadataTagsPropagation"] = value[
            "instance_metadata_tags_propagation"
        ]
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
    if "instance_requirements" in value:
        import capo_ecs.types.instance_requirements_request

        out["instanceRequirements"] = (
            capo_ecs.types.instance_requirements_request.serialize_aws_json_1_1(
                value["instance_requirements"]
            )
        )
    if "capacity_reservations" in value:
        import capo_ecs.types.capacity_reservation_request

        out["capacityReservations"] = (
            capo_ecs.types.capacity_reservation_request.serialize_aws_json_1_1(
                value["capacity_reservations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceLaunchTemplateUpdate:
    out: InstanceLaunchTemplateUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ec2InstanceProfileArn") is not None:
        out["ec2_instance_profile_arn"] = data["ec2InstanceProfileArn"]
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.managed_instances_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.managed_instances_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("storageConfiguration") is not None:
        import capo_ecs.types.managed_instances_storage_configuration

        out["storage_configuration"] = (
            capo_ecs.types.managed_instances_storage_configuration.deserialize_aws_json_1_1(
                data["storageConfiguration"]
            )
        )
    if data.get("instanceMetadataTagsPropagation") is not None:
        out["instance_metadata_tags_propagation"] = data[
            "instanceMetadataTagsPropagation"
        ]
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
    if data.get("instanceRequirements") is not None:
        import capo_ecs.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_ecs.types.instance_requirements_request.deserialize_aws_json_1_1(
                data["instanceRequirements"]
            )
        )
    if data.get("capacityReservations") is not None:
        import capo_ecs.types.capacity_reservation_request

        out["capacity_reservations"] = (
            capo_ecs.types.capacity_reservation_request.deserialize_aws_json_1_1(
                data["capacityReservations"]
            )
        )
    return out
