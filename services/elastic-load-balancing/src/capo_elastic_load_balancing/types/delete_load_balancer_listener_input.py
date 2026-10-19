"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DeleteLoadBalancerListenerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.ports


class DeleteLoadBalancerListenerInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    load_balancer_ports: "capo_elastic_load_balancing.types.ports.Ports"
    """<p>The client port numbers of the listeners.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLoadBalancerListenerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.ports

    capo_elastic_load_balancing.types.ports.serialize_query(
        value["load_balancer_ports"], pairs, f"{key_prefix}LoadBalancerPorts"
    )


def deserialize_query(el: Element) -> DeleteLoadBalancerListenerInput:
    out: DeleteLoadBalancerListenerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_load_balancer_ports = el.find("LoadBalancerPorts")
    if child_load_balancer_ports is not None:
        import capo_elastic_load_balancing.types.ports

        out["load_balancer_ports"] = (
            capo_elastic_load_balancing.types.ports.deserialize_query(
                child_load_balancer_ports
            )
        )
    else:
        out["load_balancer_ports"] = []
    return out
