"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRDSDatabaseRecommendationProjectedMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_statistic
    import capo_compute_optimizer.types.period
    import capo_compute_optimizer.types.recommendation_preferences
    import capo_compute_optimizer.types.resource_arn
    import capo_compute_optimizer.types.timestamp


class GetRDSDatabaseRecommendationProjectedMetricsRequest(TypedDict, closed=True):
    resource_arn: "capo_compute_optimizer.types.resource_arn.ResourceArn"
    """<p> The ARN that identifies the Amazon Aurora or RDS database. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:db:{resourceName}</code> </p>"""
    stat: "capo_compute_optimizer.types.metric_statistic.MetricStatistic"
    """<p> The statistic of the projected metrics. </p>"""
    period: "capo_compute_optimizer.types.period.Period"
    """<p> The granularity, in seconds, of the projected metrics data points. </p>"""
    start_time: "capo_compute_optimizer.types.timestamp.Timestamp"
    """<p> The timestamp of the first projected metrics data point to return. </p>"""
    end_time: "capo_compute_optimizer.types.timestamp.Timestamp"
    """<p> The timestamp of the last projected metrics data point to return. </p>"""
    recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetRDSDatabaseRecommendationProjectedMetricsRequest,
) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_compute_optimizer.types.metric_statistic

    out["stat"] = capo_compute_optimizer.types.metric_statistic.serialize_aws_json_1_0(
        value["stat"]
    )
    out["period"] = value["period"]
    import capo_compute_optimizer.types.timestamp

    out["startTime"] = capo_compute_optimizer.types.timestamp.serialize_aws_json_1_0(
        value["start_time"]
    )
    import capo_compute_optimizer.types.timestamp

    out["endTime"] = capo_compute_optimizer.types.timestamp.serialize_aws_json_1_0(
        value["end_time"]
    )
    if "recommendation_preferences" in value:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetRDSDatabaseRecommendationProjectedMetricsRequest:
    out: GetRDSDatabaseRecommendationProjectedMetricsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("stat") is not None:
        import capo_compute_optimizer.types.metric_statistic

        out["stat"] = (
            capo_compute_optimizer.types.metric_statistic.deserialize_aws_json_1_0(
                data["stat"]
            )
        )
    else:
        import typing

        out["stat"] = typing.cast(
            "capo_compute_optimizer.types.metric_statistic.MetricStatistic", ""
        )
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        out["period"] = 0
    if data.get("startTime") is not None:
        import capo_compute_optimizer.types.timestamp

        out["start_time"] = (
            capo_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_compute_optimizer.types.timestamp

        out["end_time"] = (
            capo_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("recommendationPreferences") is not None:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out
