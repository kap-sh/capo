"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeCoverages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.code_coverage

CodeCoverages: TypeAlias = list["capo_codebuild.types.code_coverage.CodeCoverage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeCoverages) -> list:
    import capo_codebuild.types.code_coverage

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.code_coverage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CodeCoverages:
    import capo_codebuild.types.code_coverage

    out: CodeCoverages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.code_coverage.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CodeCoverages) -> list:
    import capo_codebuild.types.code_coverage

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.code_coverage.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> CodeCoverages:
    import capo_codebuild.types.code_coverage

    out: CodeCoverages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.code_coverage.deserialize_cbor(item))
    return out
