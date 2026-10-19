"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetAccessSourceOutput``."""

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


class GetAccessSourceOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access source.</p>"""
    cidr: "capo_route53globalresolver.types.cidr.Cidr"
    """<p>The IP range for the rule's parameters in CIDR notation.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the rule was created.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID for the rule.</p>"""
    ip_address_type: "capo_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>Name for the access source.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID for the DNS view that the rule is associated to.</p>"""
    protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The protocol determines how data is transmitted to a Global Resolver instance.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Information about the status of the rule.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the access source was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessSourceOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["cidr"] = value["cidr"]
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
            value["ip_address_type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    out["dnsViewId"] = value["dns_view_id"]
    import capo_route53globalresolver.types.dns_protocol

    out["protocol"] = capo_route53globalresolver.types.dns_protocol.serialize_json(
        value["protocol"]
    )
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


def deserialize_json(data: dict) -> GetAccessSourceOutput:
    out: GetAccessSourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
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
        import typing

        out["ip_address_type"] = typing.cast(
            "capo_route53globalresolver.types.ip_address_type.IpAddressType", ""
        )
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
