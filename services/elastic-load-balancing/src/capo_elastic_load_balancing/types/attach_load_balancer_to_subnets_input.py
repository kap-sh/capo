"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AttachLoadBalancerToSubnetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.subnets


class AttachLoadBalancerToSubnetsInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    subnets: "capo_elastic_load_balancing.types.subnets.Subnets"
    """<p>The IDs of the subnets to add. You can add only one subnet per Availability Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancerToSubnetsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.subnets

    capo_elastic_load_balancing.types.subnets.serialize_query(
        value["subnets"], pairs, f"{key_prefix}Subnets"
    )


def deserialize_query(el: Element) -> AttachLoadBalancerToSubnetsInput:
    out: AttachLoadBalancerToSubnetsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_elastic_load_balancing.types.subnets

        out["subnets"] = capo_elastic_load_balancing.types.subnets.deserialize_query(
            child_subnets
        )
    else:
        out["subnets"] = []
    return out
