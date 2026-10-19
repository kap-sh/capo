"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#RegisterEndPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.instances


class RegisterEndPointsInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    instances: "capo_elastic_load_balancing.types.instances.Instances"
    """<p>The IDs of the instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterEndPointsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.instances

    capo_elastic_load_balancing.types.instances.serialize_query(
        value["instances"], pairs, f"{key_prefix}Instances"
    )


def deserialize_query(el: Element) -> RegisterEndPointsInput:
    out: RegisterEndPointsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_instances = el.find("Instances")
    if child_instances is not None:
        import capo_elastic_load_balancing.types.instances

        out["instances"] = (
            capo_elastic_load_balancing.types.instances.deserialize_query(
                child_instances
            )
        )
    else:
        out["instances"] = []
    return out
