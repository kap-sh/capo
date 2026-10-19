"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.conflict_detail_level_type_enum
    import capo_codecommit.types.conflict_resolution_strategy_type_enum
    import capo_codecommit.types.repository_name


class GetMergeOptionsInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the commits about which you want to get merge options.</p>"""
    source_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    destination_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    conflict_detail_level: NotRequired[
        "capo_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "capo_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeOptionsInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeOptionsInput:
    out: GetMergeOptionsInput = {}  # type: ignore[typeddict-item]
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
    return out
