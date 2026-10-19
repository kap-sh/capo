"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GlobalResolversItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.i_pv4_addresses
    import capo_route53globalresolver.types.i_pv6_addresses
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.sni


class GlobalResolversItem(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the global resolver.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the global resolver.</p>"""
    client_token: "capo_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dns_name: "capo_route53globalresolver.types.sni.Sni"
    """<p>The DNS name of the global resolver.</p>"""
    observability_region: NotRequired["capo_route53globalresolver.types.region.Region"]
    """<p>The Amazon Web Services Region where observability data is collected for the global resolver.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the global resolver.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the global resolver.</p>"""
    regions: "capo_route53globalresolver.types.regions.Regions"
    """<p>The Amazon Web Services Regions where the global resolver is deployed.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the global resolver was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the global resolver was last updated.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The current status of the global resolver.</p>"""
    ipv4_addresses: "capo_route53globalresolver.types.i_pv4_addresses.IPv4Addresses"
    """<p>The IPv4 addresses assigned to the global resolver.</p>"""
    ipv6_addresses: NotRequired[
        "capo_route53globalresolver.types.i_pv6_addresses.IPv6Addresses"
    ]
    """<p>The IPv6 addresses assigned to the global resolver. This field is only populated when ipAddressType is DUAL_STACK.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type configured for the global resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalResolversItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clientToken"] = value["client_token"]
    out["dnsName"] = value["dns_name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_route53globalresolver.types.regions

    out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
        value["regions"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.i_pv4_addresses

    out["ipv4Addresses"] = (
        capo_route53globalresolver.types.i_pv4_addresses.serialize_json(
            value["ipv4_addresses"]
        )
    )
    if "ipv6_addresses" in value:
        import capo_route53globalresolver.types.i_pv6_addresses

        out["ipv6Addresses"] = (
            capo_route53globalresolver.types.i_pv6_addresses.serialize_json(
                value["ipv6_addresses"]
            )
        )
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlobalResolversItem:
    out: GlobalResolversItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    else:
        out["dns_name"] = ""
    if data.get("observabilityRegion") is not None:
        out["observability_region"] = data["observabilityRegion"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("regions") is not None:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus", ""
        )
    if data.get("ipv4Addresses") is not None:
        import capo_route53globalresolver.types.i_pv4_addresses

        out["ipv4_addresses"] = (
            capo_route53globalresolver.types.i_pv4_addresses.deserialize_json(
                data["ipv4Addresses"]
            )
        )
    else:
        out["ipv4_addresses"] = []
    if data.get("ipv6Addresses") is not None:
        import capo_route53globalresolver.types.i_pv6_addresses

        out["ipv6_addresses"] = (
            capo_route53globalresolver.types.i_pv6_addresses.deserialize_json(
                data["ipv6Addresses"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    return out
