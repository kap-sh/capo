"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeBranchesBySquashInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.conflict_detail_level_type_enum
    import capo_codecommit.types.conflict_resolution
    import capo_codecommit.types.conflict_resolution_strategy_type_enum
    import capo_codecommit.types.email
    import capo_codecommit.types.keep_empty_folders
    import capo_codecommit.types.message
    import capo_codecommit.types.name
    import capo_codecommit.types.repository_name


class MergeBranchesBySquashInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to merge two branches.</p>"""
    source_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    destination_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    target_branch: NotRequired["capo_codecommit.types.branch_name.BranchName"]
    """<p>The branch where the merge is applied. </p>"""
    conflict_detail_level: NotRequired[
        "capo_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "capo_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    author_name: NotRequired["capo_codecommit.types.name.Name"]
    """<p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>"""
    email: NotRequired["capo_codecommit.types.email.Email"]
    """<p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>"""
    commit_message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>The commit message for the merge.</p>"""
    keep_empty_folders: NotRequired[
        "capo_codecommit.types.keep_empty_folders.KeepEmptyFolders"
    ]
    """<p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.</p>"""
    conflict_resolution: NotRequired[
        "capo_codecommit.types.conflict_resolution.ConflictResolution"
    ]
    """<p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeBranchesBySquashInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
    if "target_branch" in value:
        out["targetBranch"] = value["target_branch"]
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
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "email" in value:
        out["email"] = value["email"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
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


def deserialize_aws_json_1_1(data: dict) -> MergeBranchesBySquashInput:
    out: MergeBranchesBySquashInput = {}  # type: ignore[typeddict-item]
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
    if data.get("authorName") is not None:
        out["author_name"] = data["authorName"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
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
