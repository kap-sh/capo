"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EvaluationType``."""

from typing import Literal, TypeAlias, cast

EvaluationType: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationType:
    return cast(EvaluationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationType) -> str:
    return value


def deserialize_cbor(data: str) -> EvaluationType:
    return cast(EvaluationType, data)
