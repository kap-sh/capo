"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitFilePathFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.git_file_path_pattern_list


class GitFilePathFilterCriteria(TypedDict, closed=True):
    includes: NotRequired[
        "capo_codepipeline.types.git_file_path_pattern_list.GitFilePathPatternList"
    ]
    """<p>The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.</p>"""
    excludes: NotRequired[
        "capo_codepipeline.types.git_file_path_pattern_list.GitFilePathPatternList"
    ]
    """<p>The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitFilePathFilterCriteria) -> dict:
    out: dict = {}
    if "includes" in value:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.serialize_aws_json_1_1(
                value["includes"]
            )
        )
    if "excludes" in value:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.serialize_aws_json_1_1(
                value["excludes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitFilePathFilterCriteria:
    out: GitFilePathFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("includes") is not None:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.deserialize_aws_json_1_1(
                data["includes"]
            )
        )
    if data.get("excludes") is not None:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.deserialize_aws_json_1_1(
                data["excludes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitFilePathFilterCriteria) -> dict:
    out: dict = {}
    if "includes" in value:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.serialize_cbor(
                value["includes"]
            )
        )
    if "excludes" in value:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.serialize_cbor(
                value["excludes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GitFilePathFilterCriteria:
    out: GitFilePathFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("includes") is not None:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.deserialize_cbor(
                data["includes"]
            )
        )
    if data.get("excludes") is not None:
        import capo_codepipeline.types.git_file_path_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_file_path_pattern_list.deserialize_cbor(
                data["excludes"]
            )
        )
    return out
