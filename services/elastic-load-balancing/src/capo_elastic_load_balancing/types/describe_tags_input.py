"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.load_balancer_names_max20


class DescribeTagsInput(TypedDict, closed=True):
    load_balancer_names: "capo_elastic_load_balancing.types.load_balancer_names_max20.LoadBalancerNamesMax20"
    """<p>The names of the load balancers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_elastic_load_balancing.types.load_balancer_names_max20

    capo_elastic_load_balancing.types.load_balancer_names_max20.serialize_query(
        value["load_balancer_names"], pairs, f"{key_prefix}LoadBalancerNames"
    )


def deserialize_query(el: Element) -> DescribeTagsInput:
    out: DescribeTagsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import capo_elastic_load_balancing.types.load_balancer_names_max20

        out["load_balancer_names"] = (
            capo_elastic_load_balancing.types.load_balancer_names_max20.deserialize_query(
                child_load_balancer_names
            )
        )
    else:
        out["load_balancer_names"] = []
    return out
