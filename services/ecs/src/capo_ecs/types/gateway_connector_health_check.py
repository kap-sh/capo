"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorHealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_connector_health_check_matcher
    import capo_ecs.types.gateway_connector_health_check_protocol
    import capo_ecs.types.string


class GatewayConnectorHealthCheck(TypedDict, closed=True):
    health_check_protocol: NotRequired[
        "capo_ecs.types.gateway_connector_health_check_protocol.GatewayConnectorHealthCheckProtocol"
    ]
    """<p>The protocol that the gateway uses to perform health checks.</p> <p>Valid values:</p> <ul> <li> <p> <code>HTTP</code> - Health checks are performed over HTTP.</p> </li> <li> <p> <code>HTTPS</code> - Health checks are performed over HTTPS.</p> </li> </ul>"""
    health_check_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port that the gateway uses to perform health checks on the targets.</p>"""
    health_check_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The destination path for health check requests.</p>"""
    health_check_timeout_seconds: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The amount of time, in seconds, during which no response from a target means a failed health check.</p>"""
    health_check_interval_seconds: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The approximate amount of time, in seconds, between health checks of an individual target.</p>"""
    healthy_threshold_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of consecutive successful health checks that a target must pass before the gateway considers it healthy.</p>"""
    unhealthy_threshold_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of consecutive failed health checks that a target must fail before the gateway considers it unhealthy.</p>"""
    matcher: NotRequired[
        "capo_ecs.types.gateway_connector_health_check_matcher.GatewayConnectorHealthCheckMatcher"
    ]
    """<p>The HTTP or gRPC codes that indicate a successful health check response from a target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorHealthCheck) -> dict:
    out: dict = {}
    if "health_check_protocol" in value:
        import capo_ecs.types.gateway_connector_health_check_protocol

        out["healthCheckProtocol"] = (
            capo_ecs.types.gateway_connector_health_check_protocol.serialize_aws_json_1_1(
                value["health_check_protocol"]
            )
        )
    if "health_check_port" in value:
        out["healthCheckPort"] = value["health_check_port"]
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "health_check_timeout_seconds" in value:
        out["healthCheckTimeoutSeconds"] = value["health_check_timeout_seconds"]
    if "health_check_interval_seconds" in value:
        out["healthCheckIntervalSeconds"] = value["health_check_interval_seconds"]
    if "healthy_threshold_count" in value:
        out["healthyThresholdCount"] = value["healthy_threshold_count"]
    if "unhealthy_threshold_count" in value:
        out["unhealthyThresholdCount"] = value["unhealthy_threshold_count"]
    if "matcher" in value:
        import capo_ecs.types.gateway_connector_health_check_matcher

        out["matcher"] = (
            capo_ecs.types.gateway_connector_health_check_matcher.serialize_aws_json_1_1(
                value["matcher"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectorHealthCheck:
    out: GatewayConnectorHealthCheck = {}  # type: ignore[typeddict-item]
    if data.get("healthCheckProtocol") is not None:
        import capo_ecs.types.gateway_connector_health_check_protocol

        out["health_check_protocol"] = (
            capo_ecs.types.gateway_connector_health_check_protocol.deserialize_aws_json_1_1(
                data["healthCheckProtocol"]
            )
        )
    if data.get("healthCheckPort") is not None:
        out["health_check_port"] = data["healthCheckPort"]
    if data.get("healthCheckPath") is not None:
        out["health_check_path"] = data["healthCheckPath"]
    if data.get("healthCheckTimeoutSeconds") is not None:
        out["health_check_timeout_seconds"] = data["healthCheckTimeoutSeconds"]
    if data.get("healthCheckIntervalSeconds") is not None:
        out["health_check_interval_seconds"] = data["healthCheckIntervalSeconds"]
    if data.get("healthyThresholdCount") is not None:
        out["healthy_threshold_count"] = data["healthyThresholdCount"]
    if data.get("unhealthyThresholdCount") is not None:
        out["unhealthy_threshold_count"] = data["unhealthyThresholdCount"]
    if data.get("matcher") is not None:
        import capo_ecs.types.gateway_connector_health_check_matcher

        out["matcher"] = (
            capo_ecs.types.gateway_connector_health_check_matcher.deserialize_aws_json_1_1(
                data["matcher"]
            )
        )
    return out
