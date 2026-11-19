"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateBodyBlob``."""

import base64
from typing import TypeAlias

CertificateBodyBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBodyBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CertificateBodyBlob:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateBodyBlob) -> CertificateBodyBlob:
    return value


def deserialize_cbor(data: CertificateBodyBlob) -> CertificateBodyBlob:
    return data
