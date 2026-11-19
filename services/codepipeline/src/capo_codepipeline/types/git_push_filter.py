"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPushFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.git_branch_filter_criteria
    import capo_codepipeline.types.git_file_path_filter_criteria
    import capo_codepipeline.types.git_tag_filter_criteria


class GitPushFilter(TypedDict, closed=True):
    tags: NotRequired[
        "capo_codepipeline.types.git_tag_filter_criteria.GitTagFilterCriteria"
    ]
    """<p>The field that contains the details for the Git tags trigger configuration.</p>"""
    branches: NotRequired[
        "capo_codepipeline.types.git_branch_filter_criteria.GitBranchFilterCriteria"
    ]
    """<p>The field that specifies to filter on branches for the push trigger configuration.</p>"""
    file_paths: NotRequired[
        "capo_codepipeline.types.git_file_path_filter_criteria.GitFilePathFilterCriteria"
    ]
    """<p>The field that specifies to filter on file paths for the push trigger configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPushFilter) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codepipeline.types.git_tag_filter_criteria

        out["tags"] = (
            capo_codepipeline.types.git_tag_filter_criteria.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "branches" in value:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.serialize_aws_json_1_1(
                value["branches"]
            )
        )
    if "file_paths" in value:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["filePaths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.serialize_aws_json_1_1(
                value["file_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitPushFilter:
    out: GitPushFilter = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codepipeline.types.git_tag_filter_criteria

        out["tags"] = (
            capo_codepipeline.types.git_tag_filter_criteria.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if data.get("branches") is not None:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.deserialize_aws_json_1_1(
                data["branches"]
            )
        )
    if data.get("filePaths") is not None:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["file_paths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.deserialize_aws_json_1_1(
                data["filePaths"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitPushFilter) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codepipeline.types.git_tag_filter_criteria

        out["tags"] = capo_codepipeline.types.git_tag_filter_criteria.serialize_cbor(
            value["tags"]
        )
    if "branches" in value:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.serialize_cbor(
                value["branches"]
            )
        )
    if "file_paths" in value:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["filePaths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.serialize_cbor(
                value["file_paths"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GitPushFilter:
    out: GitPushFilter = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codepipeline.types.git_tag_filter_criteria

        out["tags"] = capo_codepipeline.types.git_tag_filter_criteria.deserialize_cbor(
            data["tags"]
        )
    if data.get("branches") is not None:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.deserialize_cbor(
                data["branches"]
            )
        )
    if data.get("filePaths") is not None:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["file_paths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.deserialize_cbor(
                data["filePaths"]
            )
        )
    return out
