"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricsDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.export_dimensions
    import capo_sesv2.types.export_metrics
    import capo_sesv2.types.metric_namespace
    import capo_sesv2.types.timestamp


class MetricsDataSource(TypedDict, closed=True):
    dimensions: "capo_sesv2.types.export_dimensions.ExportDimensions"
    """<p>An object that contains a mapping between a <code>MetricDimensionName</code> and <code>MetricDimensionValue</code> to filter metrics by. Must contain a least 1 dimension but no more than 3 unique ones.</p>"""
    namespace: "capo_sesv2.types.metric_namespace.MetricNamespace"
    """<p>The metrics namespace - e.g., <code>VDM</code>.</p>"""
    metrics: "capo_sesv2.types.export_metrics.ExportMetrics"
    """<p>A list of <code>ExportMetric</code> objects to export.</p>"""
    start_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the export interval as a timestamp.</p>"""
    end_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the export interval as a timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsDataSource) -> dict:
    out: dict = {}
    import capo_sesv2.types.export_dimensions

    out["Dimensions"] = capo_sesv2.types.export_dimensions.serialize_json(
        value["dimensions"]
    )
    import capo_sesv2.types.metric_namespace

    out["Namespace"] = capo_sesv2.types.metric_namespace.serialize_json(
        value["namespace"]
    )
    import capo_sesv2.types.export_metrics

    out["Metrics"] = capo_sesv2.types.export_metrics.serialize_json(value["metrics"])
    import capo_sesv2.types.timestamp

    out["StartDate"] = capo_sesv2.types.timestamp.serialize_json(value["start_date"])
    import capo_sesv2.types.timestamp

    out["EndDate"] = capo_sesv2.types.timestamp.serialize_json(value["end_date"])
    return out


def deserialize_json(data: dict) -> MetricsDataSource:
    out: MetricsDataSource = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_sesv2.types.export_dimensions

        out["dimensions"] = capo_sesv2.types.export_dimensions.deserialize_json(
            data["Dimensions"]
        )
    else:
        out["dimensions"] = {}
    if data.get("Namespace") is not None:
        import capo_sesv2.types.metric_namespace

        out["namespace"] = capo_sesv2.types.metric_namespace.deserialize_json(
            data["Namespace"]
        )
    else:
        import typing

        out["namespace"] = typing.cast(
            "capo_sesv2.types.metric_namespace.MetricNamespace", ""
        )
    if data.get("Metrics") is not None:
        import capo_sesv2.types.export_metrics

        out["metrics"] = capo_sesv2.types.export_metrics.deserialize_json(
            data["Metrics"]
        )
    else:
        out["metrics"] = []
    if data.get("StartDate") is not None:
        import capo_sesv2.types.timestamp

        out["start_date"] = capo_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndDate") is not None:
        import capo_sesv2.types.timestamp

        out["end_date"] = capo_sesv2.types.timestamp.deserialize_json(data["EndDate"])
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
