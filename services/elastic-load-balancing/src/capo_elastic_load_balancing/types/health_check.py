"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#HealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.health_check_interval
    import capo_elastic_load_balancing.types.health_check_target
    import capo_elastic_load_balancing.types.health_check_timeout
    import capo_elastic_load_balancing.types.healthy_threshold
    import capo_elastic_load_balancing.types.unhealthy_threshold


class HealthCheck(TypedDict, closed=True):
    target: "capo_elastic_load_balancing.types.health_check_target.HealthCheckTarget"
    """<p>The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.</p> <p>TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.</p> <p>SSL is also specified as SSL: port pair, for example, SSL:5000.</p> <p>For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than "200 OK" within the timeout period is considered unhealthy.</p> <p>The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.</p>"""
    interval: (
        "capo_elastic_load_balancing.types.health_check_interval.HealthCheckInterval"
    )
    """<p>The approximate interval, in seconds, between health checks of an individual instance.</p>"""
    timeout: "capo_elastic_load_balancing.types.health_check_timeout.HealthCheckTimeout"
    """<p>The amount of time, in seconds, during which no response means a failed health check.</p> <p>This value must be less than the <code>Interval</code> value.</p>"""
    unhealthy_threshold: (
        "capo_elastic_load_balancing.types.unhealthy_threshold.UnhealthyThreshold"
    )
    """<p>The number of consecutive health check failures required before moving the instance to the <code>Unhealthy</code> state.</p>"""
    healthy_threshold: (
        "capo_elastic_load_balancing.types.healthy_threshold.HealthyThreshold"
    )
    """<p>The number of consecutive health checks successes required before moving the instance to the <code>Healthy</code> state.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HealthCheck, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Target", str(value["target"])))
    pairs.append((f"{key_prefix}Interval", str(value["interval"])))
    pairs.append((f"{key_prefix}Timeout", str(value["timeout"])))
    pairs.append((f"{key_prefix}UnhealthyThreshold", str(value["unhealthy_threshold"])))
    pairs.append((f"{key_prefix}HealthyThreshold", str(value["healthy_threshold"])))


def deserialize_query(el: Element) -> HealthCheck:
    out: HealthCheck = {}  # type: ignore[typeddict-item]
    child_target = el.find("Target")
    if child_target is not None:
        out["target"] = str(child_target.text or "")
    else:
        raise DeserializationError("HealthCheck.target required")
    child_interval = el.find("Interval")
    if child_interval is not None:
        out["interval"] = int(child_interval.text or "")
    else:
        raise DeserializationError("HealthCheck.interval required")
    child_timeout = el.find("Timeout")
    if child_timeout is not None:
        out["timeout"] = int(child_timeout.text or "")
    else:
        raise DeserializationError("HealthCheck.timeout required")
    child_unhealthy_threshold = el.find("UnhealthyThreshold")
    if child_unhealthy_threshold is not None:
        out["unhealthy_threshold"] = int(child_unhealthy_threshold.text or "")
    else:
        raise DeserializationError("HealthCheck.unhealthy_threshold required")
    child_healthy_threshold = el.find("HealthyThreshold")
    if child_healthy_threshold is not None:
        out["healthy_threshold"] = int(child_healthy_threshold.text or "")
    else:
        raise DeserializationError("HealthCheck.healthy_threshold required")
    return out
