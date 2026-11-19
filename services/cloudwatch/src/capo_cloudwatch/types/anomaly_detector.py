"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_configuration
    import capo_cloudwatch.types.anomaly_detector_id
    import capo_cloudwatch.types.anomaly_detector_metric_stat
    import capo_cloudwatch.types.anomaly_detector_state_value
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.metric_characteristics
    import capo_cloudwatch.types.metric_math_anomaly_detector
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.single_metric_anomaly_detector


class AnomalyDetector(TypedDict, closed=True):
    anomaly_detector_id: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_id.AnomalyDetectorId"
    ]
    """<p>The unique identifier of the anomaly detector.</p> <note> <p>The identifier does not restrict access to a specific anomaly detector in an IAM policy. Permissions for anomaly detector operations apply to all anomaly detectors in the account.</p> </note>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric associated with the anomaly detection model.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric associated with the anomaly detection model.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The metric dimensions associated with the anomaly detection model.</p>"""
    stat: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
    ]
    """<p>The statistic associated with the anomaly detection model.</p>"""
    configuration: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_configuration.AnomalyDetectorConfiguration"
    ]
    """<p>The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model, and the time zone to use for the metric.</p>"""
    state_value: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_state_value.AnomalyDetectorStateValue"
    ]
    """<p>The current status of the anomaly detector's training.</p>"""
    metric_characteristics: NotRequired[
        "capo_cloudwatch.types.metric_characteristics.MetricCharacteristics"
    ]
    """<p>This object includes parameters that you can use to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models. Currently, it includes the <code>PeriodicSpikes</code> parameter.</p>"""
    single_metric_anomaly_detector: NotRequired[
        "capo_cloudwatch.types.single_metric_anomaly_detector.SingleMetricAnomalyDetector"
    ]
    """<p>The CloudWatch metric and statistic for this anomaly detector.</p>"""
    metric_math_anomaly_detector: NotRequired[
        "capo_cloudwatch.types.metric_math_anomaly_detector.MetricMathAnomalyDetector"
    ]
    """<p>The CloudWatch metric math expression for this anomaly detector.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetector) -> dict:
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
    if "configuration" in value:
        import capo_cloudwatch.types.anomaly_detector_configuration

        out["Configuration"] = (
            capo_cloudwatch.types.anomaly_detector_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "state_value" in value:
        import capo_cloudwatch.types.anomaly_detector_state_value

        out["StateValue"] = (
            capo_cloudwatch.types.anomaly_detector_state_value.serialize_aws_json_1_0(
                value["state_value"]
            )
        )
    if "metric_characteristics" in value:
        import capo_cloudwatch.types.metric_characteristics

        out["MetricCharacteristics"] = (
            capo_cloudwatch.types.metric_characteristics.serialize_aws_json_1_0(
                value["metric_characteristics"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> AnomalyDetector:
    out: AnomalyDetector = {}  # type: ignore[typeddict-item]
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
    if data.get("Configuration") is not None:
        import capo_cloudwatch.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_cloudwatch.types.anomaly_detector_configuration.deserialize_aws_json_1_0(
                data["Configuration"]
            )
        )
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.anomaly_detector_state_value

        out["state_value"] = (
            capo_cloudwatch.types.anomaly_detector_state_value.deserialize_aws_json_1_0(
                data["StateValue"]
            )
        )
    if data.get("MetricCharacteristics") is not None:
        import capo_cloudwatch.types.metric_characteristics

        out["metric_characteristics"] = (
            capo_cloudwatch.types.metric_characteristics.deserialize_aws_json_1_0(
                data["MetricCharacteristics"]
            )
        )
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
    value: AnomalyDetector, pairs: list[tuple[str, str]], prefix: str
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
    if "configuration" in value:
        import capo_cloudwatch.types.anomaly_detector_configuration

        capo_cloudwatch.types.anomaly_detector_configuration.serialize_query(
            value["configuration"], pairs, f"{key_prefix}Configuration"
        )
    if "state_value" in value:
        import capo_cloudwatch.types.anomaly_detector_state_value

        capo_cloudwatch.types.anomaly_detector_state_value.serialize_query(
            value["state_value"], pairs, f"{key_prefix}StateValue"
        )
    if "metric_characteristics" in value:
        import capo_cloudwatch.types.metric_characteristics

        capo_cloudwatch.types.metric_characteristics.serialize_query(
            value["metric_characteristics"], pairs, f"{key_prefix}MetricCharacteristics"
        )
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


def deserialize_query(el: Element) -> AnomalyDetector:
    out: AnomalyDetector = {}  # type: ignore[typeddict-item]
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
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        import capo_cloudwatch.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_cloudwatch.types.anomaly_detector_configuration.deserialize_query(
                child_configuration
            )
        )
    child_state_value = el.find("StateValue")
    if child_state_value is not None:
        import capo_cloudwatch.types.anomaly_detector_state_value

        out["state_value"] = (
            capo_cloudwatch.types.anomaly_detector_state_value.deserialize_query(
                child_state_value
            )
        )
    child_metric_characteristics = el.find("MetricCharacteristics")
    if child_metric_characteristics is not None:
        import capo_cloudwatch.types.metric_characteristics

        out["metric_characteristics"] = (
            capo_cloudwatch.types.metric_characteristics.deserialize_query(
                child_metric_characteristics
            )
        )
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
def serialize_cbor(value: AnomalyDetector) -> dict:
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
    if "configuration" in value:
        import capo_cloudwatch.types.anomaly_detector_configuration

        out["Configuration"] = (
            capo_cloudwatch.types.anomaly_detector_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    if "state_value" in value:
        import capo_cloudwatch.types.anomaly_detector_state_value

        out["StateValue"] = (
            capo_cloudwatch.types.anomaly_detector_state_value.serialize_cbor(
                value["state_value"]
            )
        )
    if "metric_characteristics" in value:
        import capo_cloudwatch.types.metric_characteristics

        out["MetricCharacteristics"] = (
            capo_cloudwatch.types.metric_characteristics.serialize_cbor(
                value["metric_characteristics"]
            )
        )
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


def deserialize_cbor(data: dict) -> AnomalyDetector:
    out: AnomalyDetector = {}  # type: ignore[typeddict-item]
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
    if data.get("Configuration") is not None:
        import capo_cloudwatch.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_cloudwatch.types.anomaly_detector_configuration.deserialize_cbor(
                data["Configuration"]
            )
        )
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.anomaly_detector_state_value

        out["state_value"] = (
            capo_cloudwatch.types.anomaly_detector_state_value.deserialize_cbor(
                data["StateValue"]
            )
        )
    if data.get("MetricCharacteristics") is not None:
        import capo_cloudwatch.types.metric_characteristics

        out["metric_characteristics"] = (
            capo_cloudwatch.types.metric_characteristics.deserialize_cbor(
                data["MetricCharacteristics"]
            )
        )
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
