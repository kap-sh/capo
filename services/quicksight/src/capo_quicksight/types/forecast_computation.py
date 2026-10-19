"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.double
    import capo_quicksight.types.forecast_computation_custom_seasonality_value
    import capo_quicksight.types.forecast_computation_seasonality
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.periods_backward
    import capo_quicksight.types.periods_forward
    import capo_quicksight.types.prediction_interval
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class ForecastComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    periods_forward: NotRequired["capo_quicksight.types.periods_forward.PeriodsForward"]
    """<p>The periods forward setup of a forecast computation.</p>"""
    periods_backward: NotRequired[
        "capo_quicksight.types.periods_backward.PeriodsBackward"
    ]
    """<p>The periods backward setup of a forecast computation.</p>"""
    upper_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The upper boundary setup of a forecast computation.</p>"""
    lower_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The lower boundary setup of a forecast computation.</p>"""
    prediction_interval: NotRequired[
        "capo_quicksight.types.prediction_interval.PredictionInterval"
    ]
    """<p>The prediction interval setup of a forecast computation.</p>"""
    seasonality: NotRequired[
        "capo_quicksight.types.forecast_computation_seasonality.ForecastComputationSeasonality"
    ]
    """<p>The seasonality setup of a forecast computation. Choose one of the following options:</p> <ul> <li> <p> <code>AUTOMATIC</code> </p> </li> <li> <p> <code>CUSTOM</code>: Checks the custom seasonality value.</p> </li> </ul>"""
    custom_seasonality_value: NotRequired[
        "capo_quicksight.types.forecast_computation_custom_seasonality_value.ForecastComputationCustomSeasonalityValue"
    ]
    """<p>The custom seasonality value setup of a forecast computation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["Time"] = capo_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["Value"] = capo_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "periods_forward" in value:
        out["PeriodsForward"] = value["periods_forward"]
    if "periods_backward" in value:
        out["PeriodsBackward"] = value["periods_backward"]
    if "upper_boundary" in value:
        out["UpperBoundary"] = (
            "NaN"
            if value["upper_boundary"] != value["upper_boundary"]
            else "Infinity"
            if value["upper_boundary"] == float("inf")
            else "-Infinity"
            if value["upper_boundary"] == float("-inf")
            else value["upper_boundary"]
        )
    if "lower_boundary" in value:
        out["LowerBoundary"] = (
            "NaN"
            if value["lower_boundary"] != value["lower_boundary"]
            else "Infinity"
            if value["lower_boundary"] == float("inf")
            else "-Infinity"
            if value["lower_boundary"] == float("-inf")
            else value["lower_boundary"]
        )
    if "prediction_interval" in value:
        out["PredictionInterval"] = value["prediction_interval"]
    if "seasonality" in value:
        import capo_quicksight.types.forecast_computation_seasonality

        out["Seasonality"] = (
            capo_quicksight.types.forecast_computation_seasonality.serialize_json(
                value["seasonality"]
            )
        )
    if "custom_seasonality_value" in value:
        out["CustomSeasonalityValue"] = value["custom_seasonality_value"]
    return out


def deserialize_json(data: dict) -> ForecastComputation:
    out: ForecastComputation = {}  # type: ignore[typeddict-item]
    if data.get("ComputationId") is not None:
        out["computation_id"] = data["ComputationId"]
    else:
        out["computation_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Time") is not None:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if data.get("PeriodsForward") is not None:
        out["periods_forward"] = data["PeriodsForward"]
    if data.get("PeriodsBackward") is not None:
        out["periods_backward"] = data["PeriodsBackward"]
    if data.get("UpperBoundary") is not None:
        out["upper_boundary"] = float(data["UpperBoundary"])
    if data.get("LowerBoundary") is not None:
        out["lower_boundary"] = float(data["LowerBoundary"])
    if data.get("PredictionInterval") is not None:
        out["prediction_interval"] = data["PredictionInterval"]
    if data.get("Seasonality") is not None:
        import capo_quicksight.types.forecast_computation_seasonality

        out["seasonality"] = (
            capo_quicksight.types.forecast_computation_seasonality.deserialize_json(
                data["Seasonality"]
            )
        )
    if data.get("CustomSeasonalityValue") is not None:
        out["custom_seasonality_value"] = data["CustomSeasonalityValue"]
    return out


def redact_sensitive(value: ForecastComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["time"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.redact_sensitive(
            value["value"]
        )
    return out
