"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.job_status


class CodeReviewJobSummary(TypedDict, closed=True):
    code_review_job_id: "str"
    """<p>The unique identifier of the code review job.</p>"""
    code_review_id: "str"
    """<p>The unique identifier of the code review associated with the job.</p>"""
    title: NotRequired["str"]
    """<p>The title of the code review job.</p>"""
    status: NotRequired["capo_securityagent.types.job_status.JobStatus"]
    """<p>The current status of the code review job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review job was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobSummary) -> dict:
    out: dict = {}
    out["codeReviewJobId"] = value["code_review_job_id"]
    out["codeReviewId"] = value["code_review_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "status" in value:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CodeReviewJobSummary:
    out: CodeReviewJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("codeReviewJobId") is not None:
        out["code_review_job_id"] = data["codeReviewJobId"]
    else:
        out["code_review_job_id"] = ""
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    else:
        out["code_review_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("status") is not None:
        import capo_securityagent.types.job_status

        out["status"] = capo_securityagent.types.job_status.deserialize_json(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
