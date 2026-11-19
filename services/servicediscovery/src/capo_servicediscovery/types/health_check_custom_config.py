"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthCheckCustomConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.failure_threshold


class HealthCheckCustomConfig(TypedDict, closed=True):
    failure_threshold: NotRequired[
        "capo_servicediscovery.types.failure_threshold.FailureThreshold"
    ]
    """<important> <p>This parameter is no longer supported and is always set to 1. Cloud Map waits for approximately 30 seconds after receiving an <code>UpdateInstanceCustomHealthStatus</code> request before changing the status of the service instance.</p> </important> <p>The number of 30-second intervals that you want Cloud Map to wait after receiving an <code>UpdateInstanceCustomHealthStatus</code> request before it changes the health status of a service instance.</p> <p>Sending a second or subsequent <code>UpdateInstanceCustomHealthStatus</code> request with the same value before 30 seconds has passed doesn't accelerate the change. Cloud Map still waits <code>30</code> seconds after the first request to make the change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckCustomConfig) -> dict:
    out: dict = {}
    if "failure_threshold" in value:
        out["FailureThreshold"] = value["failure_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HealthCheckCustomConfig:
    out: HealthCheckCustomConfig = {}  # type: ignore[typeddict-item]
    if data.get("FailureThreshold") is not None:
        out["failure_threshold"] = data["FailureThreshold"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HealthCheckCustomConfig) -> dict:
    out: dict = {}
    if "failure_threshold" in value:
        out["FailureThreshold"] = value["failure_threshold"]
    return out


def deserialize_cbor(data: dict) -> HealthCheckCustomConfig:
    out: HealthCheckCustomConfig = {}  # type: ignore[typeddict-item]
    if data.get("FailureThreshold") is not None:
        out["failure_threshold"] = data["FailureThreshold"]
    return out
