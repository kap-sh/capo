"""Generated from Smithy shape ``com.amazonaws.rtbfabric#HealthCheckConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.status_code_matcher


class HealthCheckConfig(TypedDict, closed=True):
    port: "int"
    """<p>The port to use for health check probes. Valid range is 80 to 65535.</p>"""
    path: "str"
    """<p>The destination path for the health check request. Must start with <code>/</code>.</p>"""
    protocol: NotRequired["capo_rtbfabric.types.protocol.Protocol"]
    """<p>The protocol to use for health check probes.</p>"""
    timeout_ms: NotRequired["int"]
    """<p>The timeout for each health check probe, in milliseconds. Valid range is 100 to 5000.</p>"""
    interval_seconds: NotRequired["int"]
    """<p>The interval between health check probes, in seconds. Valid range is 5 to 60.</p>"""
    status_code_matcher: NotRequired[
        "capo_rtbfabric.types.status_code_matcher.StatusCodeMatcher"
    ]
    """<p>The expected HTTP status code or status code pattern from healthy instances. Supports a single code (for example, <code>200</code>), a range (for example, <code>200-299</code>), or a comma-separated list (for example, <code>200,204</code>).</p>"""
    healthy_threshold_count: NotRequired["int"]
    """<p>The number of consecutive successful health checks required before an instance is considered healthy. Valid range is 2 to 10.</p>"""
    unhealthy_threshold_count: NotRequired["int"]
    """<p>The number of consecutive failed health checks required before an instance is considered unhealthy. Valid range is 2 to 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthCheckConfig) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["path"] = value["path"]
    if "protocol" in value:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.serialize_json(
            value["protocol"]
        )
    if "timeout_ms" in value:
        out["timeoutMs"] = value["timeout_ms"]
    if "interval_seconds" in value:
        out["intervalSeconds"] = value["interval_seconds"]
    if "status_code_matcher" in value:
        out["statusCodeMatcher"] = value["status_code_matcher"]
    if "healthy_threshold_count" in value:
        out["healthyThresholdCount"] = value["healthy_threshold_count"]
    if "unhealthy_threshold_count" in value:
        out["unhealthyThresholdCount"] = value["unhealthy_threshold_count"]
    return out


def deserialize_json(data: dict) -> HealthCheckConfig:
    out: HealthCheckConfig = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("protocol") is not None:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    if data.get("timeoutMs") is not None:
        out["timeout_ms"] = data["timeoutMs"]
    if data.get("intervalSeconds") is not None:
        out["interval_seconds"] = data["intervalSeconds"]
    if data.get("statusCodeMatcher") is not None:
        out["status_code_matcher"] = data["statusCodeMatcher"]
    if data.get("healthyThresholdCount") is not None:
        out["healthy_threshold_count"] = data["healthyThresholdCount"]
    if data.get("unhealthyThresholdCount") is not None:
        out["unhealthy_threshold_count"] = data["unhealthyThresholdCount"]
    return out
