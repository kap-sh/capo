"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachLoadBalancerTlsCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class AttachLoadBalancerTlsCertificateRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer to which you want to associate the SSL/TLS certificate.</p>"""
    certificate_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachLoadBalancerTlsCertificateRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["certificateName"] = value["certificate_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachLoadBalancerTlsCertificateRequest:
    out: AttachLoadBalancerTlsCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        out["load_balancer_name"] = ""
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    else:
        out["certificate_name"] = ""
    return out
