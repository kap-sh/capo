"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#GetScalingPlanResourceForecastDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.forecast_data_type
    import capo_auto_scaling_plans.types.scalable_dimension
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_version
    import capo_auto_scaling_plans.types.service_namespace
    import capo_auto_scaling_plans.types.timestamp_type
    import capo_auto_scaling_plans.types.xml_string


class GetScalingPlanResourceForecastDataRequest(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>"""
    service_namespace: (
        "capo_auto_scaling_plans.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the AWS service. The only valid value is <code>autoscaling</code>. </p>"""
    resource_id: "capo_auto_scaling_plans.types.xml_string.XmlString"
    """<p>The ID of the resource. This string consists of a prefix (<code>autoScalingGroup</code>) followed by the name of a specified Auto Scaling group (<code>my-asg</code>). Example: <code>autoScalingGroup/my-asg</code>. </p>"""
    scalable_dimension: (
        "capo_auto_scaling_plans.types.scalable_dimension.ScalableDimension"
    )
    """<p>The scalable dimension for the resource. The only valid value is <code>autoscaling:autoScalingGroup:DesiredCapacity</code>. </p>"""
    forecast_data_type: (
        "capo_auto_scaling_plans.types.forecast_data_type.ForecastDataType"
    )
    """<p>The type of forecast data to get.</p> <ul> <li> <p> <code>LoadForecast</code>: The load metric forecast. </p> </li> <li> <p> <code>CapacityForecast</code>: The capacity forecast. </p> </li> <li> <p> <code>ScheduledActionMinCapacity</code>: The minimum capacity for each scheduled scaling action. This data is calculated as the larger of two values: the capacity forecast or the minimum capacity in the scaling instruction.</p> </li> <li> <p> <code>ScheduledActionMaxCapacity</code>: The maximum capacity for each scheduled scaling action. The calculation used is determined by the predictive scaling maximum capacity behavior setting in the scaling instruction.</p> </li> </ul>"""
    start_time: "capo_auto_scaling_plans.types.timestamp_type.TimestampType"
    """<p>The inclusive start time of the time range for the forecast data to get. The date and time can be at most 56 days before the current date and time. </p>"""
    end_time: "capo_auto_scaling_plans.types.timestamp_type.TimestampType"
    """<p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is seven days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. AWS Auto Scaling only issues forecasts for periods of two days in advance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScalingPlanResourceForecastDataRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    import capo_auto_scaling_plans.types.service_namespace

    out["ServiceNamespace"] = (
        capo_auto_scaling_plans.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_auto_scaling_plans.types.scalable_dimension

    out["ScalableDimension"] = (
        capo_auto_scaling_plans.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    import capo_auto_scaling_plans.types.forecast_data_type

    out["ForecastDataType"] = (
        capo_auto_scaling_plans.types.forecast_data_type.serialize_aws_json_1_1(
            value["forecast_data_type"]
        )
    )
    import capo_auto_scaling_plans.types.timestamp_type

    out["StartTime"] = (
        capo_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
            value["start_time"]
        )
    )
    import capo_auto_scaling_plans.types.timestamp_type

    out["EndTime"] = (
        capo_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
            value["end_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScalingPlanResourceForecastDataRequest:
    out: GetScalingPlanResourceForecastDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        out["scaling_plan_name"] = ""
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        out["scaling_plan_version"] = 0
    if data.get("ServiceNamespace") is not None:
        import capo_auto_scaling_plans.types.service_namespace

        out["service_namespace"] = (
            capo_auto_scaling_plans.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        import typing

        out["service_namespace"] = typing.cast(
            "capo_auto_scaling_plans.types.service_namespace.ServiceNamespace", ""
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ScalableDimension") is not None:
        import capo_auto_scaling_plans.types.scalable_dimension

        out["scalable_dimension"] = (
            capo_auto_scaling_plans.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        import typing

        out["scalable_dimension"] = typing.cast(
            "capo_auto_scaling_plans.types.scalable_dimension.ScalableDimension", ""
        )
    if data.get("ForecastDataType") is not None:
        import capo_auto_scaling_plans.types.forecast_data_type

        out["forecast_data_type"] = (
            capo_auto_scaling_plans.types.forecast_data_type.deserialize_aws_json_1_1(
                data["ForecastDataType"]
            )
        )
    else:
        import typing

        out["forecast_data_type"] = typing.cast(
            "capo_auto_scaling_plans.types.forecast_data_type.ForecastDataType", ""
        )
    if data.get("StartTime") is not None:
        import capo_auto_scaling_plans.types.timestamp_type

        out["start_time"] = (
            capo_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_auto_scaling_plans.types.timestamp_type

        out["end_time"] = (
            capo_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
