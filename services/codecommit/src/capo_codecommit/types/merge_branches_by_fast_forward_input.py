"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeBranchesByFastForwardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.repository_name


class MergeBranchesByFastForwardInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to merge two branches.</p>"""
    source_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    destination_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    target_branch: NotRequired["capo_codecommit.types.branch_name.BranchName"]
    """<p>The branch where the merge is applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeBranchesByFastForwardInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
    if "target_branch" in value:
        out["targetBranch"] = value["target_branch"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeBranchesByFastForwardInput:
    out: MergeBranchesByFastForwardInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("sourceCommitSpecifier") is not None:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        out["source_commit_specifier"] = ""
    if data.get("destinationCommitSpecifier") is not None:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        out["destination_commit_specifier"] = ""
    if data.get("targetBranch") is not None:
        out["target_branch"] = data["targetBranch"]
    return out
