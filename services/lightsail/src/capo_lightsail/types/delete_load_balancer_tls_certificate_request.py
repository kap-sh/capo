"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteLoadBalancerTlsCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name


class DeleteLoadBalancerTlsCertificateRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The load balancer name.</p>"""
    certificate_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The SSL/TLS certificate name.</p>"""
    force: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>When <code>true</code>, forces the deletion of an SSL/TLS certificate.</p> <p>There can be two certificates associated with a Lightsail load balancer: the primary and the backup. The <code>force</code> parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLoadBalancerTlsCertificateRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["certificateName"] = value["certificate_name"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLoadBalancerTlsCertificateRequest:
    out: DeleteLoadBalancerTlsCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        out["load_balancer_name"] = ""
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    else:
        out["certificate_name"] = ""
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
