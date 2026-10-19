"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentsForComparedCommitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.max_results
    import capo_codecommit.types.next_token
    import capo_codecommit.types.repository_name


class GetCommentsForComparedCommitInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to compare commits.</p>"""
    before_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>To establish the directionality of the comparison, the full commit ID of the before commit.</p>"""
    after_commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>To establish the directionality of the comparison, the full commit ID of the after commit.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that when provided in a request, returns the next batch of the results. </p>"""
    max_results: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments, but you can configure up to 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentsForComparedCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "before_commit_id" in value:
        out["beforeCommitId"] = value["before_commit_id"]
    out["afterCommitId"] = value["after_commit_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentsForComparedCommitInput:
    out: GetCommentsForComparedCommitInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("beforeCommitId") is not None:
        out["before_commit_id"] = data["beforeCommitId"]
    if data.get("afterCommitId") is not None:
        out["after_commit_id"] = data["afterCommitId"]
    else:
        out["after_commit_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
