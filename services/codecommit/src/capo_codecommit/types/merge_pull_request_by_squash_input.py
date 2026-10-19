"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestBySquashInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.conflict_detail_level_type_enum
    import capo_codecommit.types.conflict_resolution
    import capo_codecommit.types.conflict_resolution_strategy_type_enum
    import capo_codecommit.types.email
    import capo_codecommit.types.keep_empty_folders
    import capo_codecommit.types.message
    import capo_codecommit.types.name
    import capo_codecommit.types.object_id
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.repository_name


class MergePullRequestBySquashInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where the pull request was created.</p>"""
    source_commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.</p>"""
    conflict_detail_level: NotRequired[
        "capo_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "capo_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    commit_message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>The commit message to include in the commit information for the merge.</p>"""
    author_name: NotRequired["capo_codecommit.types.name.Name"]
    """<p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>"""
    email: NotRequired["capo_codecommit.types.email.Email"]
    """<p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>"""
    keep_empty_folders: NotRequired[
        "capo_codecommit.types.keep_empty_folders.KeepEmptyFolders"
    ]
    """<p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.</p>"""
    conflict_resolution: NotRequired[
        "capo_codecommit.types.conflict_resolution.ConflictResolution"
    ]
    """<p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergePullRequestBySquashInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["repositoryName"] = value["repository_name"]
    if "source_commit_id" in value:
        out["sourceCommitId"] = value["source_commit_id"]
    if "conflict_detail_level" in value:
        import capo_codecommit.types.conflict_detail_level_type_enum

        out["conflictDetailLevel"] = (
            capo_codecommit.types.conflict_detail_level_type_enum.serialize_aws_json_1_1(
                value["conflict_detail_level"]
            )
        )
    if "conflict_resolution_strategy" in value:
        import capo_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflictResolutionStrategy"] = (
            capo_codecommit.types.conflict_resolution_strategy_type_enum.serialize_aws_json_1_1(
                value["conflict_resolution_strategy"]
            )
        )
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "email" in value:
        out["email"] = value["email"]
    if "keep_empty_folders" in value:
        out["keepEmptyFolders"] = value["keep_empty_folders"]
    if "conflict_resolution" in value:
        import capo_codecommit.types.conflict_resolution

        out["conflictResolution"] = (
            capo_codecommit.types.conflict_resolution.serialize_aws_json_1_1(
                value["conflict_resolution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergePullRequestBySquashInput:
    out: MergePullRequestBySquashInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("sourceCommitId") is not None:
        out["source_commit_id"] = data["sourceCommitId"]
    if data.get("conflictDetailLevel") is not None:
        import capo_codecommit.types.conflict_detail_level_type_enum

        out["conflict_detail_level"] = (
            capo_codecommit.types.conflict_detail_level_type_enum.deserialize_aws_json_1_1(
                data["conflictDetailLevel"]
            )
        )
    if data.get("conflictResolutionStrategy") is not None:
        import capo_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflict_resolution_strategy"] = (
            capo_codecommit.types.conflict_resolution_strategy_type_enum.deserialize_aws_json_1_1(
                data["conflictResolutionStrategy"]
            )
        )
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    if data.get("authorName") is not None:
        out["author_name"] = data["authorName"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("keepEmptyFolders") is not None:
        out["keep_empty_folders"] = data["keepEmptyFolders"]
    if data.get("conflictResolution") is not None:
        import capo_codecommit.types.conflict_resolution

        out["conflict_resolution"] = (
            capo_codecommit.types.conflict_resolution.deserialize_aws_json_1_1(
                data["conflictResolution"]
            )
        )
    return out
