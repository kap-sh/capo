"""Generated from Smithy shape ``com.amazonaws.fms#EvaluationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.evaluation_result

EvaluationResults: TypeAlias = list["capo_fms.types.evaluation_result.EvaluationResult"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResults) -> list:
    import capo_fms.types.evaluation_result

    out: list = []
    for item in value:
        out.append(capo_fms.types.evaluation_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EvaluationResults:
    import capo_fms.types.evaluation_result

    out: EvaluationResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.evaluation_result.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationResults) -> list:
    import capo_fms.types.evaluation_result

    out: list = []
    for item in value:
        out.append(capo_fms.types.evaluation_result.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EvaluationResults:
    import capo_fms.types.evaluation_result

    out: EvaluationResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.evaluation_result.deserialize_cbor(item))
    return out
