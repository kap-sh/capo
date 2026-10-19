"""Generated from Smithy shape ``com.amazonaws.codecommit#ListPullRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.arn
    import capo_codecommit.types.max_results
    import capo_codecommit.types.next_token
    import capo_codecommit.types.pull_request_status_enum
    import capo_codecommit.types.repository_name


class ListPullRequestsInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository for which you want to list pull requests.</p>"""
    author_arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.</p>"""
    pull_request_status: NotRequired[
        "capo_codecommit.types.pull_request_status_enum.PullRequestStatusEnum"
    ]
    """<p>Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPullRequestsInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "author_arn" in value:
        out["authorArn"] = value["author_arn"]
    if "pull_request_status" in value:
        import capo_codecommit.types.pull_request_status_enum

        out["pullRequestStatus"] = (
            capo_codecommit.types.pull_request_status_enum.serialize_aws_json_1_1(
                value["pull_request_status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPullRequestsInput:
    out: ListPullRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("authorArn") is not None:
        out["author_arn"] = data["authorArn"]
    if data.get("pullRequestStatus") is not None:
        import capo_codecommit.types.pull_request_status_enum

        out["pull_request_status"] = (
            capo_codecommit.types.pull_request_status_enum.deserialize_aws_json_1_1(
                data["pullRequestStatus"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
