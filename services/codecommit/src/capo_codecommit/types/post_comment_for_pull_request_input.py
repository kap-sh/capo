"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForPullRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.content
    import capo_codecommit.types.location
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.repository_name


class PostCommentForPullRequestInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to post a comment on a pull request.</p>"""
    before_commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.</p>"""
    after_commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.</p>"""
    location: NotRequired["capo_codecommit.types.location.Location"]
    """<p>The location of the change where you want to post your comment. If no location is provided, the comment is posted as a general comment on the pull request difference between the before commit ID and the after commit ID.</p>"""
    content: "capo_codecommit.types.content.Content"
    """<p>The content of your comment on the change.</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentForPullRequestInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["repositoryName"] = value["repository_name"]
    out["beforeCommitId"] = value["before_commit_id"]
    out["afterCommitId"] = value["after_commit_id"]
    if "location" in value:
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    out["content"] = value["content"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentForPullRequestInput:
    out: PostCommentForPullRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("beforeCommitId") is not None:
        out["before_commit_id"] = data["beforeCommitId"]
    else:
        out["before_commit_id"] = ""
    if data.get("afterCommitId") is not None:
        out["after_commit_id"] = data["afterCommitId"]
    else:
        out["after_commit_id"] = ""
    if data.get("location") is not None:
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
