"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAnomalyDetectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_id
    import capo_cloudwatch.types.anomaly_detector_metric_stat
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.metric_math_anomaly_detector
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.single_metric_anomaly_detector


class DeleteAnomalyDetectorInput(TypedDict, closed=True):
    anomaly_detector_id: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_id.AnomalyDetectorId"
    ]
    """<p>Specifies the unique identifier of the anomaly detector to delete. If you specify this parameter, you do not need to specify a metric to identify the detector.</p>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace associated with the anomaly detection model to delete.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The metric name associated with the anomaly detection model to delete.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The metric dimensions associated with the anomaly detection model to delete.</p>"""
    stat: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
    ]
    """<p>The statistic associated with the anomaly detection model to delete.</p>"""
    single_metric_anomaly_detector: NotRequired[
        "capo_cloudwatch.types.single_metric_anomaly_detector.SingleMetricAnomalyDetector"
    ]
    """<p>A single metric anomaly detector to be deleted.</p> <p>When using <code>SingleMetricAnomalyDetector</code>, you cannot include the following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>MetricMathAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the single metric anomaly detector attributes as part of the <code>SingleMetricAnomalyDetector</code> property.</p>"""
    metric_math_anomaly_detector: NotRequired[
        "capo_cloudwatch.types.metric_math_anomaly_detector.MetricMathAnomalyDetector"
    ]
    """<p>The metric math anomaly detector to be deleted.</p> <p>When using <code>MetricMathAnomalyDetector</code>, you cannot include following parameters in the same operation:</p> <ul> <li> <p> <code>Dimensions</code>,</p> </li> <li> <p> <code>MetricName</code> </p> </li> <li> <p> <code>Namespace</code> </p> </li> <li> <p> <code>Stat</code> </p> </li> <li> <p>the <code>SingleMetricAnomalyDetector</code> parameters of <code>DeleteAnomalyDetectorInput</code> </p> </li> </ul> <p>Instead, specify the metric math anomaly detector attributes as part of the <code>MetricMathAnomalyDetector</code> property.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAnomalyDetectorInput) -> dict:
    out: dict = {}
    if "anomaly_detector_id" in value:
        out["AnomalyDetectorId"] = value["anomaly_detector_id"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "single_metric_anomaly_detector" in value:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        out["SingleMetricAnomalyDetector"] = (
            capo_cloudwatch.types.single_metric_anomaly_detector.serialize_aws_json_1_0(
                value["single_metric_anomaly_detector"]
            )
        )
    if "metric_math_anomaly_detector" in value:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        out["MetricMathAnomalyDetector"] = (
            capo_cloudwatch.types.metric_math_anomaly_detector.serialize_aws_json_1_0(
                value["metric_math_anomaly_detector"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAnomalyDetectorInput:
    out: DeleteAnomalyDetectorInput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorId") is not None:
        out["anomaly_detector_id"] = data["AnomalyDetectorId"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    if data.get("SingleMetricAnomalyDetector") is not None:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        out["single_metric_anomaly_detector"] = (
            capo_cloudwatch.types.single_metric_anomaly_detector.deserialize_aws_json_1_0(
                data["SingleMetricAnomalyDetector"]
            )
        )
    if data.get("MetricMathAnomalyDetector") is not None:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        out["metric_math_anomaly_detector"] = (
            capo_cloudwatch.types.metric_math_anomaly_detector.deserialize_aws_json_1_0(
                data["MetricMathAnomalyDetector"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnomalyDetectorInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "anomaly_detector_id" in value:
        pairs.append(
            (f"{key_prefix}AnomalyDetectorId", str(value["anomaly_detector_id"]))
        )
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "stat" in value:
        pairs.append((f"{key_prefix}Stat", str(value["stat"])))
    if "single_metric_anomaly_detector" in value:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        capo_cloudwatch.types.single_metric_anomaly_detector.serialize_query(
            value["single_metric_anomaly_detector"],
            pairs,
            f"{key_prefix}SingleMetricAnomalyDetector",
        )
    if "metric_math_anomaly_detector" in value:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        capo_cloudwatch.types.metric_math_anomaly_detector.serialize_query(
            value["metric_math_anomaly_detector"],
            pairs,
            f"{key_prefix}MetricMathAnomalyDetector",
        )


def deserialize_query(el: Element) -> DeleteAnomalyDetectorInput:
    out: DeleteAnomalyDetectorInput = {}  # type: ignore[typeddict-item]
    child_anomaly_detector_id = el.find("AnomalyDetectorId")
    if child_anomaly_detector_id is not None:
        out["anomaly_detector_id"] = str(child_anomaly_detector_id.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_stat = el.find("Stat")
    if child_stat is not None:
        out["stat"] = str(child_stat.text or "")
    child_single_metric_anomaly_detector = el.find("SingleMetricAnomalyDetector")
    if child_single_metric_anomaly_detector is not None:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        out["single_metric_anomaly_detector"] = (
            capo_cloudwatch.types.single_metric_anomaly_detector.deserialize_query(
                child_single_metric_anomaly_detector
            )
        )
    child_metric_math_anomaly_detector = el.find("MetricMathAnomalyDetector")
    if child_metric_math_anomaly_detector is not None:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        out["metric_math_anomaly_detector"] = (
            capo_cloudwatch.types.metric_math_anomaly_detector.deserialize_query(
                child_metric_math_anomaly_detector
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAnomalyDetectorInput) -> dict:
    out: dict = {}
    if "anomaly_detector_id" in value:
        out["AnomalyDetectorId"] = value["anomaly_detector_id"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_cbor(
            value["dimensions"]
        )
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "single_metric_anomaly_detector" in value:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        out["SingleMetricAnomalyDetector"] = (
            capo_cloudwatch.types.single_metric_anomaly_detector.serialize_cbor(
                value["single_metric_anomaly_detector"]
            )
        )
    if "metric_math_anomaly_detector" in value:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        out["MetricMathAnomalyDetector"] = (
            capo_cloudwatch.types.metric_math_anomaly_detector.serialize_cbor(
                value["metric_math_anomaly_detector"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteAnomalyDetectorInput:
    out: DeleteAnomalyDetectorInput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorId") is not None:
        out["anomaly_detector_id"] = data["AnomalyDetectorId"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_cbor(
            data["Dimensions"]
        )
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    if data.get("SingleMetricAnomalyDetector") is not None:
        import capo_cloudwatch.types.single_metric_anomaly_detector

        out["single_metric_anomaly_detector"] = (
            capo_cloudwatch.types.single_metric_anomaly_detector.deserialize_cbor(
                data["SingleMetricAnomalyDetector"]
            )
        )
    if data.get("MetricMathAnomalyDetector") is not None:
        import capo_cloudwatch.types.metric_math_anomaly_detector

        out["metric_math_anomaly_detector"] = (
            capo_cloudwatch.types.metric_math_anomaly_detector.deserialize_cbor(
                data["MetricMathAnomalyDetector"]
            )
        )
    return out
