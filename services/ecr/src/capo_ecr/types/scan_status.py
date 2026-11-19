"""Generated from Smithy shape ``com.amazonaws.ecr#ScanStatus``."""

from typing import Literal, TypeAlias, cast

ScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "UNSUPPORTED_IMAGE",
    "ACTIVE",
    "PENDING",
    "SCAN_ELIGIBILITY_EXPIRED",
    "FINDINGS_UNAVAILABLE",
    "LIMIT_EXCEEDED",
    "IMAGE_ARCHIVED",
    "IMAGE_SIZE_EXCEEDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanStatus:
    return cast(ScanStatus, data)
