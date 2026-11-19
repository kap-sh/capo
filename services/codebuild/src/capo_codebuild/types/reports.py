"""Generated from Smithy shape ``com.amazonaws.codebuild#Reports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.report

Reports: TypeAlias = list["capo_codebuild.types.report.Report"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Reports) -> list:
    import capo_codebuild.types.report

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.report.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Reports:
    import capo_codebuild.types.report

    out: Reports = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.report.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Reports) -> list:
    import capo_codebuild.types.report

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.report.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Reports:
    import capo_codebuild.types.report

    out: Reports = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.report.deserialize_cbor(item))
    return out
