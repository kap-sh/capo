"""Generated from Smithy shape ``com.amazonaws.pi#DeletePerformanceAnalysisReportResponse``."""

from typing_extensions import TypedDict


class DeletePerformanceAnalysisReportResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePerformanceAnalysisReportResponse:
    out: DeletePerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletePerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeletePerformanceAnalysisReportResponse:
    out: DeletePerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    return out
