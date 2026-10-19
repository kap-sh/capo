"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesOfListenerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.access_point_port
    import capo_elastic_load_balancing.types.policy_names


class SetLoadBalancerPoliciesOfListenerInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    load_balancer_port: (
        "capo_elastic_load_balancing.types.access_point_port.AccessPointPort"
    )
    """<p>The external port of the load balancer.</p>"""
    policy_names: "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    """<p>The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerPoliciesOfListenerInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{key_prefix}LoadBalancerPort", str(value["load_balancer_port"])))
    import capo_elastic_load_balancing.types.policy_names

    capo_elastic_load_balancing.types.policy_names.serialize_query(
        value["policy_names"], pairs, f"{key_prefix}PolicyNames"
    )


def deserialize_query(el: Element) -> SetLoadBalancerPoliciesOfListenerInput:
    out: SetLoadBalancerPoliciesOfListenerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesOfListenerInput.load_balancer_name required"
        )
    child_load_balancer_port = el.find("LoadBalancerPort")
    if child_load_balancer_port is not None:
        out["load_balancer_port"] = int(child_load_balancer_port.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesOfListenerInput.load_balancer_port required"
        )
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesOfListenerInput.policy_names required"
        )
    return out
