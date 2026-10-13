"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRuns``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.job_run

JobRuns: TypeAlias = list["capo_emr_containers.types.job_run.JobRun"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRuns) -> list:
    import capo_emr_containers.types.job_run

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.job_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRuns:
    import capo_emr_containers.types.job_run

    out: JobRuns = []
    for item in data:
        if item is None:
            continue
        out.append(capo_emr_containers.types.job_run.deserialize_json(item))
    return out


def redact_sensitive(value: JobRuns) -> list[Any]:
    import capo_emr_containers.types.job_run

    return [capo_emr_containers.types.job_run.redact_sensitive(item) for item in value]
