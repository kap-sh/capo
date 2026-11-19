"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteCoreNetworkEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_items
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class DeleteCoreNetworkEndpointOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted core network endpoint.</p>"""
    available_regions: "capo_route53globalresolver.types.regions.Regions"
    """<p>The Amazon Web Services Regions in which the deleted core network endpoint was available.</p>"""
    core_network_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Cloud WAN core network that was connected to the deleted endpoint.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the core network endpoint was originally created.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that was associated with the deleted core network endpoint.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted core network endpoint.</p>"""
    ip_addresses: "capo_route53globalresolver.types.core_network_endpoint_dns_ip_items.CoreNetworkEndpointDnsIpItems"
    """<p>The IP addresses that the deleted core network endpoint used to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the deleted core network endpoint.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted core network endpoint.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the core network endpoint was last updated before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkEndpointOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_route53globalresolver.types.regions

    out["availableRegions"] = capo_route53globalresolver.types.regions.serialize_json(
        value["available_regions"]
    )
    out["coreNetworkArn"] = value["core_network_arn"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["globalResolverId"] = value["global_resolver_id"]
    out["id"] = value["id"]
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_items

    out["ipAddresses"] = (
        capo_route53globalresolver.types.core_network_endpoint_dns_ip_items.serialize_json(
            value["ip_addresses"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkEndpointOutput:
    out: DeleteCoreNetworkEndpointOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("availableRegions") is not None:
        import capo_route53globalresolver.types.regions

        out["available_regions"] = (
            capo_route53globalresolver.types.regions.deserialize_json(
                data["availableRegions"]
            )
        )
    else:
        out["available_regions"] = []
    if data.get("coreNetworkArn") is not None:
        out["core_network_arn"] = data["coreNetworkArn"]
    else:
        out["core_network_arn"] = ""
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
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        out["global_resolver_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("ipAddresses") is not None:
        import capo_route53globalresolver.types.core_network_endpoint_dns_ip_items

        out["ip_addresses"] = (
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_items.deserialize_json(
                data["ipAddresses"]
            )
        )
    else:
        out["ip_addresses"] = []
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    return out
