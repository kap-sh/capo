"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#GetScalingPlanResourceForecastDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.datapoints


class GetScalingPlanResourceForecastDataResponse(TypedDict, closed=True):
    datapoints: "capo_auto_scaling_plans.types.datapoints.Datapoints"
    """<p>The data points to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScalingPlanResourceForecastDataResponse) -> dict:
    out: dict = {}
    import capo_auto_scaling_plans.types.datapoints

    out["Datapoints"] = capo_auto_scaling_plans.types.datapoints.serialize_aws_json_1_1(
        value["datapoints"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScalingPlanResourceForecastDataResponse:
    out: GetScalingPlanResourceForecastDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("Datapoints") is not None:
        import capo_auto_scaling_plans.types.datapoints

        out["datapoints"] = (
            capo_auto_scaling_plans.types.datapoints.deserialize_aws_json_1_1(
                data["Datapoints"]
            )
        )
    else:
        out["datapoints"] = []
    return out
