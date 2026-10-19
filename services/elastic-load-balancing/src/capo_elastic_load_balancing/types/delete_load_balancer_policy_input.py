"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DeleteLoadBalancerPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.policy_name


class DeleteLoadBalancerPolicyInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoadBalancerPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> DeleteLoadBalancerPolicyInput:
    out: DeleteLoadBalancerPolicyInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        out["policy_name"] = ""
    return out
