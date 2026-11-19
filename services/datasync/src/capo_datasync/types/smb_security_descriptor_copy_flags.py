"""Generated from Smithy shape ``com.amazonaws.datasync#SmbSecurityDescriptorCopyFlags``."""

from typing import Literal, TypeAlias, cast

SmbSecurityDescriptorCopyFlags: TypeAlias = Literal[
    "NONE",
    "OWNER_DACL",
    "OWNER_DACL_SACL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmbSecurityDescriptorCopyFlags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbSecurityDescriptorCopyFlags:
    return cast(SmbSecurityDescriptorCopyFlags, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SmbSecurityDescriptorCopyFlags) -> str:
    return value


def deserialize_cbor(data: str) -> SmbSecurityDescriptorCopyFlags:
    return cast(SmbSecurityDescriptorCopyFlags, data)
