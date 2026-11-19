"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateChainBlob``."""

import base64
from typing import TypeAlias

CertificateChainBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateChainBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CertificateChainBlob:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateChainBlob) -> CertificateChainBlob:
    return value


def deserialize_cbor(data: CertificateChainBlob) -> CertificateChainBlob:
    return data
