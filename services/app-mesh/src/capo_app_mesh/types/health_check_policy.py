"""Generated from Smithy shape ``com.amazonaws.appmesh#HealthCheckPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.health_check_interval_millis
    import capo_app_mesh.types.health_check_threshold
    import capo_app_mesh.types.health_check_timeout_millis
    import capo_app_mesh.types.port_number
    import capo_app_mesh.types.port_protocol


class HealthCheckPolicy(TypedDict, closed=True):
    timeout_millis: (
        "capo_app_mesh.types.health_check_timeout_millis.HealthCheckTimeoutMillis"
    )
    """<p>The amount of time to wait when receiving a response from the health check, in milliseconds.</p>"""
    interval_millis: (
        "capo_app_mesh.types.health_check_interval_millis.HealthCheckIntervalMillis"
    )
    """<p>The time period in milliseconds between each health check execution.</p>"""
    protocol: "capo_app_mesh.types.port_protocol.PortProtocol"
    """<p>The protocol for the health check request. If you specify <code>grpc</code>, then your service must conform to the <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">GRPC Health Checking Protocol</a>.</p>"""
    port: NotRequired["capo_app_mesh.types.port_number.PortNumber"]
    """<p>The destination port for the health check request. This port must match the port defined in the <a>PortMapping</a> for the listener.</p>"""
    path: NotRequired["str"]
    """<p>The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.</p>"""
    healthy_threshold: "capo_app_mesh.types.health_check_threshold.HealthCheckThreshold"
    """<p>The number of consecutive successful health checks that must occur before declaring listener healthy.</p>"""
    unhealthy_threshold: (
        "capo_app_mesh.types.health_check_threshold.HealthCheckThreshold"
    )
    """<p>The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthCheckPolicy) -> dict:
    out: dict = {}
    out["timeoutMillis"] = value["timeout_millis"]
    out["intervalMillis"] = value["interval_millis"]
    out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    if "path" in value:
        out["path"] = value["path"]
    out["healthyThreshold"] = value["healthy_threshold"]
    out["unhealthyThreshold"] = value["unhealthy_threshold"]
    return out


def deserialize_json(data: dict) -> HealthCheckPolicy:
    out: HealthCheckPolicy = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMillis") is not None:
        out["timeout_millis"] = data["timeoutMillis"]
    else:
        raise DeserializationError("HealthCheckPolicy.timeout_millis required")
    if data.get("intervalMillis") is not None:
        out["interval_millis"] = data["intervalMillis"]
    else:
        raise DeserializationError("HealthCheckPolicy.interval_millis required")
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    else:
        raise DeserializationError("HealthCheckPolicy.protocol required")
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("healthyThreshold") is not None:
        out["healthy_threshold"] = data["healthyThreshold"]
    else:
        raise DeserializationError("HealthCheckPolicy.healthy_threshold required")
    if data.get("unhealthyThreshold") is not None:
        out["unhealthy_threshold"] = data["unhealthyThreshold"]
    else:
        raise DeserializationError("HealthCheckPolicy.unhealthy_threshold required")
    return out
