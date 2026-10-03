"""Generated from Smithy shape ``com.amazonaws.autoscaling#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_protected
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.lifecycle_state
    import capo_auto_scaling.types.xml_string_max_len19
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len255


class Instance(TypedDict, closed=True):
    instance_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
    ]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The instance type of the EC2 instance.</p>"""
    availability_zone: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The Availability Zone in which the instance is running.</p>"""
    availability_zone_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The Availability Zone ID where the instance was launched. </p>"""
    lifecycle_state: NotRequired[
        "capo_auto_scaling.types.lifecycle_state.LifecycleState"
    ]
    """<p>A description of the current lifecycle state. The <code>Quarantined</code> state is not used. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html">Amazon EC2 Auto Scaling instance lifecycle</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""
    health_status: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>The last reported health status of the instance. <code>Healthy</code> means that the instance is healthy and should remain in service. <code>Unhealthy</code> means that the instance is unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.</p>"""
    launch_configuration_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The launch configuration associated with the instance.</p>"""
    launch_template: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template for the instance.</p>"""
    image_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The ID of the Amazon Machine Image (AMI) used for the instance's current root volume. This value reflects the most recent AMI applied to the instance, including updates made through root volume replacement operations. </p> <p> This field appears for: </p> <ul> <li> <p>Instances with root volume replacements through Instance Refresh</p> </li> <li> <p>Instances launched with AMI overrides </p> </li> </ul> <p>This field won't appear for:</p> <ul> <li> <p>Existing instances launched from Launch Templates without overrides</p> </li> <li> <p>Existing instances that didn’t have their root volume replaced through Instance Refresh</p> </li> </ul>"""
    protected_from_scale_in: NotRequired[
        "capo_auto_scaling.types.instance_protected.InstanceProtected"
    ]
    """<p>Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.</p>"""
    weighted_capacity: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>The number of capacity units contributed by the instance based on its instance type.</p> <p>Valid Range: Minimum value of 1. Maximum value of 999.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Instance, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "lifecycle_state" in value:
        import capo_auto_scaling.types.lifecycle_state

        capo_auto_scaling.types.lifecycle_state.serialize_query(
            value["lifecycle_state"], pairs, f"{key_prefix}LifecycleState"
        )
    if "health_status" in value:
        pairs.append((f"{key_prefix}HealthStatus", str(value["health_status"])))
    if "launch_configuration_name" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchConfigurationName",
                str(value["launch_configuration_name"]),
            )
        )
    if "launch_template" in value:
        import capo_auto_scaling.types.launch_template_specification

        capo_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template"], pairs, f"{key_prefix}LaunchTemplate"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "protected_from_scale_in" in value:
        pairs.append(
            (
                f"{key_prefix}ProtectedFromScaleIn",
                "true" if value["protected_from_scale_in"] else "false",
            )
        )
    if "weighted_capacity" in value:
        pairs.append((f"{key_prefix}WeightedCapacity", str(value["weighted_capacity"])))


def deserialize_query(el: Element) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_lifecycle_state = el.find("LifecycleState")
    if child_lifecycle_state is not None:
        import capo_auto_scaling.types.lifecycle_state

        out["lifecycle_state"] = (
            capo_auto_scaling.types.lifecycle_state.deserialize_query(
                child_lifecycle_state
            )
        )
    child_health_status = el.find("HealthStatus")
    if child_health_status is not None:
        out["health_status"] = str(child_health_status.text or "")
    child_launch_configuration_name = el.find("LaunchConfigurationName")
    if child_launch_configuration_name is not None:
        out["launch_configuration_name"] = str(
            child_launch_configuration_name.text or ""
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_auto_scaling.types.launch_template_specification

        out["launch_template"] = (
            capo_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_protected_from_scale_in = el.find("ProtectedFromScaleIn")
    if child_protected_from_scale_in is not None:
        out["protected_from_scale_in"] = (
            child_protected_from_scale_in.text or ""
        ).lower() == "true"
    child_weighted_capacity = el.find("WeightedCapacity")
    if child_weighted_capacity is not None:
        out["weighted_capacity"] = str(child_weighted_capacity.text or "")
    return out
