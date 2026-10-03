"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchTemplateOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.image_id
    import capo_auto_scaling.types.instance_requirements
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len255


class LaunchTemplateOverrides(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The instance type, such as <code>m3.xlarge</code>. You must specify an instance type that is supported in your requested Region and Availability Zones. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>You can specify up to 40 instance types per Auto Scaling group.</p>"""
    weighted_capacity: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>If you provide a list of instance types to use, you can specify the number of capacity units provided by each instance type in terms of virtual CPUs, memory, storage, throughput, or other relative performance characteristic. When a Spot or On-Demand Instance is launched, the capacity units count toward the desired capacity. Amazon EC2 Auto Scaling launches instances until the desired capacity is totally fulfilled, even if this results in an overage. For example, if there are two units remaining to fulfill capacity, and Amazon EC2 Auto Scaling can only launch an instance with a <code>WeightedCapacity</code> of five units, the instance is launched, and the desired capacity is exceeded by three units. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-instance-weighting.html">Configure an Auto Scaling group to use instance weights</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. Value must be in the range of 1–999.</p> <p>If you specify a value for <code>WeightedCapacity</code> for one instance type, you must specify a value for <code>WeightedCapacity</code> for all of them.</p> <important> <p>Every Auto Scaling group has three size parameters (<code>DesiredCapacity</code>, <code>MaxSize</code>, and <code>MinSize</code>). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances. </p> </important>"""
    launch_template_specification: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>Provides a launch template for the specified instance type or set of instance requirements. For example, some instance types might require a launch template with a different AMI. If not provided, Amazon EC2 Auto Scaling uses the launch template that's specified in the <code>LaunchTemplate</code> definition. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.html">Specifying a different launch template for an instance type</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p> <p>You can specify up to 20 launch templates per Auto Scaling group. The launch templates specified in the overrides and in the <code>LaunchTemplate</code> definition count towards this limit.</p>"""
    instance_requirements: NotRequired[
        "capo_auto_scaling.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.</p> <p>You can specify up to four separate sets of instance requirements per Auto Scaling group. This is useful for provisioning instances from different Amazon Machine Images (AMIs) in the same Auto Scaling group. To do this, create the AMIs and create a new launch template for each AMI. Then, create a compatible set of instance requirements for each launch template. </p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    image_id: NotRequired["capo_auto_scaling.types.image_id.ImageId"]
    """<p> The ID of the Amazon Machine Image (AMI) to use for instances launched with this override. When using Instance Refresh with <code>ReplaceRootVolume</code> strategy, this specifies the AMI for root volume replacement operations. </p> <p> For <code>ReplaceRootVolume</code> operations: </p> <ul> <li> <p>All overrides in the <code>MixedInstancesPolicy</code> must specify an ImageId</p> </li> <li> <p>The AMI must contain only a single root volume</p> </li> <li> <p>Root volume replacement doesn't support multi-volume AMIs</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchTemplateOverrides, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "weighted_capacity" in value:
        pairs.append((f"{key_prefix}WeightedCapacity", str(value["weighted_capacity"])))
    if "launch_template_specification" in value:
        import capo_auto_scaling.types.launch_template_specification

        capo_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template_specification"],
            pairs,
            f"{key_prefix}LaunchTemplateSpecification",
        )
    if "instance_requirements" in value:
        import capo_auto_scaling.types.instance_requirements

        capo_auto_scaling.types.instance_requirements.serialize_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))


def deserialize_query(el: Element) -> LaunchTemplateOverrides:
    out: LaunchTemplateOverrides = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_weighted_capacity = el.find("WeightedCapacity")
    if child_weighted_capacity is not None:
        out["weighted_capacity"] = str(child_weighted_capacity.text or "")
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import capo_auto_scaling.types.launch_template_specification

        out["launch_template_specification"] = (
            capo_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template_specification
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import capo_auto_scaling.types.instance_requirements

        out["instance_requirements"] = (
            capo_auto_scaling.types.instance_requirements.deserialize_query(
                child_instance_requirements
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    return out
