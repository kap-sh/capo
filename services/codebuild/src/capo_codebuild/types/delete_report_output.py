"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteReportOutput``."""

from typing_extensions import TypedDict


class DeleteReportOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportOutput:
    out: DeleteReportOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteReportOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteReportOutput:
    out: DeleteReportOutput = {}  # type: ignore[typeddict-item]
    return out
