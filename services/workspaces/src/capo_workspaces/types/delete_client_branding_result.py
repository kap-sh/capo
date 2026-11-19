"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteClientBrandingResult``."""

from typing_extensions import TypedDict


class DeleteClientBrandingResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClientBrandingResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClientBrandingResult:
    out: DeleteClientBrandingResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteClientBrandingResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteClientBrandingResult:
    out: DeleteClientBrandingResult = {}  # type: ignore[typeddict-item]
    return out
