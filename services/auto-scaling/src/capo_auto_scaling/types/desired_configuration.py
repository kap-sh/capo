"""Generated from Smithy shape ``com.amazonaws.autoscaling#DesiredConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.mixed_instances_policy


class DesiredConfiguration(TypedDict, closed=True):
    launch_template: NotRequired[
        "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>Describes the launch template and the version of the launch template that Amazon EC2 Auto Scaling uses to launch Amazon EC2 instances. For more information about launch templates, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html">Launch templates</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    mixed_instances_policy: NotRequired[
        "capo_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
    ]
    """<p>Use this structure to launch multiple instance types and configure how capacity is distributed across On-Demand, Spot, and supported Capacity Reservation types within a single Auto Scaling group.</p> <p>A mixed instances policy contains information that Amazon EC2 Auto Scaling can use to launch instances, prioritize capacity types, and help optimize your costs. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html">Auto Scaling groups with multiple instance types and purchase options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DesiredConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template" in value:
        import capo_auto_scaling.types.launch_template_specification

        capo_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template"], pairs, f"{key_prefix}LaunchTemplate"
        )
    if "mixed_instances_policy" in value:
        import capo_auto_scaling.types.mixed_instances_policy

        capo_auto_scaling.types.mixed_instances_policy.serialize_query(
            value["mixed_instances_policy"], pairs, f"{key_prefix}MixedInstancesPolicy"
        )


def deserialize_query(el: Element) -> DesiredConfiguration:
    out: DesiredConfiguration = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_auto_scaling.types.launch_template_specification

        out["launch_template"] = (
            capo_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template
            )
        )
    child_mixed_instances_policy = el.find("MixedInstancesPolicy")
    if child_mixed_instances_policy is not None:
        import capo_auto_scaling.types.mixed_instances_policy

        out["mixed_instances_policy"] = (
            capo_auto_scaling.types.mixed_instances_policy.deserialize_query(
                child_mixed_instances_policy
            )
        )
    return out
