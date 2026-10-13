"""Generated from Smithy shape ``com.amazonaws.codepipeline#Job``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.account_id
    import capo_codepipeline.types.job_data
    import capo_codepipeline.types.job_id
    import capo_codepipeline.types.nonce


class Job(TypedDict, closed=True):
    id: NotRequired["capo_codepipeline.types.job_id.JobId"]
    """<p>The unique system-generated ID of the job.</p>"""
    data: NotRequired["capo_codepipeline.types.job_data.JobData"]
    """<p>Other data about a job.</p>"""
    nonce: NotRequired["capo_codepipeline.types.nonce.Nonce"]
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an <a>AcknowledgeJob</a> request.</p>"""
    account_id: NotRequired["capo_codepipeline.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account to use when performing the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Job) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data" in value:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.serialize_aws_json_1_1(
            value["data"]
        )
    if "nonce" in value:
        out["nonce"] = value["nonce"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("data") is not None:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.deserialize_aws_json_1_1(
            data["data"]
        )
    if data.get("nonce") is not None:
        out["nonce"] = data["nonce"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out


def redact_sensitive(value: Job) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.redact_sensitive(value["data"])
    return out
