"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#StorageLocationType``."""

from typing import Literal, TypeAlias, cast

StorageLocationType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageLocationType:
    return cast(StorageLocationType, data)
