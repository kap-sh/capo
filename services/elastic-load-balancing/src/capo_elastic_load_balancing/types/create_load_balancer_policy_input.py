"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.policy_attributes
    import capo_elastic_load_balancing.types.policy_name
    import capo_elastic_load_balancing.types.policy_type_name


class CreateLoadBalancerPolicyInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName"
    """<p>The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.</p>"""
    policy_type_name: (
        "capo_elastic_load_balancing.types.policy_type_name.PolicyTypeName"
    )
    """<p>The name of the base policy type. To get the list of policy types, use <a>DescribeLoadBalancerPolicyTypes</a>.</p>"""
    policy_attributes: NotRequired[
        "capo_elastic_load_balancing.types.policy_attributes.PolicyAttributes"
    ]
    """<p>The policy attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    pairs.append((f"{key_prefix}PolicyTypeName", str(value["policy_type_name"])))
    if "policy_attributes" in value:
        import capo_elastic_load_balancing.types.policy_attributes

        capo_elastic_load_balancing.types.policy_attributes.serialize_query(
            value["policy_attributes"], pairs, f"{key_prefix}PolicyAttributes"
        )


def deserialize_query(el: Element) -> CreateLoadBalancerPolicyInput:
    out: CreateLoadBalancerPolicyInput = {}  # type: ignore[typeddict-item]
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
    child_policy_type_name = el.find("PolicyTypeName")
    if child_policy_type_name is not None:
        out["policy_type_name"] = str(child_policy_type_name.text or "")
    else:
        out["policy_type_name"] = ""
    child_policy_attributes = el.find("PolicyAttributes")
    if child_policy_attributes is not None:
        import capo_elastic_load_balancing.types.policy_attributes

        out["policy_attributes"] = (
            capo_elastic_load_balancing.types.policy_attributes.deserialize_query(
                child_policy_attributes
            )
        )
    return out
