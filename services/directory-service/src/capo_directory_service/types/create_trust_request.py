"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateTrustRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.remote_domain_name
    import capo_directory_service.types.selective_auth
    import capo_directory_service.types.trust_direction
    import capo_directory_service.types.trust_password
    import capo_directory_service.types.trust_type


class CreateTrustRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The Directory ID of the Managed Microsoft AD directory for which to establish the trust relationship.</p>"""
    remote_domain_name: (
        "capo_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.</p>"""
    trust_password: "capo_directory_service.types.trust_password.TrustPassword"
    """<p>The trust password. The trust password must be the same password that was used when creating the trust relationship on the external domain.</p>"""
    trust_direction: "capo_directory_service.types.trust_direction.TrustDirection"
    """<p>The direction of the trust relationship.</p>"""
    trust_type: NotRequired["capo_directory_service.types.trust_type.TrustType"]
    """<p>The trust relationship type. <code>Forest</code> is the default.</p>"""
    conditional_forwarder_ip_addrs: NotRequired[
        "capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"
    ]
    """<p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    conditional_forwarder_ipv6_addrs: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    selective_auth: NotRequired[
        "capo_directory_service.types.selective_auth.SelectiveAuth"
    ]
    """<p>Optional parameter to enable selective authentication for the trust.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RemoteDomainName"] = value["remote_domain_name"]
    out["TrustPassword"] = value["trust_password"]
    import capo_directory_service.types.trust_direction

    out["TrustDirection"] = (
        capo_directory_service.types.trust_direction.serialize_aws_json_1_1(
            value["trust_direction"]
        )
    )
    if "trust_type" in value:
        import capo_directory_service.types.trust_type

        out["TrustType"] = (
            capo_directory_service.types.trust_type.serialize_aws_json_1_1(
                value["trust_type"]
            )
        )
    if "conditional_forwarder_ip_addrs" in value:
        import capo_directory_service.types.dns_ip_addrs

        out["ConditionalForwarderIpAddrs"] = (
            capo_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
                value["conditional_forwarder_ip_addrs"]
            )
        )
    if "conditional_forwarder_ipv6_addrs" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["ConditionalForwarderIpv6Addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["conditional_forwarder_ipv6_addrs"]
            )
        )
    if "selective_auth" in value:
        import capo_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            capo_directory_service.types.selective_auth.serialize_aws_json_1_1(
                value["selective_auth"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustRequest:
    out: CreateTrustRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        out["remote_domain_name"] = ""
    if data.get("TrustPassword") is not None:
        out["trust_password"] = data["TrustPassword"]
    else:
        out["trust_password"] = ""
    if data.get("TrustDirection") is not None:
        import capo_directory_service.types.trust_direction

        out["trust_direction"] = (
            capo_directory_service.types.trust_direction.deserialize_aws_json_1_1(
                data["TrustDirection"]
            )
        )
    else:
        import typing

        out["trust_direction"] = typing.cast(
            "capo_directory_service.types.trust_direction.TrustDirection", ""
        )
    if data.get("TrustType") is not None:
        import capo_directory_service.types.trust_type

        out["trust_type"] = (
            capo_directory_service.types.trust_type.deserialize_aws_json_1_1(
                data["TrustType"]
            )
        )
    if data.get("ConditionalForwarderIpAddrs") is not None:
        import capo_directory_service.types.dns_ip_addrs

        out["conditional_forwarder_ip_addrs"] = (
            capo_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["ConditionalForwarderIpAddrs"]
            )
        )
    if data.get("ConditionalForwarderIpv6Addrs") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["conditional_forwarder_ipv6_addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["ConditionalForwarderIpv6Addrs"]
            )
        )
    if data.get("SelectiveAuth") is not None:
        import capo_directory_service.types.selective_auth

        out["selective_auth"] = (
            capo_directory_service.types.selective_auth.deserialize_aws_json_1_1(
                data["SelectiveAuth"]
            )
        )
    return out


def redact_sensitive(value: CreateTrustRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "trust_password" in value:
        out["trust_password"] = "*** Sensitive Data Redacted ***"
    return out
