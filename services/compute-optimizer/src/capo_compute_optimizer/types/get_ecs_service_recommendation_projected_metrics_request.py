"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetECSServiceRecommendationProjectedMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_statistic
    import capo_compute_optimizer.types.period
    import capo_compute_optimizer.types.service_arn
    import capo_compute_optimizer.types.timestamp


class GetECSServiceRecommendationProjectedMetricsRequest(TypedDict, closed=True):
    service_arn: "capo_compute_optimizer.types.service_arn.ServiceArn"
    """<p> The ARN that identifies the Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>"""
    stat: "capo_compute_optimizer.types.metric_statistic.MetricStatistic"
    """<p> The statistic of the projected metrics. </p>"""
    period: "capo_compute_optimizer.types.period.Period"
    """<p> The granularity, in seconds, of the projected metrics data points. </p>"""
    start_time: "capo_compute_optimizer.types.timestamp.Timestamp"
    """<p> The timestamp of the first projected metrics data point to return. </p>"""
    end_time: "capo_compute_optimizer.types.timestamp.Timestamp"
    """<p> The timestamp of the last projected metrics data point to return. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetECSServiceRecommendationProjectedMetricsRequest,
) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
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
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetECSServiceRecommendationProjectedMetricsRequest:
    out: GetECSServiceRecommendationProjectedMetricsRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "GetECSServiceRecommendationProjectedMetricsRequest.service_arn required"
        )
    if data.get("stat") is not None:
        import capo_compute_optimizer.types.metric_statistic

        out["stat"] = (
            capo_compute_optimizer.types.metric_statistic.deserialize_aws_json_1_0(
                data["stat"]
            )
        )
    else:
        raise DeserializationError(
            "GetECSServiceRecommendationProjectedMetricsRequest.stat required"
        )
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        raise DeserializationError(
            "GetECSServiceRecommendationProjectedMetricsRequest.period required"
        )
    if data.get("startTime") is not None:
        import capo_compute_optimizer.types.timestamp

        out["start_time"] = (
            capo_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetECSServiceRecommendationProjectedMetricsRequest.start_time required"
        )
    if data.get("endTime") is not None:
        import capo_compute_optimizer.types.timestamp

        out["end_time"] = (
            capo_compute_optimizer.types.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetECSServiceRecommendationProjectedMetricsRequest.end_time required"
        )
    return out
