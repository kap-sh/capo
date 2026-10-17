"""Generated from Smithy shape ``com.amazonaws.datasync#NfsVersion``."""

from typing import Literal, TypeAlias, cast

NfsVersion: TypeAlias = Literal[
    "AUTOMATIC",
    "NFS3",
    "NFS4_0",
    "NFS4_1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NfsVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NfsVersion:
    return cast(NfsVersion, data)
