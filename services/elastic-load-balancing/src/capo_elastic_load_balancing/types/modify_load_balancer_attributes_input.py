"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ModifyLoadBalancerAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.load_balancer_attributes


class ModifyLoadBalancerAttributesInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    load_balancer_attributes: "capo_elastic_load_balancing.types.load_balancer_attributes.LoadBalancerAttributes"
    """<p>The attributes for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyLoadBalancerAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.load_balancer_attributes

    capo_elastic_load_balancing.types.load_balancer_attributes.serialize_query(
        value["load_balancer_attributes"], pairs, f"{key_prefix}LoadBalancerAttributes"
    )


def deserialize_query(el: Element) -> ModifyLoadBalancerAttributesInput:
    out: ModifyLoadBalancerAttributesInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_load_balancer_attributes = el.find("LoadBalancerAttributes")
    if child_load_balancer_attributes is not None:
        import capo_elastic_load_balancing.types.load_balancer_attributes

        out["load_balancer_attributes"] = (
            capo_elastic_load_balancing.types.load_balancer_attributes.deserialize_query(
                child_load_balancer_attributes
            )
        )
    else:
        raise DeserializationError(
            "ModifyLoadBalancerAttributesInput.load_balancer_attributes required"
        )
    return out
