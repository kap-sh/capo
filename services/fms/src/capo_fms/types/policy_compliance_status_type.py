"""Generated from Smithy shape ``com.amazonaws.fms#PolicyComplianceStatusType``."""

from typing import Literal, TypeAlias, cast

PolicyComplianceStatusType: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyComplianceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyComplianceStatusType:
    return cast(PolicyComplianceStatusType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyComplianceStatusType) -> str:
    return value


def deserialize_cbor(data: str) -> PolicyComplianceStatusType:
    return cast(PolicyComplianceStatusType, data)
