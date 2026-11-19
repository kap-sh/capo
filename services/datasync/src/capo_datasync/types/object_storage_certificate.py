"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageCertificate``."""

import base64
from typing import TypeAlias

ObjectStorageCertificate: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectStorageCertificate) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ObjectStorageCertificate:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ObjectStorageCertificate) -> ObjectStorageCertificate:
    return value


def deserialize_cbor(data: ObjectStorageCertificate) -> ObjectStorageCertificate:
    return data
