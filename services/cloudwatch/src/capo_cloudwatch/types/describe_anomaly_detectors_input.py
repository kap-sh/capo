"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAnomalyDetectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_ids
    import capo_cloudwatch.types.anomaly_detector_types
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.max_returned_results_count
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.next_token


class DescribeAnomalyDetectorsInput(TypedDict, closed=True):
    anomaly_detector_ids: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_ids.AnomalyDetectorIds"
    ]
    """<p>Specifies the unique identifiers of the anomaly detectors to describe. You can specify up to 50 identifiers. If you specify this parameter, you cannot also specify the <code>Namespace</code>, <code>MetricName</code>, <code>Dimensions</code>, or <code>AnomalyDetectorTypes</code> metric filters.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>Use the token returned by the previous operation to request the next page of results.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch.types.max_returned_results_count.MaxReturnedResultsCount"
    ]
    """<p>The maximum number of results to return in one operation. The maximum value that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>Limits the results to only the anomaly detection models that are associated with the specified namespace.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>Limits the results to only the anomaly detection models that are associated with the specified metric name. If there are multiple metrics with this name in different namespaces that have anomaly detection models, they're all returned.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>Limits the results to only the anomaly detection models that are associated with the specified metric dimensions. If there are multiple metrics that have these dimensions and have anomaly detection models associated, they're all returned.</p>"""
    anomaly_detector_types: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_types.AnomalyDetectorTypes"
    ]
    """<p>The anomaly detector types to request when using <code>DescribeAnomalyDetectorsInput</code>. If empty, defaults to <code>SINGLE_METRIC</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAnomalyDetectorsInput) -> dict:
    out: dict = {}
    if "anomaly_detector_ids" in value:
        import capo_cloudwatch.types.anomaly_detector_ids

        out["AnomalyDetectorIds"] = (
            capo_cloudwatch.types.anomaly_detector_ids.serialize_aws_json_1_0(
                value["anomaly_detector_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "anomaly_detector_types" in value:
        import capo_cloudwatch.types.anomaly_detector_types

        out["AnomalyDetectorTypes"] = (
            capo_cloudwatch.types.anomaly_detector_types.serialize_aws_json_1_0(
                value["anomaly_detector_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAnomalyDetectorsInput:
    out: DescribeAnomalyDetectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorIds") is not None:
        import capo_cloudwatch.types.anomaly_detector_ids

        out["anomaly_detector_ids"] = (
            capo_cloudwatch.types.anomaly_detector_ids.deserialize_aws_json_1_0(
                data["AnomalyDetectorIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("AnomalyDetectorTypes") is not None:
        import capo_cloudwatch.types.anomaly_detector_types

        out["anomaly_detector_types"] = (
            capo_cloudwatch.types.anomaly_detector_types.deserialize_aws_json_1_0(
                data["AnomalyDetectorTypes"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAnomalyDetectorsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "anomaly_detector_ids" in value:
        import capo_cloudwatch.types.anomaly_detector_ids

        capo_cloudwatch.types.anomaly_detector_ids.serialize_query(
            value["anomaly_detector_ids"], pairs, f"{key_prefix}AnomalyDetectorIds"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "anomaly_detector_types" in value:
        import capo_cloudwatch.types.anomaly_detector_types

        capo_cloudwatch.types.anomaly_detector_types.serialize_query(
            value["anomaly_detector_types"], pairs, f"{key_prefix}AnomalyDetectorTypes"
        )


def deserialize_query(el: Element) -> DescribeAnomalyDetectorsInput:
    out: DescribeAnomalyDetectorsInput = {}  # type: ignore[typeddict-item]
    child_anomaly_detector_ids = el.find("AnomalyDetectorIds")
    if child_anomaly_detector_ids is not None:
        import capo_cloudwatch.types.anomaly_detector_ids

        out["anomaly_detector_ids"] = (
            capo_cloudwatch.types.anomaly_detector_ids.deserialize_query(
                child_anomaly_detector_ids
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
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
    child_anomaly_detector_types = el.find("AnomalyDetectorTypes")
    if child_anomaly_detector_types is not None:
        import capo_cloudwatch.types.anomaly_detector_types

        out["anomaly_detector_types"] = (
            capo_cloudwatch.types.anomaly_detector_types.deserialize_query(
                child_anomaly_detector_types
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAnomalyDetectorsInput) -> dict:
    out: dict = {}
    if "anomaly_detector_ids" in value:
        import capo_cloudwatch.types.anomaly_detector_ids

        out["AnomalyDetectorIds"] = (
            capo_cloudwatch.types.anomaly_detector_ids.serialize_cbor(
                value["anomaly_detector_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_cbor(
            value["dimensions"]
        )
    if "anomaly_detector_types" in value:
        import capo_cloudwatch.types.anomaly_detector_types

        out["AnomalyDetectorTypes"] = (
            capo_cloudwatch.types.anomaly_detector_types.serialize_cbor(
                value["anomaly_detector_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeAnomalyDetectorsInput:
    out: DescribeAnomalyDetectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorIds") is not None:
        import capo_cloudwatch.types.anomaly_detector_ids

        out["anomaly_detector_ids"] = (
            capo_cloudwatch.types.anomaly_detector_ids.deserialize_cbor(
                data["AnomalyDetectorIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_cbor(
            data["Dimensions"]
        )
    if data.get("AnomalyDetectorTypes") is not None:
        import capo_cloudwatch.types.anomaly_detector_types

        out["anomaly_detector_types"] = (
            capo_cloudwatch.types.anomaly_detector_types.deserialize_cbor(
                data["AnomalyDetectorTypes"]
            )
        )
    return out
