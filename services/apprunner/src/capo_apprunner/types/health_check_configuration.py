"""Generated from Smithy shape ``com.amazonaws.apprunner#HealthCheckConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.health_check_healthy_threshold
    import capo_apprunner.types.health_check_interval
    import capo_apprunner.types.health_check_path
    import capo_apprunner.types.health_check_protocol
    import capo_apprunner.types.health_check_timeout
    import capo_apprunner.types.health_check_unhealthy_threshold


class HealthCheckConfiguration(TypedDict, closed=True):
    protocol: NotRequired[
        "capo_apprunner.types.health_check_protocol.HealthCheckProtocol"
    ]
    """<p>The IP protocol that App Runner uses to perform health checks for your service.</p> <p>If you set <code>Protocol</code> to <code>HTTP</code>, App Runner sends health check requests to the HTTP path specified by <code>Path</code>.</p> <p>Default: <code>TCP</code> </p>"""
    path: NotRequired["capo_apprunner.types.health_check_path.HealthCheckPath"]
    """<p>The URL that health check requests are sent to.</p> <p> <code>Path</code> is only applicable when you set <code>Protocol</code> to <code>HTTP</code>.</p> <p>Default: <code>"/"</code> </p>"""
    interval: NotRequired[
        "capo_apprunner.types.health_check_interval.HealthCheckInterval"
    ]
    """<p>The time interval, in seconds, between health checks.</p> <p>Default: <code>5</code> </p>"""
    timeout: NotRequired["capo_apprunner.types.health_check_timeout.HealthCheckTimeout"]
    """<p>The time, in seconds, to wait for a health check response before deciding it failed.</p> <p>Default: <code>2</code> </p>"""
    healthy_threshold: NotRequired[
        "capo_apprunner.types.health_check_healthy_threshold.HealthCheckHealthyThreshold"
    ]
    """<p>The number of consecutive checks that must succeed before App Runner decides that the service is healthy.</p> <p>Default: <code>1</code> </p>"""
    unhealthy_threshold: NotRequired[
        "capo_apprunner.types.health_check_unhealthy_threshold.HealthCheckUnhealthyThreshold"
    ]
    """<p>The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.</p> <p>Default: <code>5</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthCheckConfiguration) -> dict:
    out: dict = {}
    if "protocol" in value:
        import capo_apprunner.types.health_check_protocol

        out["Protocol"] = (
            capo_apprunner.types.health_check_protocol.serialize_aws_json_1_0(
                value["protocol"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "healthy_threshold" in value:
        out["HealthyThreshold"] = value["healthy_threshold"]
    if "unhealthy_threshold" in value:
        out["UnhealthyThreshold"] = value["unhealthy_threshold"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HealthCheckConfiguration:
    out: HealthCheckConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Protocol") is not None:
        import capo_apprunner.types.health_check_protocol

        out["protocol"] = (
            capo_apprunner.types.health_check_protocol.deserialize_aws_json_1_0(
                data["Protocol"]
            )
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Interval") is not None:
        out["interval"] = data["Interval"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("HealthyThreshold") is not None:
        out["healthy_threshold"] = data["HealthyThreshold"]
    if data.get("UnhealthyThreshold") is not None:
        out["unhealthy_threshold"] = data["UnhealthyThreshold"]
    return out
