"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#RemoveAvailabilityZonesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.availability_zones


class RemoveAvailabilityZonesInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    availability_zones: (
        "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones"
    )
    """<p>The Availability Zones.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveAvailabilityZonesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.availability_zones

    capo_elastic_load_balancing.types.availability_zones.serialize_query(
        value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
    )


def deserialize_query(el: Element) -> RemoveAvailabilityZonesInput:
    out: RemoveAvailabilityZonesInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_elastic_load_balancing.types.availability_zones

        out["availability_zones"] = (
            capo_elastic_load_balancing.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    else:
        out["availability_zones"] = []
    return out
