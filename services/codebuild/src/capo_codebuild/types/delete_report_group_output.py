"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteReportGroupOutput``."""

from typing_extensions import TypedDict


class DeleteReportGroupOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportGroupOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportGroupOutput:
    out: DeleteReportGroupOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteReportGroupOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteReportGroupOutput:
    out: DeleteReportGroupOutput = {}  # type: ignore[typeddict-item]
    return out
