"""Generated from Smithy shape ``com.amazonaws.mwaa#MetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mwaa.types.dimensions
    import capo_mwaa.types.statistic_set
    import capo_mwaa.types.unit


class MetricDatum(TypedDict, closed=True):
    metric_name: "str"
    """<p> <b>Internal only</b>. The name of the metric.</p>"""
    timestamp: "datetime.datetime"
    """<p> <b>Internal only</b>. The time the metric data was received, expressed as an ISO 8601 datetime string.</p>"""
    dimensions: NotRequired["capo_mwaa.types.dimensions.Dimensions"]
    """<p> <b>Internal only</b>. The dimensions associated with the metric.</p>"""
    value: NotRequired["float"]
    """<p> <b>Internal only</b>. The value for the metric.</p>"""
    unit: NotRequired["capo_mwaa.types.unit.Unit"]
    """<p> <b>Internal only</b>. The unit used to store the metric.</p>"""
    statistic_values: NotRequired["capo_mwaa.types.statistic_set.StatisticSet"]
    """<p> <b>Internal only</b>. The statistical values for the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatum) -> dict:
    out: dict = {}
    out["MetricName"] = value["metric_name"]
    import capo_mwaa.types._prelude.timestamp

    out["Timestamp"] = capo_mwaa.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "dimensions" in value:
        import capo_mwaa.types.dimensions

        out["Dimensions"] = capo_mwaa.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "statistic_values" in value:
        import capo_mwaa.types.statistic_set

        out["StatisticValues"] = capo_mwaa.types.statistic_set.serialize_json(
            value["statistic_values"]
        )
    return out


def deserialize_json(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        out["metric_name"] = ""
    if data.get("Timestamp") is not None:
        import capo_mwaa.types._prelude.timestamp

        out["timestamp"] = capo_mwaa.types._prelude.timestamp.deserialize_json(
            data["Timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Dimensions") is not None:
        import capo_mwaa.types.dimensions

        out["dimensions"] = capo_mwaa.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    if data.get("StatisticValues") is not None:
        import capo_mwaa.types.statistic_set

        out["statistic_values"] = capo_mwaa.types.statistic_set.deserialize_json(
            data["StatisticValues"]
        )
    return out
