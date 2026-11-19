"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessSourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cidr
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.dns_protocol
    import capo_route53globalresolver.types.ip_address_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.segment_name


class DeleteAccessSourceOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted access source.</p>"""
    cidr: "capo_route53globalresolver.types.cidr.Cidr"
    """<p>The IP address or CIDR range of the deleted access source.</p>"""
    core_network_endpoint_id: NotRequired[
        "capo_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the core network endpoint associated with this access source.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the access source was originally created.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted access source.</p>"""
    ip_address_type: "capo_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type of the deleted access source. Valid values are IPV4, IPV6, and NONE.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the deleted access source.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view that was associated with the deleted access source.</p>"""
    protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The DNS protocol that was permitted for the deleted access source.</p>"""
    segment: NotRequired["capo_route53globalresolver.types.segment_name.SegmentName"]
    """<p>The name of the segment associated with this access source.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted access source.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the access source was last updated before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessSourceOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["cidr"] = value.get("cidr", "")
    if "core_network_endpoint_id" in value:
        out["coreNetworkEndpointId"] = value["core_network_endpoint_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["id"] = value["id"]
    import capo_route53globalresolver.types.ip_address_type

    out["ipAddressType"] = (
        capo_route53globalresolver.types.ip_address_type.serialize_json(
            value.get("ip_address_type", "NONE")
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    out["dnsViewId"] = value["dns_view_id"]
    import capo_route53globalresolver.types.dns_protocol

    out["protocol"] = capo_route53globalresolver.types.dns_protocol.serialize_json(
        value["protocol"]
    )
    if "segment" in value:
        out["segment"] = value["segment"]
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


def deserialize_json(data: dict) -> DeleteAccessSourceOutput:
    out: DeleteAccessSourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
    if data.get("coreNetworkEndpointId") is not None:
        out["core_network_endpoint_id"] = data["coreNetworkEndpointId"]
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("ipAddressType") is not None:
        import capo_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    else:
        out["ip_address_type"] = "NONE"
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("dnsViewId") is not None:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        out["dns_view_id"] = ""
    if data.get("protocol") is not None:
        import capo_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            capo_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_route53globalresolver.types.dns_protocol.DnsProtocol", ""
        )
    if data.get("segment") is not None:
        out["segment"] = data["segment"]
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
