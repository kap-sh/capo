"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationState``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

EvaluationState: TypeAlias = Literal[
    "PARTIAL_DATA",
    "EVALUATION_FAILURE",
    "EVALUATION_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EvaluationState:
    return cast(EvaluationState, data)


# --- awsQuery ser/de ---
def to_query_text(value: EvaluationState) -> str:
    return value


def from_query_text(text: str) -> EvaluationState:
    return cast(EvaluationState, text)


def serialize_query(
    value: EvaluationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EvaluationState:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationState) -> str:
    return value


def deserialize_cbor(data: str) -> EvaluationState:
    return cast(EvaluationState, data)
