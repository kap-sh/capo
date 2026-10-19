"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerListenerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.listeners


class CreateLoadBalancerListenerInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    listeners: "capo_elastic_load_balancing.types.listeners.Listeners"
    """<p>The listeners.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerListenerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.listeners

    capo_elastic_load_balancing.types.listeners.serialize_query(
        value["listeners"], pairs, f"{key_prefix}Listeners"
    )


def deserialize_query(el: Element) -> CreateLoadBalancerListenerInput:
    out: CreateLoadBalancerListenerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import capo_elastic_load_balancing.types.listeners

        out["listeners"] = (
            capo_elastic_load_balancing.types.listeners.deserialize_query(
                child_listeners
            )
        )
    else:
        out["listeners"] = []
    return out
