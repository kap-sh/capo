"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalySubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_subscription_frequency
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.monitor_arn_list
    import capo_cost_explorer.types.nullable_non_negative_double
    import capo_cost_explorer.types.subscribers


class AnomalySubscription(TypedDict, closed=True):
    subscription_arn: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The <code>AnomalySubscription</code> Amazon Resource Name (ARN). </p>"""
    account_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>Your unique account identifier. </p>"""
    monitor_arn_list: "capo_cost_explorer.types.monitor_arn_list.MonitorArnList"
    """<p>A list of cost anomaly monitors. </p>"""
    subscribers: "capo_cost_explorer.types.subscribers.Subscribers"
    """<p>A list of subscribers to notify. </p>"""
    threshold: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>(deprecated)</p> <p>An absolute dollar value that must be exceeded by the anomaly's total impact (see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html">Impact</a> for more details) for an anomaly notification to be generated.</p> <p>This field has been deprecated. To specify a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.</p> <p>One of Threshold or ThresholdExpression is required for this resource. You cannot specify both.</p>"""
    frequency: "capo_cost_explorer.types.anomaly_subscription_frequency.AnomalySubscriptionFrequency"
    """<p>The frequency that anomaly notifications are sent. Notifications are sent either over email (for DAILY and WEEKLY frequencies) or SNS (for IMMEDIATE frequency). For more information, see <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/ad-SNS.html">Creating an Amazon SNS topic for anomaly notifications</a>.</p>"""
    subscription_name: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The name for the subscription. </p>"""
    threshold_expression: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>An <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are <code>ANOMALY_TOTAL_IMPACT_ABSOLUTE</code> and <code>ANOMALY_TOTAL_IMPACT_PERCENTAGE</code>, corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html">Impact</a> for more details). The supported nested expression types are <code>AND</code> and <code>OR</code>. The match option <code>GREATER_THAN_OR_EQUAL</code> is required. Values must be numbers between 0 and 10,000,000,000 in string format.</p> <p>One of Threshold or ThresholdExpression is required for this resource. You cannot specify both.</p> <p>The following are examples of valid ThresholdExpressions:</p> <ul> <li> <p>Absolute threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p>Percentage threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p> <code>AND</code> two thresholds together: <code>{ "And": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> <li> <p> <code>OR</code> two thresholds together: <code>{ "Or": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalySubscription) -> dict:
    out: dict = {}
    if "subscription_arn" in value:
        out["SubscriptionArn"] = value["subscription_arn"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    import capo_cost_explorer.types.monitor_arn_list

    out["MonitorArnList"] = (
        capo_cost_explorer.types.monitor_arn_list.serialize_aws_json_1_1(
            value["monitor_arn_list"]
        )
    )
    import capo_cost_explorer.types.subscribers

    out["Subscribers"] = capo_cost_explorer.types.subscribers.serialize_aws_json_1_1(
        value["subscribers"]
    )
    if "threshold" in value:
        out["Threshold"] = (
            "NaN"
            if value["threshold"] != value["threshold"]
            else "Infinity"
            if value["threshold"] == float("inf")
            else "-Infinity"
            if value["threshold"] == float("-inf")
            else value["threshold"]
        )
    import capo_cost_explorer.types.anomaly_subscription_frequency

    out["Frequency"] = (
        capo_cost_explorer.types.anomaly_subscription_frequency.serialize_aws_json_1_1(
            value["frequency"]
        )
    )
    out["SubscriptionName"] = value["subscription_name"]
    if "threshold_expression" in value:
        import capo_cost_explorer.types.expression

        out["ThresholdExpression"] = (
            capo_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["threshold_expression"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalySubscription:
    out: AnomalySubscription = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("MonitorArnList") is not None:
        import capo_cost_explorer.types.monitor_arn_list

        out["monitor_arn_list"] = (
            capo_cost_explorer.types.monitor_arn_list.deserialize_aws_json_1_1(
                data["MonitorArnList"]
            )
        )
    else:
        raise DeserializationError("AnomalySubscription.monitor_arn_list required")
    if data.get("Subscribers") is not None:
        import capo_cost_explorer.types.subscribers

        out["subscribers"] = (
            capo_cost_explorer.types.subscribers.deserialize_aws_json_1_1(
                data["Subscribers"]
            )
        )
    else:
        raise DeserializationError("AnomalySubscription.subscribers required")
    if data.get("Threshold") is not None:
        out["threshold"] = float(data["Threshold"])
    if data.get("Frequency") is not None:
        import capo_cost_explorer.types.anomaly_subscription_frequency

        out["frequency"] = (
            capo_cost_explorer.types.anomaly_subscription_frequency.deserialize_aws_json_1_1(
                data["Frequency"]
            )
        )
    else:
        raise DeserializationError("AnomalySubscription.frequency required")
    if data.get("SubscriptionName") is not None:
        out["subscription_name"] = data["SubscriptionName"]
    else:
        raise DeserializationError("AnomalySubscription.subscription_name required")
    if data.get("ThresholdExpression") is not None:
        import capo_cost_explorer.types.expression

        out["threshold_expression"] = (
            capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["ThresholdExpression"]
            )
        )
    return out
