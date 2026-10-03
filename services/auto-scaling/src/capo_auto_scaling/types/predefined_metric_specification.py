"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredefinedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_type
    import capo_auto_scaling.types.xml_string_max_len1023


class PredefinedMetricSpecification(TypedDict, closed=True):
    predefined_metric_type: NotRequired[
        "capo_auto_scaling.types.metric_type.MetricType"
    ]
    """<p>The metric type. The following predefined metrics are available:</p> <ul> <li> <p> <code>ASGAverageCPUUtilization</code> - Average CPU utilization of the Auto Scaling group.</p> </li> <li> <p> <code>ASGAverageNetworkIn</code> - Average number of bytes received on all network interfaces by the Auto Scaling group.</p> </li> <li> <p> <code>ASGAverageNetworkOut</code> - Average number of bytes sent out on all network interfaces by the Auto Scaling group.</p> </li> <li> <p> <code>ALBRequestCountPerTarget</code> - Average Application Load Balancer request count per target for your Auto Scaling group.</p> </li> </ul>"""
    resource_label: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len1023.XmlStringMaxLen1023"
    ]
    """<p>A label that uniquely identifies a specific Application Load Balancer target group from which to determine the average request count served by your Auto Scaling group. You can't specify a resource label unless the target group is attached to the Auto Scaling group.</p> <p>You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:</p> <p> <code>app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff</code>.</p> <p>Where:</p> <ul> <li> <p>app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN</p> </li> <li> <p>targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.</p> </li> </ul> <p>To find the ARN for an Application Load Balancer, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API operation. To find the ARN for the target group, use the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> API operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PredefinedMetricSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "predefined_metric_type" in value:
        import capo_auto_scaling.types.metric_type

        capo_auto_scaling.types.metric_type.serialize_query(
            value["predefined_metric_type"], pairs, f"{key_prefix}PredefinedMetricType"
        )
    if "resource_label" in value:
        pairs.append((f"{key_prefix}ResourceLabel", str(value["resource_label"])))


def deserialize_query(el: Element) -> PredefinedMetricSpecification:
    out: PredefinedMetricSpecification = {}  # type: ignore[typeddict-item]
    child_predefined_metric_type = el.find("PredefinedMetricType")
    if child_predefined_metric_type is not None:
        import capo_auto_scaling.types.metric_type

        out["predefined_metric_type"] = (
            capo_auto_scaling.types.metric_type.deserialize_query(
                child_predefined_metric_type
            )
        )
    child_resource_label = el.find("ResourceLabel")
    if child_resource_label is not None:
        out["resource_label"] = str(child_resource_label.text or "")
    return out
