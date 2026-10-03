"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalySubscriptionRequest``."""

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


class UpdateAnomalySubscriptionRequest(TypedDict, closed=True):
    subscription_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly subscription Amazon Resource Name (ARN). </p>"""
    threshold: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>(deprecated)</p> <p>The update to the threshold value for receiving notifications. </p> <p>This field has been deprecated. To update a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p>"""
    frequency: NotRequired[
        "capo_cost_explorer.types.anomaly_subscription_frequency.AnomalySubscriptionFrequency"
    ]
    """<p>The update to the frequency value that subscribers receive notifications. </p>"""
    monitor_arn_list: NotRequired[
        "capo_cost_explorer.types.monitor_arn_list.MonitorArnList"
    ]
    """<p>A list of cost anomaly monitor ARNs. </p>"""
    subscribers: NotRequired["capo_cost_explorer.types.subscribers.Subscribers"]
    """<p>The update to the subscriber list. </p>"""
    subscription_name: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The new name of the subscription. </p>"""
    threshold_expression: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>The update to the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are <code>ANOMALY_TOTAL_IMPACT_ABSOLUTE</code> and <code>ANOMALY_TOTAL_IMPACT_PERCENTAGE</code>, corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html">Impact</a> for more details). The supported nested expression types are <code>AND</code> and <code>OR</code>. The match option <code>GREATER_THAN_OR_EQUAL</code> is required. Values must be numbers between 0 and 10,000,000,000 in string format.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p> <p>The following are examples of valid ThresholdExpressions:</p> <ul> <li> <p>Absolute threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p>Percentage threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p> <code>AND</code> two thresholds together: <code>{ "And": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> <li> <p> <code>OR</code> two thresholds together: <code>{ "Or": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalySubscriptionRequest) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
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
    if "frequency" in value:
        import capo_cost_explorer.types.anomaly_subscription_frequency

        out["Frequency"] = (
            capo_cost_explorer.types.anomaly_subscription_frequency.serialize_aws_json_1_1(
                value["frequency"]
            )
        )
    if "monitor_arn_list" in value:
        import capo_cost_explorer.types.monitor_arn_list

        out["MonitorArnList"] = (
            capo_cost_explorer.types.monitor_arn_list.serialize_aws_json_1_1(
                value["monitor_arn_list"]
            )
        )
    if "subscribers" in value:
        import capo_cost_explorer.types.subscribers

        out["Subscribers"] = (
            capo_cost_explorer.types.subscribers.serialize_aws_json_1_1(
                value["subscribers"]
            )
        )
    if "subscription_name" in value:
        out["SubscriptionName"] = value["subscription_name"]
    if "threshold_expression" in value:
        import capo_cost_explorer.types.expression

        out["ThresholdExpression"] = (
            capo_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["threshold_expression"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalySubscriptionRequest:
    out: UpdateAnomalySubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionArn") is not None:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        raise DeserializationError(
            "UpdateAnomalySubscriptionRequest.subscription_arn required"
        )
    if data.get("Threshold") is not None:
        out["threshold"] = float(data["Threshold"])
    if data.get("Frequency") is not None:
        import capo_cost_explorer.types.anomaly_subscription_frequency

        out["frequency"] = (
            capo_cost_explorer.types.anomaly_subscription_frequency.deserialize_aws_json_1_1(
                data["Frequency"]
            )
        )
    if data.get("MonitorArnList") is not None:
        import capo_cost_explorer.types.monitor_arn_list

        out["monitor_arn_list"] = (
            capo_cost_explorer.types.monitor_arn_list.deserialize_aws_json_1_1(
                data["MonitorArnList"]
            )
        )
    if data.get("Subscribers") is not None:
        import capo_cost_explorer.types.subscribers

        out["subscribers"] = (
            capo_cost_explorer.types.subscribers.deserialize_aws_json_1_1(
                data["Subscribers"]
            )
        )
    if data.get("SubscriptionName") is not None:
        out["subscription_name"] = data["SubscriptionName"]
    if data.get("ThresholdExpression") is not None:
        import capo_cost_explorer.types.expression

        out["threshold_expression"] = (
            capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["ThresholdExpression"]
            )
        )
    return out
