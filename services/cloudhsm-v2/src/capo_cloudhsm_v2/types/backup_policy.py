"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupPolicy``."""

from typing import Literal, TypeAlias, cast

BackupPolicy: TypeAlias = Literal["DEFAULT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupPolicy:
    return cast(BackupPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BackupPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> BackupPolicy:
    return cast(BackupPolicy, data)
