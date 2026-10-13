"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobTemplates``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.job_template

JobTemplates: TypeAlias = list["capo_emr_containers.types.job_template.JobTemplate"]


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplates) -> list:
    import capo_emr_containers.types.job_template

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.job_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobTemplates:
    import capo_emr_containers.types.job_template

    out: JobTemplates = []
    for item in data:
        if item is None:
            continue
        out.append(capo_emr_containers.types.job_template.deserialize_json(item))
    return out


def redact_sensitive(value: JobTemplates) -> list[Any]:
    import capo_emr_containers.types.job_template

    return [
        capo_emr_containers.types.job_template.redact_sensitive(item) for item in value
    ]
