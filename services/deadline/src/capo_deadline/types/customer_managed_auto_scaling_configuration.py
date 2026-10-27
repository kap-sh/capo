"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedAutoScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.min_one_max_integer
    import capo_deadline.types.min_zero_max_integer


class CustomerManagedAutoScalingConfiguration(TypedDict, closed=True):
    standby_worker_count: NotRequired[
        "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    ]
    """The number of idle workers maintained and ready to process incoming tasks. The default is 0."""
    worker_idle_duration_seconds: (
        "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    )
    """The number of seconds that a worker can remain idle before it is shut down. The default is 300 seconds (5 minutes)."""
    scale_out_workers_per_minute: NotRequired[
        "capo_deadline.types.min_one_max_integer.MinOneMaxInteger"
    ]
    """The number of workers that can be added per minute to the fleet. The default is 10 workers per minute."""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedAutoScalingConfiguration) -> dict:
    out: dict = {}
    if "standby_worker_count" in value:
        out["standbyWorkerCount"] = value["standby_worker_count"]
    out["workerIdleDurationSeconds"] = value.get("worker_idle_duration_seconds", 300)
    if "scale_out_workers_per_minute" in value:
        out["scaleOutWorkersPerMinute"] = value["scale_out_workers_per_minute"]
    return out


def deserialize_json(data: dict) -> CustomerManagedAutoScalingConfiguration:
    out: CustomerManagedAutoScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("standbyWorkerCount") is not None:
        out["standby_worker_count"] = data["standbyWorkerCount"]
    if data.get("workerIdleDurationSeconds") is not None:
        out["worker_idle_duration_seconds"] = data["workerIdleDurationSeconds"]
    else:
        out["worker_idle_duration_seconds"] = 300
    if data.get("scaleOutWorkersPerMinute") is not None:
        out["scale_out_workers_per_minute"] = data["scaleOutWorkersPerMinute"]
    return out
