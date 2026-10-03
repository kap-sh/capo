"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateListenerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.actions
    import capo_elastic_load_balancing_v2.types.alpn_policy_name
    import capo_elastic_load_balancing_v2.types.certificate_list
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.mutual_authentication_attributes
    import capo_elastic_load_balancing_v2.types.port
    import capo_elastic_load_balancing_v2.types.protocol_enum
    import capo_elastic_load_balancing_v2.types.ssl_policy_name
    import capo_elastic_load_balancing_v2.types.tag_list


class CreateListenerInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    protocol: NotRequired[
        "capo_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC. You can’t specify the UDP, TCP_UDP, QUIC, or TCP_QUIC protocol if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.</p>"""
    port: NotRequired["capo_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port on which the load balancer is listening. You can't specify a port for a Gateway Load Balancer.</p>"""
    ssl_policy: NotRequired[
        "capo_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
    ]
    """<p>[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html">Security policies</a> in the <i>Application Load Balancers Guide</i> and <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html">Security policies</a> in the <i>Network Load Balancers Guide</i>.</p>"""
    certificates: NotRequired[
        "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>"""
    default_actions: NotRequired["capo_elastic_load_balancing_v2.types.actions.Actions"]
    """<p>The actions for the default rule.</p>"""
    alpn_policy: NotRequired[
        "capo_elastic_load_balancing_v2.types.alpn_policy_name.AlpnPolicyName"
    ]
    """<p>[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:</p> <ul> <li> <p> <code>HTTP1Only</code> </p> </li> <li> <p> <code>HTTP2Only</code> </p> </li> <li> <p> <code>HTTP2Optional</code> </p> </li> <li> <p> <code>HTTP2Preferred</code> </p> </li> <li> <p> <code>None</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies">ALPN policies</a> in the <i>Network Load Balancers Guide</i>.</p>"""
    tags: NotRequired["capo_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags to assign to the listener.</p>"""
    mutual_authentication: NotRequired[
        "capo_elastic_load_balancing_v2.types.mutual_authentication_attributes.MutualAuthenticationAttributes"
    ]
    """<p>[HTTPS listeners] The mutual authentication configuration information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateListenerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "protocol" in value:
        import capo_elastic_load_balancing_v2.types.protocol_enum

        capo_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "ssl_policy" in value:
        pairs.append((f"{key_prefix}SslPolicy", str(value["ssl_policy"])))
    if "certificates" in value:
        import capo_elastic_load_balancing_v2.types.certificate_list

        capo_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{key_prefix}Certificates"
        )
    if "default_actions" in value:
        import capo_elastic_load_balancing_v2.types.actions

        capo_elastic_load_balancing_v2.types.actions.serialize_query(
            value["default_actions"], pairs, f"{key_prefix}DefaultActions"
        )
    if "alpn_policy" in value:
        import capo_elastic_load_balancing_v2.types.alpn_policy_name

        capo_elastic_load_balancing_v2.types.alpn_policy_name.serialize_query(
            value["alpn_policy"], pairs, f"{key_prefix}AlpnPolicy"
        )
    if "tags" in value:
        import capo_elastic_load_balancing_v2.types.tag_list

        capo_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "mutual_authentication" in value:
        import capo_elastic_load_balancing_v2.types.mutual_authentication_attributes

        capo_elastic_load_balancing_v2.types.mutual_authentication_attributes.serialize_query(
            value["mutual_authentication"], pairs, f"{key_prefix}MutualAuthentication"
        )


def deserialize_query(el: Element) -> CreateListenerInput:
    out: CreateListenerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_elastic_load_balancing_v2.types.protocol_enum

        out["protocol"] = (
            capo_elastic_load_balancing_v2.types.protocol_enum.deserialize_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_ssl_policy = el.find("SslPolicy")
    if child_ssl_policy is not None:
        out["ssl_policy"] = str(child_ssl_policy.text or "")
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import capo_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            capo_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    child_default_actions = el.find("DefaultActions")
    if child_default_actions is not None:
        import capo_elastic_load_balancing_v2.types.actions

        out["default_actions"] = (
            capo_elastic_load_balancing_v2.types.actions.deserialize_query(
                child_default_actions
            )
        )
    child_alpn_policy = el.find("AlpnPolicy")
    if child_alpn_policy is not None:
        import capo_elastic_load_balancing_v2.types.alpn_policy_name

        out["alpn_policy"] = (
            capo_elastic_load_balancing_v2.types.alpn_policy_name.deserialize_query(
                child_alpn_policy
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing_v2.types.tag_list

        out["tags"] = capo_elastic_load_balancing_v2.types.tag_list.deserialize_query(
            child_tags
        )
    child_mutual_authentication = el.find("MutualAuthentication")
    if child_mutual_authentication is not None:
        import capo_elastic_load_balancing_v2.types.mutual_authentication_attributes

        out["mutual_authentication"] = (
            capo_elastic_load_balancing_v2.types.mutual_authentication_attributes.deserialize_query(
                child_mutual_authentication
            )
        )
    return out
