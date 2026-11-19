"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartAddressListImportJobResponse``."""

from typing_extensions import TypedDict


class StartAddressListImportJobResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAddressListImportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAddressListImportJobResponse:
    out: StartAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartAddressListImportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StartAddressListImportJobResponse:
    out: StartAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    return out
