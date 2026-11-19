"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionEvaluationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.adapter_version_evaluation_metric

AdapterVersionEvaluationMetrics: TypeAlias = list[
    "capo_textract.types.adapter_version_evaluation_metric.AdapterVersionEvaluationMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionEvaluationMetrics) -> list:
    import capo_textract.types.adapter_version_evaluation_metric

    out: list = []
    for item in value:
        out.append(
            capo_textract.types.adapter_version_evaluation_metric.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdapterVersionEvaluationMetrics:
    import capo_textract.types.adapter_version_evaluation_metric

    out: AdapterVersionEvaluationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.adapter_version_evaluation_metric.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterVersionEvaluationMetrics) -> list:
    import capo_textract.types.adapter_version_evaluation_metric

    out: list = []
    for item in value:
        out.append(
            capo_textract.types.adapter_version_evaluation_metric.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AdapterVersionEvaluationMetrics:
    import capo_textract.types.adapter_version_evaluation_metric

    out: AdapterVersionEvaluationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.adapter_version_evaluation_metric.deserialize_cbor(item)
        )
    return out
