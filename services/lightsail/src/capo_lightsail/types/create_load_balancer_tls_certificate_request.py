"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateLoadBalancerTlsCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.domain_name_list
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class CreateLoadBalancerTlsCertificateRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The load balancer name where you want to create the SSL/TLS certificate.</p>"""
    certificate_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The SSL/TLS certificate name.</p> <p>You can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see <a href="http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html">Limits</a>.</p>"""
    certificate_domain_name: "capo_lightsail.types.domain_name.DomainName"
    """<p>The domain name (<code>example.com</code>) for your SSL/TLS certificate.</p>"""
    certificate_alternative_names: NotRequired[
        "capo_lightsail.types.domain_name_list.DomainNameList"
    ]
    """<p>An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (<code>*.example.com</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLoadBalancerTlsCertificateRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["certificateName"] = value["certificate_name"]
    out["certificateDomainName"] = value["certificate_domain_name"]
    if "certificate_alternative_names" in value:
        import capo_lightsail.types.domain_name_list

        out["certificateAlternativeNames"] = (
            capo_lightsail.types.domain_name_list.serialize_aws_json_1_1(
                value["certificate_alternative_names"]
            )
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLoadBalancerTlsCertificateRequest:
    out: CreateLoadBalancerTlsCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "CreateLoadBalancerTlsCertificateRequest.load_balancer_name required"
        )
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError(
            "CreateLoadBalancerTlsCertificateRequest.certificate_name required"
        )
    if data.get("certificateDomainName") is not None:
        out["certificate_domain_name"] = data["certificateDomainName"]
    else:
        raise DeserializationError(
            "CreateLoadBalancerTlsCertificateRequest.certificate_domain_name required"
        )
    if data.get("certificateAlternativeNames") is not None:
        import capo_lightsail.types.domain_name_list

        out["certificate_alternative_names"] = (
            capo_lightsail.types.domain_name_list.deserialize_aws_json_1_1(
                data["certificateAlternativeNames"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
