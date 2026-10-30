"""Generated from Smithy shape ``com.amazonaws.continuum#GitHubTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.delivery_git_commit_sha
    import capo_continuum.types.delivery_git_hub_name
    import capo_continuum.types.delivery_pull_request_number


class GitHubTarget(TypedDict, closed=True):
    owner: "capo_continuum.types.delivery_git_hub_name.DeliveryGitHubName"
    """The GitHub user or organization that owns the repository."""
    repository: "capo_continuum.types.delivery_git_hub_name.DeliveryGitHubName"
    """The repository name."""
    pull_request_number: NotRequired[
        "capo_continuum.types.delivery_pull_request_number.DeliveryPullRequestNumber"
    ]
    """Repository-scoped pull request number assigned by GitHub."""
    head_sha: NotRequired[
        "capo_continuum.types.delivery_git_commit_sha.DeliveryGitCommitSha"
    ]
    """The head commit SHA of the pull request. Absent until the pull request is opened."""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubTarget) -> dict:
    out: dict = {}
    out["owner"] = value["owner"]
    out["repository"] = value["repository"]
    if "pull_request_number" in value:
        out["pullRequestNumber"] = value["pull_request_number"]
    if "head_sha" in value:
        out["headSha"] = value["head_sha"]
    return out


def deserialize_json(data: dict) -> GitHubTarget:
    out: GitHubTarget = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    else:
        out["repository"] = ""
    if data.get("pullRequestNumber") is not None:
        out["pull_request_number"] = data["pullRequestNumber"]
    if data.get("headSha") is not None:
        out["head_sha"] = data["headSha"]
    return out
