"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EnabledAnalysisType``."""

from typing import Literal, TypeAlias, cast

EnabledAnalysisType: TypeAlias = Literal[
    "TLS_SNI",
    "HTTP_HOST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnabledAnalysisType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnabledAnalysisType:
    return cast(EnabledAnalysisType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnabledAnalysisType) -> str:
    return value


def deserialize_cbor(data: str) -> EnabledAnalysisType:
    return cast(EnabledAnalysisType, data)
