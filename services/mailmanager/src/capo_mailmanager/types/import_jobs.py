"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJobs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.import_job

ImportJobs: TypeAlias = list["capo_mailmanager.types.import_job.ImportJob"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJobs) -> list:
    import capo_mailmanager.types.import_job

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.import_job.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ImportJobs:
    import capo_mailmanager.types.import_job

    out: ImportJobs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.import_job.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: ImportJobs) -> list[Any]:
    import capo_mailmanager.types.import_job

    return [capo_mailmanager.types.import_job.redact_sensitive(item) for item in value]
