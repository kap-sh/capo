"""Generated from Smithy shape ``com.amazonaws.acmpca#AuditReportResponseFormat``."""

from typing import Literal, TypeAlias, cast

AuditReportResponseFormat: TypeAlias = Literal[
    "JSON",
    "CSV",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditReportResponseFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuditReportResponseFormat:
    return cast(AuditReportResponseFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuditReportResponseFormat) -> str:
    return value


def deserialize_cbor(data: str) -> AuditReportResponseFormat:
    return cast(AuditReportResponseFormat, data)
