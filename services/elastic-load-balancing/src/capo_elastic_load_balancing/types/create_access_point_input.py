"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateAccessPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.availability_zones
    import capo_elastic_load_balancing.types.listeners
    import capo_elastic_load_balancing.types.load_balancer_scheme
    import capo_elastic_load_balancing.types.security_groups
    import capo_elastic_load_balancing.types.subnets
    import capo_elastic_load_balancing.types.tag_list


class CreateAccessPointInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p> <p>This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.</p>"""
    listeners: "capo_elastic_load_balancing.types.listeners.Listeners"
    """<p>The listeners.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html">Listeners for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    availability_zones: NotRequired[
        "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones"
    ]
    """<p>One or more Availability Zones from the same region as the load balancer.</p> <p>You must specify at least one Availability Zone.</p> <p>You can add more Availability Zones after you create the load balancer using <a>EnableAvailabilityZonesForLoadBalancer</a>.</p>"""
    subnets: NotRequired["capo_elastic_load_balancing.types.subnets.Subnets"]
    """<p>The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in <code>AvailabilityZones</code>.</p>"""
    security_groups: NotRequired[
        "capo_elastic_load_balancing.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups to assign to the load balancer.</p>"""
    scheme: NotRequired[
        "capo_elastic_load_balancing.types.load_balancer_scheme.LoadBalancerScheme"
    ]
    """<p>The type of a load balancer. Valid only for load balancers in a VPC.</p> <p>By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme">Load Balancer Scheme</a> in the <i>Elastic Load Balancing User Guide</i>.</p> <p>Specify <code>internal</code> to create a load balancer with a DNS name that resolves to private IP addresses.</p>"""
    tags: NotRequired["capo_elastic_load_balancing.types.tag_list.TagList"]
    """<p>A list of tags to assign to the load balancer.</p> <p>For more information about tagging your load balancer, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html">Tag Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAccessPointInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    import capo_elastic_load_balancing.types.listeners

    capo_elastic_load_balancing.types.listeners.serialize_query(
        value["listeners"], pairs, f"{key_prefix}Listeners"
    )
    if "availability_zones" in value:
        import capo_elastic_load_balancing.types.availability_zones

        capo_elastic_load_balancing.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "subnets" in value:
        import capo_elastic_load_balancing.types.subnets

        capo_elastic_load_balancing.types.subnets.serialize_query(
            value["subnets"], pairs, f"{key_prefix}Subnets"
        )
    if "security_groups" in value:
        import capo_elastic_load_balancing.types.security_groups

        capo_elastic_load_balancing.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "scheme" in value:
        pairs.append((f"{key_prefix}Scheme", str(value["scheme"])))
    if "tags" in value:
        import capo_elastic_load_balancing.types.tag_list

        capo_elastic_load_balancing.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateAccessPointInput:
    out: CreateAccessPointInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError("CreateAccessPointInput.load_balancer_name required")
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import capo_elastic_load_balancing.types.listeners

        out["listeners"] = (
            capo_elastic_load_balancing.types.listeners.deserialize_query(
                child_listeners
            )
        )
    else:
        raise DeserializationError("CreateAccessPointInput.listeners required")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_elastic_load_balancing.types.availability_zones

        out["availability_zones"] = (
            capo_elastic_load_balancing.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_elastic_load_balancing.types.subnets

        out["subnets"] = capo_elastic_load_balancing.types.subnets.deserialize_query(
            child_subnets
        )
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elastic_load_balancing.types.security_groups

        out["security_groups"] = (
            capo_elastic_load_balancing.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_scheme = el.find("Scheme")
    if child_scheme is not None:
        out["scheme"] = str(child_scheme.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing.types.tag_list

        out["tags"] = capo_elastic_load_balancing.types.tag_list.deserialize_query(
            child_tags
        )
    return out
