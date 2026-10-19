"""Generated from Smithy shape ``com.amazonaws.eventbridge#Primary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.health_check


class Primary(TypedDict, closed=True):
    health_check: "capo_eventbridge.types.health_check.HealthCheck"
    """<p>The ARN of the health check used by the endpoint to determine whether failover is triggered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Primary) -> dict:
    out: dict = {}
    out["HealthCheck"] = value["health_check"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Primary:
    out: Primary = {}  # type: ignore[typeddict-item]
    if data.get("HealthCheck") is not None:
        out["health_check"] = data["HealthCheck"]
    else:
        out["health_check"] = ""
    return out
