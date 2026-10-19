"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateConditionalForwarderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.remote_domain_name


class CreateConditionalForwarderRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The directory ID of the Amazon Web Services directory for which you are creating the conditional forwarder.</p>"""
    remote_domain_name: (
        "capo_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.</p>"""
    dns_ip_addrs: NotRequired["capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"]
    """<p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    dns_ipv6_addrs: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConditionalForwarderRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConditionalForwarderRequest:
    out: CreateConditionalForwarderRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        out["remote_domain_name"] = ""
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
    return out
