"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunAttemptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.job_run_attempts
    import capo_emr_serverless.types.next_token


class ListJobRunAttemptsResponse(TypedDict, closed=True):
    job_run_attempts: "capo_emr_serverless.types.job_run_attempts.JobRunAttempts"
    """<p>The array of the listed job run attempt objects.</p>"""
    next_token: NotRequired["capo_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunAttemptsResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.job_run_attempts

    out["jobRunAttempts"] = capo_emr_serverless.types.job_run_attempts.serialize_json(
        value["job_run_attempts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunAttemptsResponse:
    out: ListJobRunAttemptsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobRunAttempts") is not None:
        import capo_emr_serverless.types.job_run_attempts

        out["job_run_attempts"] = (
            capo_emr_serverless.types.job_run_attempts.deserialize_json(
                data["jobRunAttempts"]
            )
        )
    else:
        out["job_run_attempts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
