"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateGlobalResolverInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.tags


class CreateGlobalResolverInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique string that identifies the request and ensures idempotency. If you make multiple requests with the same client token, only one Route 53 Global Resolver is created.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the Route 53 Global Resolver instance. Maximum length of 1024 characters.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL_STACK for both IPv4 and IPv6 support.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>A descriptive name for the Route 53 Global Resolver instance. Maximum length of 64 characters.</p>"""
    observability_region: NotRequired["capo_route53globalresolver.types.region.Region"]
    """<p>The Amazon Web Services Region where query resolution logs and metrics will be aggregated and delivered. If not specified, logging is not enabled.</p>"""
    regions: "capo_route53globalresolver.types.regions.Regions"
    """<p>List of Amazon Web Services Regions where the Route 53 Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>"""
    tags: NotRequired["capo_route53globalresolver.types.tags.Tags"]
    """<p>Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlobalResolverInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    out["name"] = value["name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    import capo_route53globalresolver.types.regions

    out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
        value["regions"]
    )
    if "tags" in value:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateGlobalResolverInput:
    out: CreateGlobalResolverInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ipAddressType") is not None:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("observabilityRegion") is not None:
        out["observability_region"] = data["observabilityRegion"]
    if data.get("regions") is not None:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    if data.get("tags") is not None:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
