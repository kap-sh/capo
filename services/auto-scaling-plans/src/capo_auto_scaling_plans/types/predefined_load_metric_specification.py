"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PredefinedLoadMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.load_metric_type
    import capo_auto_scaling_plans.types.resource_label


class PredefinedLoadMetricSpecification(TypedDict, closed=True):
    predefined_load_metric_type: (
        "capo_auto_scaling_plans.types.load_metric_type.LoadMetricType"
    )
    """<p>The metric type.</p>"""
    resource_label: NotRequired[
        "capo_auto_scaling_plans.types.resource_label.ResourceLabel"
    ]
    """<p>Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is <code>ALBTargetGroupRequestCount</code> and there is a target group for an Application Load Balancer attached to the Auto Scaling group.</p> <p>You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:</p> <ul> <li> <p>app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN</p> </li> <li> <p>targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.</p> </li> </ul> <p>This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.</p> <p>To find the ARN for an Application Load Balancer, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API operation. To find the ARN for the target group, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredefinedLoadMetricSpecification) -> dict:
    out: dict = {}
    import capo_auto_scaling_plans.types.load_metric_type

    out["PredefinedLoadMetricType"] = (
        capo_auto_scaling_plans.types.load_metric_type.serialize_aws_json_1_1(
            value["predefined_load_metric_type"]
        )
    )
    if "resource_label" in value:
        out["ResourceLabel"] = value["resource_label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredefinedLoadMetricSpecification:
    out: PredefinedLoadMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("PredefinedLoadMetricType") is not None:
        import capo_auto_scaling_plans.types.load_metric_type

        out["predefined_load_metric_type"] = (
            capo_auto_scaling_plans.types.load_metric_type.deserialize_aws_json_1_1(
                data["PredefinedLoadMetricType"]
            )
        )
    else:
        raise DeserializationError(
            "PredefinedLoadMetricSpecification.predefined_load_metric_type required"
        )
    if data.get("ResourceLabel") is not None:
        out["resource_label"] = data["ResourceLabel"]
    return out
