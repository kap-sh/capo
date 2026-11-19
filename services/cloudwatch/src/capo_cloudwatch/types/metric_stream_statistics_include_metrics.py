"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamStatisticsIncludeMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_statistics_metric

MetricStreamStatisticsIncludeMetrics: TypeAlias = list[
    "capo_cloudwatch.types.metric_stream_statistics_metric.MetricStreamStatisticsMetric"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamStatisticsIncludeMetrics,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_stream_statistics_metric.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricStreamStatisticsIncludeMetrics:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: MetricStreamStatisticsIncludeMetrics,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_stream_statistics_metric.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> MetricStreamStatisticsIncludeMetrics:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamStatisticsIncludeMetrics) -> list:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricStreamStatisticsIncludeMetrics:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamStatisticsIncludeMetrics) -> list:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> MetricStreamStatisticsIncludeMetrics:
    import capo_cloudwatch.types.metric_stream_statistics_metric

    out: MetricStreamStatisticsIncludeMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_stream_statistics_metric.deserialize_cbor(item)
        )
    return out
