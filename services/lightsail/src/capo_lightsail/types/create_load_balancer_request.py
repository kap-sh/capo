"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateLoadBalancerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.domain_name_list
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.port
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class CreateLoadBalancerRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your load balancer.</p>"""
    instance_port: "capo_lightsail.types.port.Port"
    """<p>The instance port where you're creating your load balancer.</p>"""
    health_check_path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (<code>"/"</code>).</p> <p>You may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.</p>"""
    certificate_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate.</p> <p>If you specify <code>certificateName</code>, then <code>certificateDomainName</code> is required (and vice-versa).</p>"""
    certificate_domain_name: NotRequired["capo_lightsail.types.domain_name.DomainName"]
    """<p>The domain name with which your certificate is associated (<code>example.com</code>).</p> <p>If you specify <code>certificateDomainName</code>, then <code>certificateName</code> is required (and vice-versa).</p>"""
    certificate_alternative_names: NotRequired[
        "capo_lightsail.types.domain_name_list.DomainNameList"
    ]
    """<p>The optional alternative domains and subdomains to use with your SSL/TLS certificate (<code>www.example.com</code>, <code>example.com</code>, <code>m.example.com</code>, <code>blog.example.com</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    ip_address_type: NotRequired["capo_lightsail.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the load balancer.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>"""
    tls_policy_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the TLS policy to apply to the load balancer.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html">GetLoadBalancerTlsPolicies</a> action to get a list of TLS policy names that you can specify.</p> <p>For more information about load balancer TLS policies, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy">Configuring TLS security policies on your Amazon Lightsail load balancers</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLoadBalancerRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["instancePort"] = value.get("instance_port", 0)
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "certificate_domain_name" in value:
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
    if "ip_address_type" in value:
        import capo_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "tls_policy_name" in value:
        out["tlsPolicyName"] = value["tls_policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLoadBalancerRequest:
    out: CreateLoadBalancerRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "CreateLoadBalancerRequest.load_balancer_name required"
        )
    if data.get("instancePort") is not None:
        out["instance_port"] = data["instancePort"]
    else:
        out["instance_port"] = 0
    if data.get("healthCheckPath") is not None:
        out["health_check_path"] = data["healthCheckPath"]
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    if data.get("certificateDomainName") is not None:
        out["certificate_domain_name"] = data["certificateDomainName"]
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
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if data.get("tlsPolicyName") is not None:
        out["tls_policy_name"] = data["tlsPolicyName"]
    return out
