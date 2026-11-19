"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupRetentionType``."""

from typing import Literal, TypeAlias, cast

BackupRetentionType: TypeAlias = Literal["DAYS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupRetentionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupRetentionType:
    return cast(BackupRetentionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BackupRetentionType) -> str:
    return value


def deserialize_cbor(data: str) -> BackupRetentionType:
    return cast(BackupRetentionType, data)
