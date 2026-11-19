"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyQualifierId``."""

from typing import Literal, TypeAlias, cast

PolicyQualifierId: TypeAlias = Literal["CPS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyQualifierId) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyQualifierId:
    return cast(PolicyQualifierId, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyQualifierId) -> str:
    return value


def deserialize_cbor(data: str) -> PolicyQualifierId:
    return cast(PolicyQualifierId, data)
