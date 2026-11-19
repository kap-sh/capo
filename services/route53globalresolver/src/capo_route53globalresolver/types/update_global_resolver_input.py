"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateGlobalResolverInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.public_ip_status
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class UpdateGlobalResolverInput(TypedDict, closed=True):
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Global Resolver.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the Global Resolver.</p>"""
    observability_region: NotRequired["capo_route53globalresolver.types.region.Region"]
    """<p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the Global Resolver.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type for the Global Resolver. Valid values are IPV4 or DUAL_STACK for both IPv4 and IPv6 support.</p>"""
    public_ip_status: NotRequired[
        "capo_route53globalresolver.types.public_ip_status.PublicIpStatus"
    ]
    """<p>Specifies the public IP connectivity to configure for the Route 53 Global Resolver. Public IP addresses let DNS clients send queries to the resolver over the internet. Valid values are the following:</p> <ul> <li> <p> <code>ENABLED_RESERVED</code> - Public IP connectivity is enabled, and the global anycast public IP addresses are reserved for the Route 53 Global Resolver.</p> </li> <li> <p> <code>DISABLED_RESERVED</code> - Public IP connectivity is disabled, and the global anycast public IP addresses remain reserved for the Route 53 Global Resolver.</p> </li> <li> <p> <code>DISABLED_RELEASED</code> - Public IP connectivity is disabled, and the global anycast public IP addresses are released.</p> </li> </ul>"""
    regions: NotRequired["capo_route53globalresolver.types.regions.Regions"]
    """<p>The list of Amazon Web Services Regions where the Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalResolverInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    if "description" in value:
        out["description"] = value["description"]
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "public_ip_status" in value:
        import capo_route53globalresolver.types.public_ip_status

        out["publicIpStatus"] = (
            capo_route53globalresolver.types.public_ip_status.serialize_json(
                value["public_ip_status"]
            )
        )
    if "regions" in value:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalResolverInput:
    out: UpdateGlobalResolverInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("observabilityRegion") is not None:
        out["observability_region"] = data["observabilityRegion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ipAddressType") is not None:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("publicIpStatus") is not None:
        import capo_route53globalresolver.types.public_ip_status

        out["public_ip_status"] = (
            capo_route53globalresolver.types.public_ip_status.deserialize_json(
                data["publicIpStatus"]
            )
        )
    if data.get("regions") is not None:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    return out
