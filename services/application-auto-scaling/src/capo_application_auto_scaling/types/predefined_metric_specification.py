"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredefinedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_type
    import capo_application_auto_scaling.types.resource_label


class PredefinedMetricSpecification(TypedDict, closed=True):
    predefined_metric_type: "capo_application_auto_scaling.types.metric_type.MetricType"
    """<p>The metric type. The following are notes about specific metric types:</p> <ul> <li> <p> <code>ALBRequestCountPerTarget</code> - This metric type applies only to Spot Fleets and ECS services.</p> </li> <li> <p> <code>ECSServiceAverageCPUUtilizationHighResolution</code> - The high-resolution version of <code>ECSServiceAverageCPUUtilization</code> that uses 20-second CloudWatch metrics. Use this metric for target tracking scaling policies that evaluate metrics every 20 seconds. You must enable high-resolution metrics in Amazon ECS before creating a scaling policy with this metric type.</p> </li> <li> <p> <code>ECSServiceAverageMemoryUtilizationHighResolution</code> - The high-resolution version of <code>ECSServiceAverageMemoryUtilization</code> that uses 20-second CloudWatch metrics. Use this metric for target tracking scaling policies that evaluate metrics every 20 seconds. You must enable high-resolution metrics in Amazon ECS before creating a scaling policy with this metric type.</p> </li> </ul>"""
    resource_label: NotRequired[
        "capo_application_auto_scaling.types.resource_label.ResourceLabel"
    ]
    """<p>Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is <code>ALBRequestCountPerTarget</code> and there is a target group attached to the Spot Fleet or ECS service.</p> <p>You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:</p> <p> <code>app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff</code>.</p> <p>Where:</p> <ul> <li> <p>app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN</p> </li> <li> <p>targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.</p> </li> </ul> <p>To find the ARN for an Application Load Balancer, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API operation. To find the ARN for the target group, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredefinedMetricSpecification) -> dict:
    out: dict = {}
    import capo_application_auto_scaling.types.metric_type

    out["PredefinedMetricType"] = (
        capo_application_auto_scaling.types.metric_type.serialize_aws_json_1_1(
            value["predefined_metric_type"]
        )
    )
    if "resource_label" in value:
        out["ResourceLabel"] = value["resource_label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredefinedMetricSpecification:
    out: PredefinedMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("PredefinedMetricType") is not None:
        import capo_application_auto_scaling.types.metric_type

        out["predefined_metric_type"] = (
            capo_application_auto_scaling.types.metric_type.deserialize_aws_json_1_1(
                data["PredefinedMetricType"]
            )
        )
    else:
        raise DeserializationError(
            "PredefinedMetricSpecification.predefined_metric_type required"
        )
    if data.get("ResourceLabel") is not None:
        out["resource_label"] = data["ResourceLabel"]
    return out
