"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadBalancerState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class LoadBalancerState(TypedDict, closed=True):
    load_balancer_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the load balancer.</p>"""
    state: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>One of the following load balancer states:</p> <ul> <li> <p> <code>Adding</code> - The Auto Scaling instances are being registered with the load balancer.</p> </li> <li> <p> <code>Added</code> - All Auto Scaling instances are registered with the load balancer.</p> </li> <li> <p> <code>InService</code> - At least one Auto Scaling instance passed an <code>ELB</code> health check. Note that the load balancer enters this state immediately if you attach it in the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html">CreateAutoScalingGroup</a> API call.</p> </li> <li> <p> <code>Removing</code> - The Auto Scaling instances are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.</p> </li> <li> <p> <code>Removed</code> - All Auto Scaling instances are deregistered from the load balancer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_name" in value:
        pairs.append(
            (f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"]))
        )
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))


def deserialize_query(el: Element) -> LoadBalancerState:
    out: LoadBalancerState = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    return out
