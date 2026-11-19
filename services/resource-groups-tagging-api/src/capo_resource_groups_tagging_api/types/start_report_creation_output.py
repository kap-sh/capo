"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#StartReportCreationOutput``."""

from typing_extensions import TypedDict


class StartReportCreationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReportCreationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReportCreationOutput:
    out: StartReportCreationOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartReportCreationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StartReportCreationOutput:
    out: StartReportCreationOutput = {}  # type: ignore[typeddict-item]
    return out
