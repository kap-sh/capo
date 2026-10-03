"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateLoadBalancerAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_attribute_name
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string_max256


class UpdateLoadBalancerAttributeRequest(TypedDict, closed=True):
    load_balancer_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer that you want to modify (<code>my-load-balancer</code>.</p>"""
    attribute_name: (
        "capo_lightsail.types.load_balancer_attribute_name.LoadBalancerAttributeName"
    )
    """<p>The name of the attribute you want to update.</p>"""
    attribute_value: "capo_lightsail.types.string_max256.StringMax256"
    """<p>The value that you want to specify for the attribute name.</p> <p>The following values are supported depending on what you specify for the <code>attributeName</code> request parameter:</p> <ul> <li> <p>If you specify <code>HealthCheckPath</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be the path to ping on the target (for example, <code>/weather/us/wa/seattle</code>).</p> </li> <li> <p>If you specify <code>SessionStickinessEnabled</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be <code>true</code> to activate session stickiness or <code>false</code> to deactivate session stickiness.</p> </li> <li> <p>If you specify <code>SessionStickiness_LB_CookieDurationSeconds</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be an interger that represents the cookie duration in seconds.</p> </li> <li> <p>If you specify <code>HttpsRedirectionEnabled</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be <code>true</code> to activate HTTP to HTTPS redirection or <code>false</code> to deactivate HTTP to HTTPS redirection.</p> </li> <li> <p>If you specify <code>TlsPolicyName</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be the name of the TLS policy.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html">GetLoadBalancerTlsPolicies</a> action to get a list of TLS policy names that you can specify.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLoadBalancerAttributeRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    import capo_lightsail.types.load_balancer_attribute_name

    out["attributeName"] = (
        capo_lightsail.types.load_balancer_attribute_name.serialize_aws_json_1_1(
            value["attribute_name"]
        )
    )
    out["attributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLoadBalancerAttributeRequest:
    out: UpdateLoadBalancerAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "UpdateLoadBalancerAttributeRequest.load_balancer_name required"
        )
    if data.get("attributeName") is not None:
        import capo_lightsail.types.load_balancer_attribute_name

        out["attribute_name"] = (
            capo_lightsail.types.load_balancer_attribute_name.deserialize_aws_json_1_1(
                data["attributeName"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLoadBalancerAttributeRequest.attribute_name required"
        )
    if data.get("attributeValue") is not None:
        out["attribute_value"] = data["attributeValue"]
    else:
        raise DeserializationError(
            "UpdateLoadBalancerAttributeRequest.attribute_value required"
        )
    return out
