"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.report_group

ReportGroups: TypeAlias = list["capo_codebuild.types.report_group.ReportGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroups) -> list:
    import capo_codebuild.types.report_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.report_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReportGroups:
    import capo_codebuild.types.report_group

    out: ReportGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.report_group.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroups) -> list:
    import capo_codebuild.types.report_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.report_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ReportGroups:
    import capo_codebuild.types.report_group

    out: ReportGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.report_group.deserialize_cbor(item))
    return out
