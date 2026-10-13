"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetJobDetailsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.job_details


class GetJobDetailsOutput(TypedDict, closed=True):
    job_details: NotRequired["capo_codepipeline.types.job_details.JobDetails"]
    """<p>The details of the job.</p> <note> <p>If AWSSessionCredentials is used, a long-running job can call <code>GetJobDetails</code> again to obtain new credentials.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobDetailsOutput) -> dict:
    out: dict = {}
    if "job_details" in value:
        import capo_codepipeline.types.job_details

        out["jobDetails"] = capo_codepipeline.types.job_details.serialize_aws_json_1_1(
            value["job_details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobDetailsOutput:
    out: GetJobDetailsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobDetails") is not None:
        import capo_codepipeline.types.job_details

        out["job_details"] = (
            capo_codepipeline.types.job_details.deserialize_aws_json_1_1(
                data["jobDetails"]
            )
        )
    return out


def redact_sensitive(value: GetJobDetailsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_details" in value:
        import capo_codepipeline.types.job_details

        out["job_details"] = capo_codepipeline.types.job_details.redact_sensitive(
            value["job_details"]
        )
    return out
