"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.account_id
    import capo_codepipeline.types.job_data
    import capo_codepipeline.types.job_id


class JobDetails(TypedDict, closed=True):
    id: NotRequired["capo_codepipeline.types.job_id.JobId"]
    """<p>The unique system-generated ID of the job.</p>"""
    data: NotRequired["capo_codepipeline.types.job_data.JobData"]
    """<p>Represents other information about a job required for a job worker to complete the job. </p>"""
    account_id: NotRequired["capo_codepipeline.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data" in value:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.serialize_aws_json_1_1(
            value["data"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("data") is not None:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.deserialize_aws_json_1_1(
            data["data"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out


def redact_sensitive(value: JobDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.redact_sensitive(value["data"])
    return out
