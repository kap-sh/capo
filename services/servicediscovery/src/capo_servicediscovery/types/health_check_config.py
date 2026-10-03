"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthCheckConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.failure_threshold
    import capo_servicediscovery.types.health_check_type
    import capo_servicediscovery.types.resource_path


class HealthCheckConfig(TypedDict, closed=True):
    type: "capo_servicediscovery.types.health_check_type.HealthCheckType"
    """<p>The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.</p> <important> <p>You can't change the value of <code>Type</code> after you create a health check.</p> </important> <p>You can create the following types of health checks:</p> <ul> <li> <p> <b>HTTP</b>: Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.</p> </li> <li> <p> <b>HTTPS</b>: Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.</p> <important> <p>If you specify HTTPS for the value of <code>Type</code>, the endpoint must support TLS v1.0 or later.</p> </important> </li> <li> <p> <b>TCP</b>: Route 53 tries to establish a TCP connection.</p> <p>If you specify <code>TCP</code> for <code>Type</code>, don't specify a value for <code>ResourcePath</code>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html">How Route 53 Determines Whether an Endpoint Is Healthy</a> in the <i>Route 53 Developer Guide</i>.</p>"""
    resource_path: NotRequired["capo_servicediscovery.types.resource_path.ResourcePath"]
    """<p>The path that you want Route 53 to request when performing health checks. The path can be any value that your endpoint returns an HTTP status code of a 2xx or 3xx format for when the endpoint is healthy. An example file is <code>/docs/route53-health-check.html</code>. Route 53 automatically adds the DNS name for the service. If you don't specify a value for <code>ResourcePath</code>, the default value is <code>/</code>.</p> <p>If you specify <code>TCP</code> for <code>Type</code>, you must <i>not</i> specify a value for <code>ResourcePath</code>.</p>"""
    failure_threshold: NotRequired[
        "capo_servicediscovery.types.failure_threshold.FailureThreshold"
    ]
    """<p>The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or the other way around. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html">How Route 53 Determines Whether an Endpoint Is Healthy</a> in the <i>Route 53 Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckConfig) -> dict:
    out: dict = {}
    import capo_servicediscovery.types.health_check_type

    out["Type"] = capo_servicediscovery.types.health_check_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "resource_path" in value:
        out["ResourcePath"] = value["resource_path"]
    if "failure_threshold" in value:
        out["FailureThreshold"] = value["failure_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HealthCheckConfig:
    out: HealthCheckConfig = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_servicediscovery.types.health_check_type

        out["type"] = (
            capo_servicediscovery.types.health_check_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("HealthCheckConfig.type required")
    if data.get("ResourcePath") is not None:
        out["resource_path"] = data["ResourcePath"]
    if data.get("FailureThreshold") is not None:
        out["failure_threshold"] = data["FailureThreshold"]
    return out
