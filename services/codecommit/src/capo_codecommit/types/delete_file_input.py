"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteFileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.email
    import capo_codecommit.types.keep_empty_folders
    import capo_codecommit.types.message
    import capo_codecommit.types.name
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class DeleteFileInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the file to delete.</p>"""
    branch_name: "capo_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch where the commit that deletes the file is made.</p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The fully qualified path to the file that to be deleted, including the full name and extension of that file. For example, /examples/file.md is a fully qualified path to a file named file.md in a folder named examples.</p>"""
    parent_commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>The ID of the commit that is the tip of the branch where you want to create the commit that deletes the file. This must be the HEAD commit for the branch. The commit that deletes the file is created from this commit ID.</p>"""
    keep_empty_folders: NotRequired[
        "capo_codecommit.types.keep_empty_folders.KeepEmptyFolders"
    ]
    """<p>If a file is the only object in the folder or directory, specifies whether to delete the folder or directory that contains the file. By default, empty folders are deleted. This includes empty folders that are part of the directory structure. For example, if the path to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in dir4 also deletes the empty folders dir4, dir3, and dir2.</p>"""
    commit_message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>The commit message you want to include as part of deleting the file. Commit messages are limited to 256 KB. If no message is specified, a default message is used.</p>"""
    name: NotRequired["capo_codecommit.types.name.Name"]
    """<p>The name of the author of the commit that deletes the file. If no name is specified, the user's ARN is used as the author name and committer name.</p>"""
    email: NotRequired["capo_codecommit.types.email.Email"]
    """<p>The email address for the commit that deletes the file. If no email address is specified, the email address is left blank.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    out["filePath"] = value["file_path"]
    out["parentCommitId"] = value["parent_commit_id"]
    if "keep_empty_folders" in value:
        out["keepEmptyFolders"] = value["keep_empty_folders"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileInput:
    out: DeleteFileInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("DeleteFileInput.repository_name required")
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("DeleteFileInput.branch_name required")
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("DeleteFileInput.file_path required")
    if data.get("parentCommitId") is not None:
        out["parent_commit_id"] = data["parentCommitId"]
    else:
        raise DeserializationError("DeleteFileInput.parent_commit_id required")
    if data.get("keepEmptyFolders") is not None:
        out["keep_empty_folders"] = data["keepEmptyFolders"]
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out
