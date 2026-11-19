"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitTagFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.git_tag_pattern_list


class GitTagFilterCriteria(TypedDict, closed=True):
    includes: NotRequired[
        "capo_codepipeline.types.git_tag_pattern_list.GitTagPatternList"
    ]
    """<p>The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline.</p>"""
    excludes: NotRequired[
        "capo_codepipeline.types.git_tag_pattern_list.GitTagPatternList"
    ]
    """<p>The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitTagFilterCriteria) -> dict:
    out: dict = {}
    if "includes" in value:
        import capo_codepipeline.types.git_tag_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_tag_pattern_list.serialize_aws_json_1_1(
                value["includes"]
            )
        )
    if "excludes" in value:
        import capo_codepipeline.types.git_tag_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_tag_pattern_list.serialize_aws_json_1_1(
                value["excludes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitTagFilterCriteria:
    out: GitTagFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("includes") is not None:
        import capo_codepipeline.types.git_tag_pattern_list

        out["includes"] = (
            capo_codepipeline.types.git_tag_pattern_list.deserialize_aws_json_1_1(
                data["includes"]
            )
        )
    if data.get("excludes") is not None:
        import capo_codepipeline.types.git_tag_pattern_list

        out["excludes"] = (
            capo_codepipeline.types.git_tag_pattern_list.deserialize_aws_json_1_1(
                data["excludes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitTagFilterCriteria) -> dict:
    out: dict = {}
    if "includes" in value:
        import capo_codepipeline.types.git_tag_pattern_list

        out["includes"] = capo_codepipeline.types.git_tag_pattern_list.serialize_cbor(
            value["includes"]
        )
    if "excludes" in value:
        import capo_codepipeline.types.git_tag_pattern_list

        out["excludes"] = capo_codepipeline.types.git_tag_pattern_list.serialize_cbor(
            value["excludes"]
        )
    return out


def deserialize_cbor(data: dict) -> GitTagFilterCriteria:
    out: GitTagFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("includes") is not None:
        import capo_codepipeline.types.git_tag_pattern_list

        out["includes"] = capo_codepipeline.types.git_tag_pattern_list.deserialize_cbor(
            data["includes"]
        )
    if data.get("excludes") is not None:
        import capo_codepipeline.types.git_tag_pattern_list

        out["excludes"] = capo_codepipeline.types.git_tag_pattern_list.deserialize_cbor(
            data["excludes"]
        )
    return out
