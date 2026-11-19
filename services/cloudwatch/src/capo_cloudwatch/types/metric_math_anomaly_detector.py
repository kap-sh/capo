"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricMathAnomalyDetector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_queries


class MetricMathAnomalyDetector(TypedDict, closed=True):
    metric_data_queries: NotRequired[
        "capo_cloudwatch.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression. Each item in <code>MetricDataQueries</code> gets a metric or performs a math expression. One item in <code>MetricDataQueries</code> is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting <code>ReturnData</code> to <code>true</code> for this object in the array. For all other expressions and metrics, set <code>ReturnData</code> to <code>false</code>. The designated expression must return a single time series.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricMathAnomalyDetector) -> dict:
    out: dict = {}
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        out["MetricDataQueries"] = (
            capo_cloudwatch.types.metric_data_queries.serialize_aws_json_1_0(
                value["metric_data_queries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricMathAnomalyDetector:
    out: MetricMathAnomalyDetector = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataQueries") is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_aws_json_1_0(
                data["MetricDataQueries"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricMathAnomalyDetector, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        capo_cloudwatch.types.metric_data_queries.serialize_query(
            value["metric_data_queries"], pairs, f"{key_prefix}MetricDataQueries"
        )


def deserialize_query(el: Element) -> MetricMathAnomalyDetector:
    out: MetricMathAnomalyDetector = {}  # type: ignore[typeddict-item]
    child_metric_data_queries = el.find("MetricDataQueries")
    if child_metric_data_queries is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_query(
                child_metric_data_queries
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricMathAnomalyDetector) -> dict:
    out: dict = {}
    if "metric_data_queries" in value:
        import capo_cloudwatch.types.metric_data_queries

        out["MetricDataQueries"] = (
            capo_cloudwatch.types.metric_data_queries.serialize_cbor(
                value["metric_data_queries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> MetricMathAnomalyDetector:
    out: MetricMathAnomalyDetector = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataQueries") is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_cbor(
                data["MetricDataQueries"]
            )
        )
    return out
