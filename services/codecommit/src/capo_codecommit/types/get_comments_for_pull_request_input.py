"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentsForPullRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.max_results
    import capo_codecommit.types.next_token
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.repository_name


class GetCommentsForPullRequestInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The name of the repository that contains the pull request. Requirement is conditional: <code>repositoryName</code> must be specified when <code>beforeCommitId</code> and <code>afterCommitId</code> are included.</p>"""
    before_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created. Requirement is conditional: <code>beforeCommitId</code> must be specified when <code>repositoryName</code> is included.</p>"""
    after_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made. Requirement is conditional: <code>afterCommitId</code> must be specified when <code>repositoryName</code> is included.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentsForPullRequestInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "before_commit_id" in value:
        out["beforeCommitId"] = value["before_commit_id"]
    if "after_commit_id" in value:
        out["afterCommitId"] = value["after_commit_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentsForPullRequestInput:
    out: GetCommentsForPullRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("beforeCommitId") is not None:
        out["before_commit_id"] = data["beforeCommitId"]
    if data.get("afterCommitId") is not None:
        out["after_commit_id"] = data["afterCommitId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
