"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LoadBalancerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.availability_zones
    import capo_elastic_load_balancing.types.backend_server_descriptions
    import capo_elastic_load_balancing.types.created_time
    import capo_elastic_load_balancing.types.dns_name
    import capo_elastic_load_balancing.types.health_check
    import capo_elastic_load_balancing.types.instances
    import capo_elastic_load_balancing.types.listener_descriptions
    import capo_elastic_load_balancing.types.load_balancer_scheme
    import capo_elastic_load_balancing.types.policies
    import capo_elastic_load_balancing.types.security_groups
    import capo_elastic_load_balancing.types.source_security_group
    import capo_elastic_load_balancing.types.subnets
    import capo_elastic_load_balancing.types.vpc_id


class LoadBalancerDescription(TypedDict, closed=True):
    load_balancer_name: NotRequired[
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    ]
    """<p>The name of the load balancer.</p>"""
    dns_name: NotRequired["capo_elastic_load_balancing.types.dns_name.DNSName"]
    """<p>The DNS name of the load balancer.</p>"""
    canonical_hosted_zone_name: NotRequired[
        "capo_elastic_load_balancing.types.dns_name.DNSName"
    ]
    """<p>The DNS name of the load balancer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html">Configure a Custom Domain Name</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    canonical_hosted_zone_name_id: NotRequired[
        "capo_elastic_load_balancing.types.dns_name.DNSName"
    ]
    """<p>The ID of the Amazon Route 53 hosted zone for the load balancer.</p>"""
    listener_descriptions: NotRequired[
        "capo_elastic_load_balancing.types.listener_descriptions.ListenerDescriptions"
    ]
    """<p>The listeners for the load balancer.</p>"""
    policies: NotRequired["capo_elastic_load_balancing.types.policies.Policies"]
    """<p>The policies defined for the load balancer.</p>"""
    backend_server_descriptions: NotRequired[
        "capo_elastic_load_balancing.types.backend_server_descriptions.BackendServerDescriptions"
    ]
    """<p>Information about your EC2 instances.</p>"""
    availability_zones: NotRequired[
        "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones"
    ]
    """<p>The Availability Zones for the load balancer.</p>"""
    subnets: NotRequired["capo_elastic_load_balancing.types.subnets.Subnets"]
    """<p>The IDs of the subnets for the load balancer.</p>"""
    vpc_id: NotRequired["capo_elastic_load_balancing.types.vpc_id.VPCId"]
    """<p>The ID of the VPC for the load balancer.</p>"""
    instances: NotRequired["capo_elastic_load_balancing.types.instances.Instances"]
    """<p>The IDs of the instances for the load balancer.</p>"""
    health_check: NotRequired[
        "capo_elastic_load_balancing.types.health_check.HealthCheck"
    ]
    """<p>Information about the health checks conducted on the load balancer.</p>"""
    source_security_group: NotRequired[
        "capo_elastic_load_balancing.types.source_security_group.SourceSecurityGroup"
    ]
    """<p>The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.</p>"""
    security_groups: NotRequired[
        "capo_elastic_load_balancing.types.security_groups.SecurityGroups"
    ]
    """<p>The security groups for the load balancer. Valid only for load balancers in a VPC.</p>"""
    created_time: NotRequired[
        "capo_elastic_load_balancing.types.created_time.CreatedTime"
    ]
    """<p>The date and time the load balancer was created.</p>"""
    scheme: NotRequired[
        "capo_elastic_load_balancing.types.load_balancer_scheme.LoadBalancerScheme"
    ]
    """<p>The type of load balancer. Valid only for load balancers in a VPC.</p> <p>If <code>Scheme</code> is <code>internet-facing</code>, the load balancer has a public DNS name that resolves to a public IP address.</p> <p>If <code>Scheme</code> is <code>internal</code>, the load balancer has a public DNS name that resolves to a private IP address.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_name" in value:
        pairs.append(
            (f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"]))
        )
    if "dns_name" in value:
        pairs.append((f"{key_prefix}DNSName", str(value["dns_name"])))
    if "canonical_hosted_zone_name" in value:
        pairs.append(
            (
                f"{key_prefix}CanonicalHostedZoneName",
                str(value["canonical_hosted_zone_name"]),
            )
        )
    if "canonical_hosted_zone_name_id" in value:
        pairs.append(
            (
                f"{key_prefix}CanonicalHostedZoneNameID",
                str(value["canonical_hosted_zone_name_id"]),
            )
        )
    if "listener_descriptions" in value:
        import capo_elastic_load_balancing.types.listener_descriptions

        capo_elastic_load_balancing.types.listener_descriptions.serialize_query(
            value["listener_descriptions"], pairs, f"{key_prefix}ListenerDescriptions"
        )
    if "policies" in value:
        import capo_elastic_load_balancing.types.policies

        capo_elastic_load_balancing.types.policies.serialize_query(
            value["policies"], pairs, f"{key_prefix}Policies"
        )
    if "backend_server_descriptions" in value:
        import capo_elastic_load_balancing.types.backend_server_descriptions

        capo_elastic_load_balancing.types.backend_server_descriptions.serialize_query(
            value["backend_server_descriptions"],
            pairs,
            f"{key_prefix}BackendServerDescriptions",
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
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VPCId", str(value["vpc_id"])))
    if "instances" in value:
        import capo_elastic_load_balancing.types.instances

        capo_elastic_load_balancing.types.instances.serialize_query(
            value["instances"], pairs, f"{key_prefix}Instances"
        )
    if "health_check" in value:
        import capo_elastic_load_balancing.types.health_check

        capo_elastic_load_balancing.types.health_check.serialize_query(
            value["health_check"], pairs, f"{key_prefix}HealthCheck"
        )
    if "source_security_group" in value:
        import capo_elastic_load_balancing.types.source_security_group

        capo_elastic_load_balancing.types.source_security_group.serialize_query(
            value["source_security_group"], pairs, f"{key_prefix}SourceSecurityGroup"
        )
    if "security_groups" in value:
        import capo_elastic_load_balancing.types.security_groups

        capo_elastic_load_balancing.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "created_time" in value:
        import capo_elastic_load_balancing.types.created_time

        capo_elastic_load_balancing.types.created_time.serialize_query(
            value["created_time"], pairs, f"{key_prefix}CreatedTime"
        )
    if "scheme" in value:
        pairs.append((f"{key_prefix}Scheme", str(value["scheme"])))


def deserialize_query(el: Element) -> LoadBalancerDescription:
    out: LoadBalancerDescription = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_dns_name = el.find("DNSName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_canonical_hosted_zone_name = el.find("CanonicalHostedZoneName")
    if child_canonical_hosted_zone_name is not None:
        out["canonical_hosted_zone_name"] = str(
            child_canonical_hosted_zone_name.text or ""
        )
    child_canonical_hosted_zone_name_id = el.find("CanonicalHostedZoneNameID")
    if child_canonical_hosted_zone_name_id is not None:
        out["canonical_hosted_zone_name_id"] = str(
            child_canonical_hosted_zone_name_id.text or ""
        )
    child_listener_descriptions = el.find("ListenerDescriptions")
    if child_listener_descriptions is not None:
        import capo_elastic_load_balancing.types.listener_descriptions

        out["listener_descriptions"] = (
            capo_elastic_load_balancing.types.listener_descriptions.deserialize_query(
                child_listener_descriptions
            )
        )
    child_policies = el.find("Policies")
    if child_policies is not None:
        import capo_elastic_load_balancing.types.policies

        out["policies"] = capo_elastic_load_balancing.types.policies.deserialize_query(
            child_policies
        )
    child_backend_server_descriptions = el.find("BackendServerDescriptions")
    if child_backend_server_descriptions is not None:
        import capo_elastic_load_balancing.types.backend_server_descriptions

        out["backend_server_descriptions"] = (
            capo_elastic_load_balancing.types.backend_server_descriptions.deserialize_query(
                child_backend_server_descriptions
            )
        )
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
    child_vpc_id = el.find("VPCId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_instances = el.find("Instances")
    if child_instances is not None:
        import capo_elastic_load_balancing.types.instances

        out["instances"] = (
            capo_elastic_load_balancing.types.instances.deserialize_query(
                child_instances
            )
        )
    child_health_check = el.find("HealthCheck")
    if child_health_check is not None:
        import capo_elastic_load_balancing.types.health_check

        out["health_check"] = (
            capo_elastic_load_balancing.types.health_check.deserialize_query(
                child_health_check
            )
        )
    child_source_security_group = el.find("SourceSecurityGroup")
    if child_source_security_group is not None:
        import capo_elastic_load_balancing.types.source_security_group

        out["source_security_group"] = (
            capo_elastic_load_balancing.types.source_security_group.deserialize_query(
                child_source_security_group
            )
        )
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elastic_load_balancing.types.security_groups

        out["security_groups"] = (
            capo_elastic_load_balancing.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_elastic_load_balancing.types.created_time

        out["created_time"] = (
            capo_elastic_load_balancing.types.created_time.deserialize_query(
                child_created_time
            )
        )
    child_scheme = el.find("Scheme")
    if child_scheme is not None:
        out["scheme"] = str(child_scheme.text or "")
    return out
