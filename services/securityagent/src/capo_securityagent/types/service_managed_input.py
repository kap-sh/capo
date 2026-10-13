"""Generated from Smithy shape ``com.amazonaws.securityagent#ServiceManagedInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.certificate_chain
    import capo_securityagent.types.host_address
    import capo_securityagent.types.ip_address_type
    import capo_securityagent.types.max_ipv4_addresses_per_eni
    import capo_securityagent.types.port_ranges
    import capo_securityagent.types.private_connection_security_group_ids
    import capo_securityagent.types.private_connection_subnet_ids
    import capo_securityagent.types.private_connection_vpc_id
    import capo_securityagent.types.resource_config_dns_resolution


class ServiceManagedInput(TypedDict, closed=True):
    host_address: "capo_securityagent.types.host_address.HostAddress"
    """<p>The IP address or DNS name of the target resource.</p>"""
    vpc_id: "capo_securityagent.types.private_connection_vpc_id.PrivateConnectionVpcId"
    """<p>The VPC to create the service-managed resource gateway in.</p>"""
    subnet_ids: "capo_securityagent.types.private_connection_subnet_ids.PrivateConnectionSubnetIds"
    """<p>The subnets that the service-managed resource gateway spans.</p>"""
    security_group_ids: NotRequired[
        "capo_securityagent.types.private_connection_security_group_ids.PrivateConnectionSecurityGroupIds"
    ]
    """<p>The security groups to attach to the service-managed resource gateway.</p>"""
    ip_address_type: NotRequired[
        "capo_securityagent.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type of the service-managed resource gateway.</p>"""
    ipv4_addresses_per_eni: NotRequired[
        "capo_securityagent.types.max_ipv4_addresses_per_eni.MaxIpv4AddressesPerEni"
    ]
    """<p>The number of IPv4 addresses in each elastic network interface for the service-managed resource gateway.</p>"""
    port_ranges: NotRequired["capo_securityagent.types.port_ranges.PortRanges"]
    """<p>The TCP port ranges that a consumer can use to access the resource.</p>"""
    certificate: NotRequired[
        "capo_securityagent.types.certificate_chain.CertificateChain"
    ]
    """<p>The certificate for the private connection.</p>"""
    dns_resolution: NotRequired[
        "capo_securityagent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>The DNS resolution mode for the resource gateway. Defaults to PUBLIC when not set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedInput) -> dict:
    out: dict = {}
    out["hostAddress"] = value["host_address"]
    out["vpcId"] = value["vpc_id"]
    import capo_securityagent.types.private_connection_subnet_ids

    out["subnetIds"] = (
        capo_securityagent.types.private_connection_subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    )
    if "security_group_ids" in value:
        import capo_securityagent.types.private_connection_security_group_ids

        out["securityGroupIds"] = (
            capo_securityagent.types.private_connection_security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        import capo_securityagent.types.ip_address_type

        out["ipAddressType"] = capo_securityagent.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "ipv4_addresses_per_eni" in value:
        out["ipv4AddressesPerEni"] = value["ipv4_addresses_per_eni"]
    if "port_ranges" in value:
        import capo_securityagent.types.port_ranges

        out["portRanges"] = capo_securityagent.types.port_ranges.serialize_json(
            value["port_ranges"]
        )
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    if "dns_resolution" in value:
        import capo_securityagent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            capo_securityagent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedInput:
    out: ServiceManagedInput = {}  # type: ignore[typeddict-item]
    if data.get("hostAddress") is not None:
        out["host_address"] = data["hostAddress"]
    else:
        raise DeserializationError("ServiceManagedInput.host_address required")
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("ServiceManagedInput.vpc_id required")
    if data.get("subnetIds") is not None:
        import capo_securityagent.types.private_connection_subnet_ids

        out["subnet_ids"] = (
            capo_securityagent.types.private_connection_subnet_ids.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("ServiceManagedInput.subnet_ids required")
    if data.get("securityGroupIds") is not None:
        import capo_securityagent.types.private_connection_security_group_ids

        out["security_group_ids"] = (
            capo_securityagent.types.private_connection_security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_securityagent.types.ip_address_type

        out["ip_address_type"] = (
            capo_securityagent.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("ipv4AddressesPerEni") is not None:
        out["ipv4_addresses_per_eni"] = data["ipv4AddressesPerEni"]
    if data.get("portRanges") is not None:
        import capo_securityagent.types.port_ranges

        out["port_ranges"] = capo_securityagent.types.port_ranges.deserialize_json(
            data["portRanges"]
        )
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    if data.get("dnsResolution") is not None:
        import capo_securityagent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            capo_securityagent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    return out


def redact_sensitive(value: ServiceManagedInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "certificate" in value:
        out["certificate"] = "*** Sensitive Data Redacted ***"
    return out
