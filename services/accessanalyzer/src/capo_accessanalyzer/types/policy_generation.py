"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PolicyGeneration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.job_id
    import capo_accessanalyzer.types.job_status
    import capo_accessanalyzer.types.principal_arn
    import capo_accessanalyzer.types.timestamp


class PolicyGeneration(TypedDict, closed=True):
    job_id: "capo_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""
    principal_arn: "capo_accessanalyzer.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy.</p>"""
    status: "capo_accessanalyzer.types.job_status.JobStatus"
    """<p>The status of the policy generation request.</p>"""
    started_on: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>A timestamp of when the policy generation started.</p>"""
    completed_on: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>A timestamp of when the policy generation was completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGeneration) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["principalArn"] = value["principal_arn"]
    out["status"] = value["status"]
    import capo_accessanalyzer.types.timestamp

    out["startedOn"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["started_on"]
    )
    if "completed_on" in value:
        import capo_accessanalyzer.types.timestamp

        out["completedOn"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["completed_on"]
        )
    return out


def deserialize_json(data: dict) -> PolicyGeneration:
    out: PolicyGeneration = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("startedOn") is not None:
        import capo_accessanalyzer.types.timestamp

        out["started_on"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["startedOn"]
        )
    else:
        import datetime

        out["started_on"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedOn") is not None:
        import capo_accessanalyzer.types.timestamp

        out["completed_on"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["completedOn"]
        )
    return out
