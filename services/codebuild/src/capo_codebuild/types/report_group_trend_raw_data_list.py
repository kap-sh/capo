"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupTrendRawDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.report_with_raw_data

ReportGroupTrendRawDataList: TypeAlias = list[
    "capo_codebuild.types.report_with_raw_data.ReportWithRawData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupTrendRawDataList) -> list:
    import capo_codebuild.types.report_with_raw_data

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.report_with_raw_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReportGroupTrendRawDataList:
    import capo_codebuild.types.report_with_raw_data

    out: ReportGroupTrendRawDataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.report_with_raw_data.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupTrendRawDataList) -> list:
    import capo_codebuild.types.report_with_raw_data

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.report_with_raw_data.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ReportGroupTrendRawDataList:
    import capo_codebuild.types.report_with_raw_data

    out: ReportGroupTrendRawDataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.report_with_raw_data.deserialize_cbor(item))
    return out
