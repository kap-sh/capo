"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_properties
    import capo_network_firewall.types.proxy_domain_name
    import capo_network_firewall.types.resource_arn


class ProxySettings(TypedDict, closed=True):
    listener_properties: (
        "capo_network_firewall.types.listener_properties.ListenerProperties"
    )
    """<p>The listeners of the firewall's proxy. Specify at least one listener, and at most one HTTP listener and one HTTPS listener. Each listener needs a port from 1 to 65535, and the two listeners must use different ports.</p> <p>If you don't specify listeners when you create the firewall, the firewall listens for HTTP on port 3128 and HTTPS on port 8443.</p>"""
    certificate_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the certificate that the firewall's HTTPS proxy listener presents to clients. The certificate must be an Certificate Manager (ACM) certificate in the same account and Region as the firewall. Its subject alternative names must cover <code>DomainName</code>, either exactly or with a wildcard that matches exactly one label. For example, <code>*.example.com</code> covers <code>proxy.example.com</code>. If you don't specify this, Network Firewall uses a certificate that it manages for a domain name that it generates.</p> <p>You manage and renew the certificate in ACM, and Network Firewall uses renewed certificates automatically. While the firewall uses the certificate, you can't delete it from ACM. Your clients must trust the certificate's certificate authority.</p> <p>If you specify <code>CertificateArn</code>, you must also specify <code>DomainName</code>. You can set them only when you create the firewall. When you call <code>UpdateProxySettings</code>, specify the same values.</p>"""
    domain_name: NotRequired[
        "capo_network_firewall.types.proxy_domain_name.ProxyDomainName"
    ]
    """<p>The domain name that your clients use to reach the firewall's proxy. The name must have at least two labels and at most 253 characters. It can't contain a wildcard or use the <code>proxy-<i>id</i>.nfw.<i>region</i>.amazonaws.com</code> format, and the certificate in <code>CertificateArn</code> must cover it. If you don't specify this, Network Firewall generates a domain name.</p> <p>Network Firewall creates the Route 53 private hosted zones that resolve this name to the firewall endpoints, so you don't need to configure DNS. A VPC can have only one private hosted zone with a given name. If a VPC that the firewall serves already has one with this name, Network Firewall can't set up the Availability Zones in that VPC.</p> <p>If you specify <code>DomainName</code>, you must also specify <code>CertificateArn</code>. You can set them only when you create the firewall. When you call <code>UpdateProxySettings</code>, specify the same values.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxySettings) -> dict:
    out: dict = {}
    import capo_network_firewall.types.listener_properties

    out["ListenerProperties"] = (
        capo_network_firewall.types.listener_properties.serialize_aws_json_1_0(
            value["listener_properties"]
        )
    )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxySettings:
    out: ProxySettings = {}  # type: ignore[typeddict-item]
    if data.get("ListenerProperties") is not None:
        import capo_network_firewall.types.listener_properties

        out["listener_properties"] = (
            capo_network_firewall.types.listener_properties.deserialize_aws_json_1_0(
                data["ListenerProperties"]
            )
        )
    else:
        out["listener_properties"] = []
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProxySettings) -> dict:
    out: dict = {}
    import capo_network_firewall.types.listener_properties

    out["ListenerProperties"] = (
        capo_network_firewall.types.listener_properties.serialize_cbor(
            value["listener_properties"]
        )
    )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    return out


def deserialize_cbor(data: dict) -> ProxySettings:
    out: ProxySettings = {}  # type: ignore[typeddict-item]
    if data.get("ListenerProperties") is not None:
        import capo_network_firewall.types.listener_properties

        out["listener_properties"] = (
            capo_network_firewall.types.listener_properties.deserialize_cbor(
                data["ListenerProperties"]
            )
        )
    else:
        out["listener_properties"] = []
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    return out
