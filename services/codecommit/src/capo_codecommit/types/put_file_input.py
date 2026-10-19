"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.email
    import capo_codecommit.types.file_content
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.message
    import capo_codecommit.types.name
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class PutFileInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to add or update the file.</p>"""
    branch_name: "capo_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch where you want to add or update the file. If this is an empty repository, this branch is created.</p>"""
    file_content: "capo_codecommit.types.file_content.FileContent"
    """<p>The content of the file, in binary object format. </p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The name of the file you want to add or update, including the relative path to the file in the repository.</p> <note> <p>If the path does not currently exist in the repository, the path is created as part of adding the file.</p> </note>"""
    file_mode: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode permissions of the blob. Valid file mode permissions are listed here.</p>"""
    parent_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required. </p> <p>The commit ID must match the ID of the head commit at the time of the operation. Otherwise, an error occurs, and the file is not added or updated.</p>"""
    commit_message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>A message about why this file was added or updated. Although it is optional, a message makes the commit history for your repository more useful.</p>"""
    name: NotRequired["capo_codecommit.types.name.Name"]
    """<p>The name of the person adding or updating the file. Although it is optional, a name makes the commit history for your repository more useful.</p>"""
    email: NotRequired["capo_codecommit.types.email.Email"]
    """<p>An email address for the person adding or updating the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    import capo_codecommit.types.file_content

    out["fileContent"] = capo_codecommit.types.file_content.serialize_aws_json_1_1(
        value["file_content"]
    )
    out["filePath"] = value["file_path"]
    if "file_mode" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    if "parent_commit_id" in value:
        out["parentCommitId"] = value["parent_commit_id"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileInput:
    out: PutFileInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    if data.get("fileContent") is not None:
        import capo_codecommit.types.file_content

        out["file_content"] = (
            capo_codecommit.types.file_content.deserialize_aws_json_1_1(
                data["fileContent"]
            )
        )
    else:
        out["file_content"] = b""
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("fileMode") is not None:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    if data.get("parentCommitId") is not None:
        out["parent_commit_id"] = data["parentCommitId"]
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out
