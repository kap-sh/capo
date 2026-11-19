"""Generated from Smithy shape ``com.amazonaws.cloudwatch#SingleMetricAnomalyDetector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.account_id
    import capo_cloudwatch.types.anomaly_detector_metric_stat
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace


class SingleMetricAnomalyDetector(TypedDict, closed=True):
    account_id: NotRequired["capo_cloudwatch.types.account_id.AccountId"]
    """<p>If the CloudWatch metric that provides the time series that the anomaly detector uses as input is in another account, specify that account ID here. If you omit this parameter, the current account is used.</p>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric to create the anomaly detection model for.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric to create the anomaly detection model for.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The metric dimensions to create the anomaly detection model for.</p>"""
    stat: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_metric_stat.AnomalyDetectorMetricStat"
    ]
    """<p>The statistic to use for the metric and anomaly detection model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SingleMetricAnomalyDetector) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> SingleMetricAnomalyDetector:
    out: SingleMetricAnomalyDetector = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
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
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: SingleMetricAnomalyDetector, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_id" in value:
        pairs.append((f"{key_prefix}AccountId", str(value["account_id"])))
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


def deserialize_query(el: Element) -> SingleMetricAnomalyDetector:
    out: SingleMetricAnomalyDetector = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SingleMetricAnomalyDetector) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
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
    return out


def deserialize_cbor(data: dict) -> SingleMetricAnomalyDetector:
    out: SingleMetricAnomalyDetector = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
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
    return out
