"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadBalancerTargetGroupState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len511


class LoadBalancerTargetGroupState(TypedDict, closed=True):
    load_balancer_target_group_arn: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    state: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The state of the target group.</p> <ul> <li> <p> <code>Adding</code> - The Auto Scaling instances are being registered with the target group.</p> </li> <li> <p> <code>Added</code> - All Auto Scaling instances are registered with the target group.</p> </li> <li> <p> <code>InService</code> - At least one Auto Scaling instance passed an <code>ELB</code> health check. Note that the target group enters this state immediately if you attach it in the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html">CreateAutoScalingGroup</a> API call.</p> </li> <li> <p> <code>Removing</code> - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.</p> </li> <li> <p> <code>Removed</code> - All Auto Scaling instances are deregistered from the target group.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerTargetGroupState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_target_group_arn" in value:
        pairs.append(
            (
                f"{key_prefix}LoadBalancerTargetGroupARN",
                str(value["load_balancer_target_group_arn"]),
            )
        )
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))


def deserialize_query(el: Element) -> LoadBalancerTargetGroupState:
    out: LoadBalancerTargetGroupState = {}  # type: ignore[typeddict-item]
    child_load_balancer_target_group_arn = el.find("LoadBalancerTargetGroupARN")
    if child_load_balancer_target_group_arn is not None:
        out["load_balancer_target_group_arn"] = str(
            child_load_balancer_target_group_arn.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    return out
