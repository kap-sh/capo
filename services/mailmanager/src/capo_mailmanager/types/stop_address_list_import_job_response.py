"""Generated from Smithy shape ``com.amazonaws.mailmanager#StopAddressListImportJobResponse``."""

from typing_extensions import TypedDict


class StopAddressListImportJobResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopAddressListImportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopAddressListImportJobResponse:
    out: StopAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopAddressListImportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopAddressListImportJobResponse:
    out: StopAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    return out
