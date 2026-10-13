"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.job

JobList: TypeAlias = list["capo_codepipeline.types.job.Job"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobList) -> list:
    import capo_codepipeline.types.job

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.job.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobList:
    import capo_codepipeline.types.job

    out: JobList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.job.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: JobList) -> list[Any]:
    import capo_codepipeline.types.job

    return [capo_codepipeline.types.job.redact_sensitive(item) for item in value]
