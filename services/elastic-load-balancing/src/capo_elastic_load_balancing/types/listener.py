"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Listener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_port
    import capo_elastic_load_balancing.types.instance_port
    import capo_elastic_load_balancing.types.protocol
    import capo_elastic_load_balancing.types.ssl_certificate_id


class Listener(TypedDict, closed=True):
    protocol: "capo_elastic_load_balancing.types.protocol.Protocol"
    """<p>The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.</p>"""
    load_balancer_port: (
        "capo_elastic_load_balancing.types.access_point_port.AccessPointPort"
    )
    """<p>The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.</p>"""
    instance_protocol: NotRequired[
        "capo_elastic_load_balancing.types.protocol.Protocol"
    ]
    """<p>The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.</p> <p>If the front-end protocol is TCP or SSL, the back-end protocol must be TCP or SSL. If the front-end protocol is HTTP or HTTPS, the back-end protocol must be HTTP or HTTPS.</p> <p>If there is another listener with the same <code>InstancePort</code> whose <code>InstanceProtocol</code> is secure, (HTTPS or SSL), the listener's <code>InstanceProtocol</code> must also be secure.</p> <p>If there is another listener with the same <code>InstancePort</code> whose <code>InstanceProtocol</code> is HTTP or TCP, the listener's <code>InstanceProtocol</code> must be HTTP or TCP.</p>"""
    instance_port: "capo_elastic_load_balancing.types.instance_port.InstancePort"
    """<p>The port on which the instance is listening.</p>"""
    ssl_certificate_id: NotRequired[
        "capo_elastic_load_balancing.types.ssl_certificate_id.SSLCertificateId"
    ]
    """<p>The Amazon Resource Name (ARN) of the server certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Listener, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    pairs.append(
        (f"{key_prefix}LoadBalancerPort", str(value.get("load_balancer_port", 0)))
    )
    if "instance_protocol" in value:
        pairs.append((f"{key_prefix}InstanceProtocol", str(value["instance_protocol"])))
    pairs.append((f"{key_prefix}InstancePort", str(value["instance_port"])))
    if "ssl_certificate_id" in value:
        pairs.append(
            (f"{key_prefix}SSLCertificateId", str(value["ssl_certificate_id"]))
        )


def deserialize_query(el: Element) -> Listener:
    out: Listener = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    else:
        out["protocol"] = ""
    child_load_balancer_port = el.find("LoadBalancerPort")
    if child_load_balancer_port is not None:
        out["load_balancer_port"] = int(child_load_balancer_port.text or "")
    else:
        out["load_balancer_port"] = 0
    child_instance_protocol = el.find("InstanceProtocol")
    if child_instance_protocol is not None:
        out["instance_protocol"] = str(child_instance_protocol.text or "")
    child_instance_port = el.find("InstancePort")
    if child_instance_port is not None:
        out["instance_port"] = int(child_instance_port.text or "")
    else:
        out["instance_port"] = 0
    child_ssl_certificate_id = el.find("SSLCertificateId")
    if child_ssl_certificate_id is not None:
        out["ssl_certificate_id"] = str(child_ssl_certificate_id.text or "")
    return out
