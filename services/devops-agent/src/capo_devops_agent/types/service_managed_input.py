"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceManagedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.certificate_string
    import capo_devops_agent.types.ip_address_or_dns_name
    import capo_devops_agent.types.ip_address_type
    import capo_devops_agent.types.list_of_security_group_ids
    import capo_devops_agent.types.list_of_subnet_ids
    import capo_devops_agent.types.max_ipv4_addresses_per_eni
    import capo_devops_agent.types.port_ranges
    import capo_devops_agent.types.resource_config_dns_resolution
    import capo_devops_agent.types.vpc_id


class ServiceManagedInput(TypedDict, closed=True):
    host_address: "capo_devops_agent.types.ip_address_or_dns_name.IpAddressOrDnsName"
    """<p>IP address or DNS name of the target resource.</p>"""
    vpc_id: "capo_devops_agent.types.vpc_id.VpcId"
    """<p>VPC to create the service-managed Resource Gateway in.</p>"""
    subnet_ids: "capo_devops_agent.types.list_of_subnet_ids.ListOfSubnetIds"
    """<p>Subnets that the service-managed Resource Gateway will span.</p>"""
    security_group_ids: NotRequired[
        "capo_devops_agent.types.list_of_security_group_ids.ListOfSecurityGroupIds"
    ]
    """<p>Security groups to attach to the service-managed Resource Gateway. If not specified, a default security group is created.</p>"""
    ip_address_type: NotRequired[
        "capo_devops_agent.types.ip_address_type.IpAddressType"
    ]
    """<p>IP address type of the service-managed Resource Gateway.</p>"""
    ipv4_addresses_per_eni: NotRequired[
        "capo_devops_agent.types.max_ipv4_addresses_per_eni.MaxIpv4AddressesPerEni"
    ]
    """<p>Number of IPv4 addresses in each ENI for the service-managed Resource Gateway.</p>"""
    port_ranges: NotRequired["capo_devops_agent.types.port_ranges.PortRanges"]
    """<p>TCP port ranges that a consumer can use to access the resource.</p>"""
    certificate: NotRequired[
        "capo_devops_agent.types.certificate_string.CertificateString"
    ]
    """<p>Certificate for the Private Connection.</p>"""
    dns_resolution: NotRequired[
        "capo_devops_agent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>DNS resolution mode for the resource gateway. Defaults to PUBLIC when not set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedInput) -> dict:
    out: dict = {}
    out["hostAddress"] = value["host_address"]
    out["vpcId"] = value["vpc_id"]
    import capo_devops_agent.types.list_of_subnet_ids

    out["subnetIds"] = capo_devops_agent.types.list_of_subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    if "security_group_ids" in value:
        import capo_devops_agent.types.list_of_security_group_ids

        out["securityGroupIds"] = (
            capo_devops_agent.types.list_of_security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        import capo_devops_agent.types.ip_address_type

        out["ipAddressType"] = capo_devops_agent.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "ipv4_addresses_per_eni" in value:
        out["ipv4AddressesPerEni"] = value["ipv4_addresses_per_eni"]
    if "port_ranges" in value:
        import capo_devops_agent.types.port_ranges

        out["portRanges"] = capo_devops_agent.types.port_ranges.serialize_json(
            value["port_ranges"]
        )
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    if "dns_resolution" in value:
        import capo_devops_agent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            capo_devops_agent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedInput:
    out: ServiceManagedInput = {}  # type: ignore[typeddict-item]
    if data.get("hostAddress") is not None:
        out["host_address"] = data["hostAddress"]
    else:
        out["host_address"] = ""
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_devops_agent.types.list_of_subnet_ids

        out["subnet_ids"] = capo_devops_agent.types.list_of_subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_devops_agent.types.list_of_security_group_ids

        out["security_group_ids"] = (
            capo_devops_agent.types.list_of_security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_devops_agent.types.ip_address_type

        out["ip_address_type"] = (
            capo_devops_agent.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("ipv4AddressesPerEni") is not None:
        out["ipv4_addresses_per_eni"] = data["ipv4AddressesPerEni"]
    if data.get("portRanges") is not None:
        import capo_devops_agent.types.port_ranges

        out["port_ranges"] = capo_devops_agent.types.port_ranges.deserialize_json(
            data["portRanges"]
        )
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    if data.get("dnsResolution") is not None:
        import capo_devops_agent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            capo_devops_agent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    return out
