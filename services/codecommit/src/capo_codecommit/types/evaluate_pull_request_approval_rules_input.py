"""Generated from Smithy shape ``com.amazonaws.codecommit#EvaluatePullRequestApprovalRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.revision_id


class EvaluatePullRequestApprovalRulesInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request you want to evaluate.</p>"""
    revision_id: "capo_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID for the pull request revision. To retrieve the most recent revision ID for a pull request, use <a>GetPullRequest</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatePullRequestApprovalRulesInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatePullRequestApprovalRulesInput:
    out: EvaluatePullRequestApprovalRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
