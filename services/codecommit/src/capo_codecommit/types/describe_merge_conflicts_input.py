"""Generated from Smithy shape ``com.amazonaws.codecommit#DescribeMergeConflictsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.conflict_detail_level_type_enum
    import capo_codecommit.types.conflict_resolution_strategy_type_enum
    import capo_codecommit.types.max_results
    import capo_codecommit.types.merge_option_type_enum
    import capo_codecommit.types.next_token
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class DescribeMergeConflictsInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to get information about a merge conflict.</p>"""
    destination_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    source_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    merge_option: "capo_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
    """<p>The merge option or strategy you want to use to merge the code.</p>"""
    max_merge_hunks: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>The maximum number of merge hunks to include in the output.</p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The path of the target files used to describe the conflicts. </p>"""
    conflict_detail_level: NotRequired[
        "capo_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "capo_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMergeConflictsInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    import capo_codecommit.types.merge_option_type_enum

    out["mergeOption"] = (
        capo_codecommit.types.merge_option_type_enum.serialize_aws_json_1_1(
            value["merge_option"]
        )
    )
    if "max_merge_hunks" in value:
        out["maxMergeHunks"] = value["max_merge_hunks"]
    out["filePath"] = value["file_path"]
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
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMergeConflictsInput:
    out: DescribeMergeConflictsInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("destinationCommitSpecifier") is not None:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        out["destination_commit_specifier"] = ""
    if data.get("sourceCommitSpecifier") is not None:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        out["source_commit_specifier"] = ""
    if data.get("mergeOption") is not None:
        import capo_codecommit.types.merge_option_type_enum

        out["merge_option"] = (
            capo_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(
                data["mergeOption"]
            )
        )
    else:
        import typing

        out["merge_option"] = typing.cast(
            "capo_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum", ""
        )
    if data.get("maxMergeHunks") is not None:
        out["max_merge_hunks"] = data["maxMergeHunks"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
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
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
