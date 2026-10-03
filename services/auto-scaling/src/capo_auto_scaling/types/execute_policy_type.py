"""Generated from Smithy shape ``com.amazonaws.autoscaling#ExecutePolicyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.honor_cooldown
    import capo_auto_scaling.types.metric_scale
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.xml_string_max_len255


class ExecutePolicyType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_name: NotRequired["capo_auto_scaling.types.resource_name.ResourceName"]
    """<p>The name or ARN of the policy.</p>"""
    honor_cooldown: NotRequired["capo_auto_scaling.types.honor_cooldown.HonorCooldown"]
    """<p>Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy.</p> <p>Valid only if the policy type is <code>SimpleScaling</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    metric_value: NotRequired["capo_auto_scaling.types.metric_scale.MetricScale"]
    """<p>The metric value to compare to <code>BreachThreshold</code>. This enables you to execute a policy of type <code>StepScaling</code> and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.</p> <p>If you specify a metric value that doesn't correspond to a step adjustment for the policy, the call returns an error.</p> <p>Required if the policy type is <code>StepScaling</code> and not supported otherwise.</p>"""
    breach_threshold: NotRequired["capo_auto_scaling.types.metric_scale.MetricScale"]
    """<p>The breach threshold for the alarm.</p> <p>Required if the policy type is <code>StepScaling</code> and not supported otherwise.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExecutePolicyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_name" in value:
        pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "honor_cooldown" in value:
        pairs.append(
            (
                f"{key_prefix}HonorCooldown",
                "true" if value["honor_cooldown"] else "false",
            )
        )
    if "metric_value" in value:
        pairs.append(
            (
                f"{key_prefix}MetricValue",
                (
                    "NaN"
                    if value["metric_value"] != value["metric_value"]
                    else "Infinity"
                    if value["metric_value"] == float("inf")
                    else "-Infinity"
                    if value["metric_value"] == float("-inf")
                    else str(value["metric_value"])
                ),
            )
        )
    if "breach_threshold" in value:
        pairs.append(
            (
                f"{key_prefix}BreachThreshold",
                (
                    "NaN"
                    if value["breach_threshold"] != value["breach_threshold"]
                    else "Infinity"
                    if value["breach_threshold"] == float("inf")
                    else "-Infinity"
                    if value["breach_threshold"] == float("-inf")
                    else str(value["breach_threshold"])
                ),
            )
        )


def deserialize_query(el: Element) -> ExecutePolicyType:
    out: ExecutePolicyType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_honor_cooldown = el.find("HonorCooldown")
    if child_honor_cooldown is not None:
        out["honor_cooldown"] = (child_honor_cooldown.text or "").lower() == "true"
    child_metric_value = el.find("MetricValue")
    if child_metric_value is not None:
        out["metric_value"] = float(child_metric_value.text or "")
    child_breach_threshold = el.find("BreachThreshold")
    if child_breach_threshold is not None:
        out["breach_threshold"] = float(child_breach_threshold.text or "")
    return out
