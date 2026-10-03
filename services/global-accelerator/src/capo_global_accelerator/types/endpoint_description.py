"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_weight
    import capo_global_accelerator.types.generic_boolean
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.health_state


class EndpointDescription(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. </p> <p>An Application Load Balancer can be either internal or internet-facing.</p>"""
    weight: NotRequired["capo_global_accelerator.types.endpoint_weight.EndpointWeight"]
    """<p>The weight associated with the endpoint. When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html">Endpoint weights</a> in the <i>Global Accelerator Developer Guide</i>. </p>"""
    health_state: NotRequired["capo_global_accelerator.types.health_state.HealthState"]
    """<p>The health status of the endpoint.</p>"""
    health_reason: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>Returns a null result.</p>"""
    client_ip_preservation_enabled: NotRequired[
        "capo_global_accelerator.types.generic_boolean.GenericBoolean"
    ]
    """<p>Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false. The default value is true for Application Load Balancers endpoints. </p> <p>If the value is set to true, the client's IP address is preserved in the <code>X-Forwarded-For</code> request header as traffic travels to applications on the endpoint fronted by the accelerator.</p> <p>Client IP address preservation is supported, in specific Amazon Web Services Regions, for endpoints that are Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. IMPORTANT: You cannot use client IP address preservation with Network Load Balancers with TLS listeners.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html"> Preserve client IP addresses in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointDescription) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "weight" in value:
        out["Weight"] = value["weight"]
    if "health_state" in value:
        import capo_global_accelerator.types.health_state

        out["HealthState"] = (
            capo_global_accelerator.types.health_state.serialize_aws_json_1_1(
                value["health_state"]
            )
        )
    if "health_reason" in value:
        out["HealthReason"] = value["health_reason"]
    if "client_ip_preservation_enabled" in value:
        out["ClientIPPreservationEnabled"] = value["client_ip_preservation_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointDescription:
    out: EndpointDescription = {}  # type: ignore[typeddict-item]
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    if data.get("Weight") is not None:
        out["weight"] = data["Weight"]
    if data.get("HealthState") is not None:
        import capo_global_accelerator.types.health_state

        out["health_state"] = (
            capo_global_accelerator.types.health_state.deserialize_aws_json_1_1(
                data["HealthState"]
            )
        )
    if data.get("HealthReason") is not None:
        out["health_reason"] = data["HealthReason"]
    if data.get("ClientIPPreservationEnabled") is not None:
        out["client_ip_preservation_enabled"] = data["ClientIPPreservationEnabled"]
    return out
