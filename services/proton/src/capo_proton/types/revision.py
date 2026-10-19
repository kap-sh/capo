"""Generated from Smithy shape ``com.amazonaws.proton#Revision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.sha


class Revision(TypedDict, closed=True):
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    sha: "capo_proton.types.sha.SHA"
    """<p>The secure hash algorithm (SHA) hash for the revision.</p>"""
    directory: "str"
    """<p>The repository directory changed by a commit and push that activated the sync attempt.</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Revision) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["sha"] = value["sha"]
    out["directory"] = value["directory"]
    out["branch"] = value["branch"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Revision:
    out: Revision = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("repositoryProvider") is not None:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        out["repository_provider"] = ""
    if data.get("sha") is not None:
        out["sha"] = data["sha"]
    else:
        out["sha"] = ""
    if data.get("directory") is not None:
        out["directory"] = data["directory"]
    else:
        out["directory"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        out["branch"] = ""
    return out
