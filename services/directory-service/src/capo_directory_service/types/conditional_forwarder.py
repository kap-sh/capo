"""Generated from Smithy shape ``com.amazonaws.directoryservice#ConditionalForwarder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.remote_domain_name
    import capo_directory_service.types.replication_scope


class ConditionalForwarder(TypedDict, closed=True):
    remote_domain_name: NotRequired[
        "capo_directory_service.types.remote_domain_name.RemoteDomainName"
    ]
    """<p>The fully qualified domain name (FQDN) of the remote domains pointed to by the conditional forwarder.</p>"""
    dns_ip_addrs: NotRequired["capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"]
    """<p>The IP addresses of the remote DNS server associated with RemoteDomainName. This is the IP address of the DNS server that your conditional forwarder points to.</p>"""
    dns_ipv6_addrs: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName. This is the IPv6 address of the DNS server that your conditional forwarder points to.</p>"""
    replication_scope: NotRequired[
        "capo_directory_service.types.replication_scope.ReplicationScope"
    ]
    """<p>The replication scope of the conditional forwarder. The only allowed value is <code>Domain</code>, which will replicate the conditional forwarder to all of the domain controllers for your Amazon Web Services directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionalForwarder) -> dict:
    out: dict = {}
    if "remote_domain_name" in value:
        out["RemoteDomainName"] = value["remote_domain_name"]
    if "dns_ip_addrs" in value:
        import capo_directory_service.types.dns_ip_addrs

        out["DnsIpAddrs"] = (
            capo_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
                value["dns_ip_addrs"]
            )
        )
    if "dns_ipv6_addrs" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["DnsIpv6Addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["dns_ipv6_addrs"]
            )
        )
    if "replication_scope" in value:
        import capo_directory_service.types.replication_scope

        out["ReplicationScope"] = (
            capo_directory_service.types.replication_scope.serialize_aws_json_1_1(
                value["replication_scope"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionalForwarder:
    out: ConditionalForwarder = {}  # type: ignore[typeddict-item]
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    if data.get("DnsIpAddrs") is not None:
        import capo_directory_service.types.dns_ip_addrs

        out["dns_ip_addrs"] = (
            capo_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["DnsIpAddrs"]
            )
        )
    if data.get("DnsIpv6Addrs") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["dns_ipv6_addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["DnsIpv6Addrs"]
            )
        )
    if data.get("ReplicationScope") is not None:
        import capo_directory_service.types.replication_scope

        out["replication_scope"] = (
            capo_directory_service.types.replication_scope.deserialize_aws_json_1_1(
                data["ReplicationScope"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionalForwarder) -> dict:
    out: dict = {}
    if "remote_domain_name" in value:
        out["RemoteDomainName"] = value["remote_domain_name"]
    if "dns_ip_addrs" in value:
        import capo_directory_service.types.dns_ip_addrs

        out["DnsIpAddrs"] = capo_directory_service.types.dns_ip_addrs.serialize_cbor(
            value["dns_ip_addrs"]
        )
    if "dns_ipv6_addrs" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["DnsIpv6Addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_cbor(
                value["dns_ipv6_addrs"]
            )
        )
    if "replication_scope" in value:
        import capo_directory_service.types.replication_scope

        out["ReplicationScope"] = (
            capo_directory_service.types.replication_scope.serialize_cbor(
                value["replication_scope"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConditionalForwarder:
    out: ConditionalForwarder = {}  # type: ignore[typeddict-item]
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    if data.get("DnsIpAddrs") is not None:
        import capo_directory_service.types.dns_ip_addrs

        out["dns_ip_addrs"] = (
            capo_directory_service.types.dns_ip_addrs.deserialize_cbor(
                data["DnsIpAddrs"]
            )
        )
    if data.get("DnsIpv6Addrs") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["dns_ipv6_addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_cbor(
                data["DnsIpv6Addrs"]
            )
        )
    if data.get("ReplicationScope") is not None:
        import capo_directory_service.types.replication_scope

        out["replication_scope"] = (
            capo_directory_service.types.replication_scope.deserialize_cbor(
                data["ReplicationScope"]
            )
        )
    return out
