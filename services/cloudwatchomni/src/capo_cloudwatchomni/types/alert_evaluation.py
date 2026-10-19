"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertEvaluation``."""

from typing_extensions import NotRequired, TypedDict


class AlertEvaluation(TypedDict, closed=True):
    interval_seconds: "int"
    """The interval between evaluations, in seconds."""
    pending_duration_seconds: NotRequired["int"]
    """The duration a breach must persist before the alert fires, in seconds."""
    recovery_duration_seconds: NotRequired["int"]
    """The duration a recovery must persist before the alert clears, in seconds."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertEvaluation) -> dict:
    out: dict = {}
    out["intervalSeconds"] = value["interval_seconds"]
    if "pending_duration_seconds" in value:
        out["pendingDurationSeconds"] = value["pending_duration_seconds"]
    if "recovery_duration_seconds" in value:
        out["recoveryDurationSeconds"] = value["recovery_duration_seconds"]
    return out


def deserialize_cbor(data: dict) -> AlertEvaluation:
    out: AlertEvaluation = {}  # type: ignore[typeddict-item]
    if data.get("intervalSeconds") is not None:
        out["interval_seconds"] = data["intervalSeconds"]
    else:
        out["interval_seconds"] = 0
    if data.get("pendingDurationSeconds") is not None:
        out["pending_duration_seconds"] = data["pendingDurationSeconds"]
    if data.get("recoveryDurationSeconds") is not None:
        out["recovery_duration_seconds"] = data["recoveryDurationSeconds"]
    return out
