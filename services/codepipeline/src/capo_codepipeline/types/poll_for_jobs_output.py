"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollForJobsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.job_list


class PollForJobsOutput(TypedDict, closed=True):
    jobs: NotRequired["capo_codepipeline.types.job_list.JobList"]
    """<p>Information about the jobs to take action on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForJobsOutput) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_codepipeline.types.job_list

        out["jobs"] = capo_codepipeline.types.job_list.serialize_aws_json_1_1(
            value["jobs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForJobsOutput:
    out: PollForJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_codepipeline.types.job_list

        out["jobs"] = capo_codepipeline.types.job_list.deserialize_aws_json_1_1(
            data["jobs"]
        )
    return out


def redact_sensitive(value: PollForJobsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_codepipeline.types.job_list

        out["jobs"] = capo_codepipeline.types.job_list.redact_sensitive(value["jobs"])
    return out
