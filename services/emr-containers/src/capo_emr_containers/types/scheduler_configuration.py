"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SchedulerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.in_queue_job_limit_integer
    import capo_emr_containers.types.job_limit_integer


class SchedulerConfiguration(TypedDict, closed=True):
    max_in_queue_job_runs: NotRequired[
        "capo_emr_containers.types.in_queue_job_limit_integer.InQueueJobLimitInteger"
    ]
    """<p>The maximum number of job runs that can be in the <code>PENDING</code> or <code>SUBMITTED</code> state at any time for the virtual cluster. When the queue is full, the service rejects <code>StartJobRun</code> requests with a <code>ValidationException</code>. If you omit this field, the service applies no queue-depth limit.</p>"""
    max_concurrent_job_runs: NotRequired[
        "capo_emr_containers.types.job_limit_integer.JobLimitInteger"
    ]
    """<p>The maximum number of job runs that can be in the <code>RUNNING</code> state at any time for the virtual cluster. As running slots free up, queued job runs start automatically. If you omit this field, the service applies a default limit of 1,000 concurrent job runs to the virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulerConfiguration) -> dict:
    out: dict = {}
    if "max_in_queue_job_runs" in value:
        out["maxInQueueJobRuns"] = value["max_in_queue_job_runs"]
    if "max_concurrent_job_runs" in value:
        out["maxConcurrentJobRuns"] = value["max_concurrent_job_runs"]
    return out


def deserialize_json(data: dict) -> SchedulerConfiguration:
    out: SchedulerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxInQueueJobRuns") is not None:
        out["max_in_queue_job_runs"] = data["maxInQueueJobRuns"]
    if data.get("maxConcurrentJobRuns") is not None:
        out["max_concurrent_job_runs"] = data["maxConcurrentJobRuns"]
    return out
