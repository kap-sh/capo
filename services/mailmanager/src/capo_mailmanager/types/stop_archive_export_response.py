"""Generated from Smithy shape ``com.amazonaws.mailmanager#StopArchiveExportResponse``."""

from typing_extensions import TypedDict


class StopArchiveExportResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopArchiveExportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopArchiveExportResponse:
    out: StopArchiveExportResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopArchiveExportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopArchiveExportResponse:
    out: StopArchiveExportResponse = {}  # type: ignore[typeddict-item]
    return out
