"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeregisterCertificateResult``."""

from typing_extensions import TypedDict


class DeregisterCertificateResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterCertificateResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterCertificateResult:
    out: DeregisterCertificateResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterCertificateResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeregisterCertificateResult:
    out: DeregisterCertificateResult = {}  # type: ignore[typeddict-item]
    return out
