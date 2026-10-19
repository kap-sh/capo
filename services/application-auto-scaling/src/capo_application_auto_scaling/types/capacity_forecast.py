"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#CapacityForecast``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps
    import capo_application_auto_scaling.types.predictive_scaling_forecast_values


class CapacityForecast(TypedDict, closed=True):
    timestamps: "capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps.PredictiveScalingForecastTimestamps"
    """<p> The timestamps for the data points, in UTC format. </p>"""
    values: "capo_application_auto_scaling.types.predictive_scaling_forecast_values.PredictiveScalingForecastValues"
    """<p> The values of the data points. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityForecast) -> dict:
    out: dict = {}
    import capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps

    out["Timestamps"] = (
        capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps.serialize_aws_json_1_1(
            value["timestamps"]
        )
    )
    import capo_application_auto_scaling.types.predictive_scaling_forecast_values

    out["Values"] = (
        capo_application_auto_scaling.types.predictive_scaling_forecast_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityForecast:
    out: CapacityForecast = {}  # type: ignore[typeddict-item]
    if data.get("Timestamps") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps

        out["timestamps"] = (
            capo_application_auto_scaling.types.predictive_scaling_forecast_timestamps.deserialize_aws_json_1_1(
                data["Timestamps"]
            )
        )
    else:
        out["timestamps"] = []
    if data.get("Values") is not None:
        import capo_application_auto_scaling.types.predictive_scaling_forecast_values

        out["values"] = (
            capo_application_auto_scaling.types.predictive_scaling_forecast_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
