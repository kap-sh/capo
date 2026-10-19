"""Generated from Smithy shape ``com.amazonaws.forecast#ExplainabilityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.time_point_granularity
    import capo_forecast.types.time_series_granularity


class ExplainabilityConfig(TypedDict, closed=True):
    time_series_granularity: (
        "capo_forecast.types.time_series_granularity.TimeSeriesGranularity"
    )
    """<p>To create an Explainability for all time series in your datasets, use <code>ALL</code>. To create an Explainability for specific time series in your datasets, use <code>SPECIFIC</code>.</p> <p>Specify time series by uploading a CSV or Parquet file to an Amazon S3 bucket and set the location within the <a>DataDestination</a> data type.</p>"""
    time_point_granularity: (
        "capo_forecast.types.time_point_granularity.TimePointGranularity"
    )
    """<p>To create an Explainability for all time points in your forecast horizon, use <code>ALL</code>. To create an Explainability for specific time points in your forecast horizon, use <code>SPECIFIC</code>.</p> <p>Specify time points with the <code>StartDateTime</code> and <code>EndDateTime</code> parameters within the <a>CreateExplainability</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainabilityConfig) -> dict:
    out: dict = {}
    import capo_forecast.types.time_series_granularity

    out["TimeSeriesGranularity"] = (
        capo_forecast.types.time_series_granularity.serialize_aws_json_1_1(
            value["time_series_granularity"]
        )
    )
    import capo_forecast.types.time_point_granularity

    out["TimePointGranularity"] = (
        capo_forecast.types.time_point_granularity.serialize_aws_json_1_1(
            value["time_point_granularity"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExplainabilityConfig:
    out: ExplainabilityConfig = {}  # type: ignore[typeddict-item]
    if data.get("TimeSeriesGranularity") is not None:
        import capo_forecast.types.time_series_granularity

        out["time_series_granularity"] = (
            capo_forecast.types.time_series_granularity.deserialize_aws_json_1_1(
                data["TimeSeriesGranularity"]
            )
        )
    else:
        import typing

        out["time_series_granularity"] = typing.cast(
            "capo_forecast.types.time_series_granularity.TimeSeriesGranularity", ""
        )
    if data.get("TimePointGranularity") is not None:
        import capo_forecast.types.time_point_granularity

        out["time_point_granularity"] = (
            capo_forecast.types.time_point_granularity.deserialize_aws_json_1_1(
                data["TimePointGranularity"]
            )
        )
    else:
        import typing

        out["time_point_granularity"] = typing.cast(
            "capo_forecast.types.time_point_granularity.TimePointGranularity", ""
        )
    return out
