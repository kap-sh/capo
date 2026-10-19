"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesForBackendServerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.end_point_port
    import capo_elastic_load_balancing.types.policy_names


class SetLoadBalancerPoliciesForBackendServerInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    instance_port: "capo_elastic_load_balancing.types.end_point_port.EndPointPort"
    """<p>The port number associated with the EC2 instance.</p>"""
    policy_names: "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    """<p>The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerPoliciesForBackendServerInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{key_prefix}InstancePort", str(value["instance_port"])))
    import capo_elastic_load_balancing.types.policy_names

    capo_elastic_load_balancing.types.policy_names.serialize_query(
        value["policy_names"], pairs, f"{key_prefix}PolicyNames"
    )


def deserialize_query(el: Element) -> SetLoadBalancerPoliciesForBackendServerInput:
    out: SetLoadBalancerPoliciesForBackendServerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_instance_port = el.find("InstancePort")
    if child_instance_port is not None:
        out["instance_port"] = int(child_instance_port.text or "")
    else:
        out["instance_port"] = 0
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    else:
        out["policy_names"] = []
    return out
