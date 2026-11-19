"""Generated from Smithy shape ``com.amazonaws.acmpca#AuditReportStatus``."""

from typing import Literal, TypeAlias, cast

AuditReportStatus: TypeAlias = Literal[
    "CREATING",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuditReportStatus:
    return cast(AuditReportStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuditReportStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AuditReportStatus:
    return cast(AuditReportStatus, data)
