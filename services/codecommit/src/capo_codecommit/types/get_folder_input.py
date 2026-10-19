"""Generated from Smithy shape ``com.amazonaws.codecommit#GetFolderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class GetFolderInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository.</p>"""
    commit_specifier: NotRequired["capo_codecommit.types.commit_name.CommitName"]
    """<p>A fully qualified reference used to identify a commit that contains the version of the folder's content to return. A fully qualified reference can be a commit ID, branch name, tag, or reference such as HEAD. If no specifier is provided, the folder content is returned as it exists in the HEAD commit.</p>"""
    folder_path: "capo_codecommit.types.path.Path"
    """<p>The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFolderInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "commit_specifier" in value:
        out["commitSpecifier"] = value["commit_specifier"]
    out["folderPath"] = value["folder_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFolderInput:
    out: GetFolderInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("commitSpecifier") is not None:
        out["commit_specifier"] = data["commitSpecifier"]
    if data.get("folderPath") is not None:
        out["folder_path"] = data["folderPath"]
    else:
        out["folder_path"] = ""
    return out
