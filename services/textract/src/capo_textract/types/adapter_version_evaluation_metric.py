"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionEvaluationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.evaluation_metric
    import capo_textract.types.feature_type


class AdapterVersionEvaluationMetric(TypedDict, closed=True):
    baseline: NotRequired["capo_textract.types.evaluation_metric.EvaluationMetric"]
    """<p>The F1 score, precision, and recall metrics for the baseline model.</p>"""
    adapter_version: NotRequired[
        "capo_textract.types.evaluation_metric.EvaluationMetric"
    ]
    """<p>The F1 score, precision, and recall metrics for the baseline model.</p>"""
    feature_type: NotRequired["capo_textract.types.feature_type.FeatureType"]
    """<p>Indicates the feature type being analyzed by a given adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionEvaluationMetric) -> dict:
    out: dict = {}
    if "baseline" in value:
        import capo_textract.types.evaluation_metric

        out["Baseline"] = capo_textract.types.evaluation_metric.serialize_aws_json_1_1(
            value["baseline"]
        )
    if "adapter_version" in value:
        import capo_textract.types.evaluation_metric

        out["AdapterVersion"] = (
            capo_textract.types.evaluation_metric.serialize_aws_json_1_1(
                value["adapter_version"]
            )
        )
    if "feature_type" in value:
        import capo_textract.types.feature_type

        out["FeatureType"] = capo_textract.types.feature_type.serialize_aws_json_1_1(
            value["feature_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionEvaluationMetric:
    out: AdapterVersionEvaluationMetric = {}  # type: ignore[typeddict-item]
    if data.get("Baseline") is not None:
        import capo_textract.types.evaluation_metric

        out["baseline"] = (
            capo_textract.types.evaluation_metric.deserialize_aws_json_1_1(
                data["Baseline"]
            )
        )
    if data.get("AdapterVersion") is not None:
        import capo_textract.types.evaluation_metric

        out["adapter_version"] = (
            capo_textract.types.evaluation_metric.deserialize_aws_json_1_1(
                data["AdapterVersion"]
            )
        )
    if data.get("FeatureType") is not None:
        import capo_textract.types.feature_type

        out["feature_type"] = capo_textract.types.feature_type.deserialize_aws_json_1_1(
            data["FeatureType"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterVersionEvaluationMetric) -> dict:
    out: dict = {}
    if "baseline" in value:
        import capo_textract.types.evaluation_metric

        out["Baseline"] = capo_textract.types.evaluation_metric.serialize_cbor(
            value["baseline"]
        )
    if "adapter_version" in value:
        import capo_textract.types.evaluation_metric

        out["AdapterVersion"] = capo_textract.types.evaluation_metric.serialize_cbor(
            value["adapter_version"]
        )
    if "feature_type" in value:
        import capo_textract.types.feature_type

        out["FeatureType"] = capo_textract.types.feature_type.serialize_cbor(
            value["feature_type"]
        )
    return out


def deserialize_cbor(data: dict) -> AdapterVersionEvaluationMetric:
    out: AdapterVersionEvaluationMetric = {}  # type: ignore[typeddict-item]
    if data.get("Baseline") is not None:
        import capo_textract.types.evaluation_metric

        out["baseline"] = capo_textract.types.evaluation_metric.deserialize_cbor(
            data["Baseline"]
        )
    if data.get("AdapterVersion") is not None:
        import capo_textract.types.evaluation_metric

        out["adapter_version"] = capo_textract.types.evaluation_metric.deserialize_cbor(
            data["AdapterVersion"]
        )
    if data.get("FeatureType") is not None:
        import capo_textract.types.feature_type

        out["feature_type"] = capo_textract.types.feature_type.deserialize_cbor(
            data["FeatureType"]
        )
    return out
