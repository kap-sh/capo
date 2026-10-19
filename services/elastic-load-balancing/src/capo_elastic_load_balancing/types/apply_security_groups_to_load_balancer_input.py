"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ApplySecurityGroupsToLoadBalancerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.security_groups


class ApplySecurityGroupsToLoadBalancerInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    security_groups: "capo_elastic_load_balancing.types.security_groups.SecurityGroups"
    """<p>The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplySecurityGroupsToLoadBalancerInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.security_groups

    capo_elastic_load_balancing.types.security_groups.serialize_query(
        value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
    )


def deserialize_query(el: Element) -> ApplySecurityGroupsToLoadBalancerInput:
    out: ApplySecurityGroupsToLoadBalancerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elastic_load_balancing.types.security_groups

        out["security_groups"] = (
            capo_elastic_load_balancing.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    else:
        out["security_groups"] = []
    return out
