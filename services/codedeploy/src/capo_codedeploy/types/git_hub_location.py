"""Generated from Smithy shape ``com.amazonaws.codedeploy#GitHubLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.commit_id
    import capo_codedeploy.types.repository


class GitHubLocation(TypedDict, closed=True):
    repository: NotRequired["capo_codedeploy.types.repository.Repository"]
    """<p>The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. </p> <p>Specified as account/repository.</p>"""
    commit_id: NotRequired["capo_codedeploy.types.commit_id.CommitId"]
    """<p>The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitHubLocation) -> dict:
    out: dict = {}
    if "repository" in value:
        out["repository"] = value["repository"]
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitHubLocation:
    out: GitHubLocation = {}  # type: ignore[typeddict-item]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitHubLocation) -> dict:
    out: dict = {}
    if "repository" in value:
        out["repository"] = value["repository"]
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    return out


def deserialize_cbor(data: dict) -> GitHubLocation:
    out: GitHubLocation = {}  # type: ignore[typeddict-item]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    return out
