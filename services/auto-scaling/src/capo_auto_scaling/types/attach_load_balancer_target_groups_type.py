"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachLoadBalancerTargetGroupsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.target_group_ar_ns
    import capo_auto_scaling.types.xml_string_max_len255


class AttachLoadBalancerTargetGroupsType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    target_group_ar_ns: NotRequired[
        "capo_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
    ]
    """<p>The Amazon Resource Names (ARNs) of the target groups. You can specify up to 10 target groups. To get the ARN of a target group, use the Elastic Load Balancing <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> API operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancerTargetGroupsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "target_group_ar_ns" in value:
        import capo_auto_scaling.types.target_group_ar_ns

        capo_auto_scaling.types.target_group_ar_ns.serialize_query(
            value["target_group_ar_ns"], pairs, f"{key_prefix}TargetGroupARNs"
        )


def deserialize_query(el: Element) -> AttachLoadBalancerTargetGroupsType:
    out: AttachLoadBalancerTargetGroupsType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_target_group_ar_ns = el.find("TargetGroupARNs")
    if child_target_group_ar_ns is not None:
        import capo_auto_scaling.types.target_group_ar_ns

        out["target_group_ar_ns"] = (
            capo_auto_scaling.types.target_group_ar_ns.deserialize_query(
                child_target_group_ar_ns
            )
        )
    return out
