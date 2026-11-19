"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitFilePathPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_file_path_pattern

GitFilePathPatternList: TypeAlias = list[
    "capo_codepipeline.types.git_file_path_pattern.GitFilePathPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitFilePathPatternList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GitFilePathPatternList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitFilePathPatternList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> GitFilePathPatternList:
    return [item for item in data if item is not None]
