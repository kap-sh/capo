"""Generated from Smithy shape ``com.amazonaws.gamelift#PutScalingPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.comparison_operator_type
    import capo_gamelift.types.double
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.integer
    import capo_gamelift.types.metric_name
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.policy_type
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.scaling_adjustment_type
    import capo_gamelift.types.target_configuration


class PutScalingPolicyInput(TypedDict, closed=True):
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.</p>"""
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.</p>"""
    scaling_adjustment: NotRequired["capo_gamelift.types.integer.Integer"]
    """<p>Amount of adjustment to make, based on the scaling adjustment type.</p>"""
    scaling_adjustment_type: NotRequired[
        "capo_gamelift.types.scaling_adjustment_type.ScalingAdjustmentType"
    ]
    """<p>The type of adjustment to make to a fleet's instance count:</p> <ul> <li> <p> <b>ChangeInCapacity</b> -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.</p> </li> <li> <p> <b>ExactCapacity</b> -- set the instance count to the scaling adjustment value.</p> </li> <li> <p> <b>PercentChangeInCapacity</b> -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.</p> </li> </ul>"""
    threshold: NotRequired["capo_gamelift.types.double.Double"]
    """<p>Metric value used to trigger a scaling event.</p>"""
    comparison_operator: NotRequired[
        "capo_gamelift.types.comparison_operator_type.ComparisonOperatorType"
    ]
    """<p>Comparison operator to use when measuring the metric against the threshold value.</p>"""
    evaluation_periods: NotRequired[
        "capo_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.</p>"""
    metric_name: NotRequired["capo_gamelift.types.metric_name.MetricName"]
    """<p>Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html">Monitor Amazon GameLift Servers with Amazon CloudWatch</a>. </p> <ul> <li> <p> <b>ActivatingGameSessions</b> -- Game sessions in the process of being created.</p> </li> <li> <p> <b>ActiveGameSessions</b> -- Game sessions that are currently running.</p> </li> <li> <p> <b>ActiveInstances</b> -- Fleet instances that are currently running at least one game session.</p> </li> <li> <p> <b>AvailableGameSessions</b> -- Additional game sessions that a fleet could host simultaneously, given current capacity.</p> </li> <li> <p> <b>AvailablePlayerSessions</b> -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.</p> </li> <li> <p> <b>CurrentPlayerSessions</b> -- Player slots in active game sessions that are being used by a player or are reserved for a player. </p> </li> <li> <p> <b>IdleInstances</b> -- Active instances that are currently hosting zero game sessions. </p> </li> <li> <p> <b>PercentAvailableGameSessions</b> -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.</p> </li> <li> <p> <b>PercentIdleInstances</b> -- Percentage of the total number of active instances that are hosting zero game sessions.</p> </li> <li> <p> <b>QueueDepth</b> -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.</p> </li> <li> <p> <b>WaitTime</b> -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination. </p> </li> </ul>"""
    policy_type: NotRequired["capo_gamelift.types.policy_type.PolicyType"]
    """<p>The type of scaling policy to create. For a target-based policy, set the parameter <i>MetricName</i> to 'PercentAvailableGameSessions' and specify a <i>TargetConfiguration</i>. For a rule-based policy set the following parameters: <i>MetricName</i>, <i>ComparisonOperator</i>, <i>Threshold</i>, <i>EvaluationPeriods</i>, <i>ScalingAdjustmentType</i>, and <i>ScalingAdjustment</i>.</p>"""
    target_configuration: NotRequired[
        "capo_gamelift.types.target_configuration.TargetConfiguration"
    ]
    """<p>An object that contains settings for a target-based scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScalingPolicyInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "scaling_adjustment" in value:
        out["ScalingAdjustment"] = value["scaling_adjustment"]
    if "scaling_adjustment_type" in value:
        import capo_gamelift.types.scaling_adjustment_type

        out["ScalingAdjustmentType"] = (
            capo_gamelift.types.scaling_adjustment_type.serialize_aws_json_1_1(
                value["scaling_adjustment_type"]
            )
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
    if "comparison_operator" in value:
        import capo_gamelift.types.comparison_operator_type

        out["ComparisonOperator"] = (
            capo_gamelift.types.comparison_operator_type.serialize_aws_json_1_1(
                value["comparison_operator"]
            )
        )
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "metric_name" in value:
        import capo_gamelift.types.metric_name

        out["MetricName"] = capo_gamelift.types.metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    if "policy_type" in value:
        import capo_gamelift.types.policy_type

        out["PolicyType"] = capo_gamelift.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    if "target_configuration" in value:
        import capo_gamelift.types.target_configuration

        out["TargetConfiguration"] = (
            capo_gamelift.types.target_configuration.serialize_aws_json_1_1(
                value["target_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutScalingPolicyInput:
    out: PutScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ScalingAdjustment") is not None:
        out["scaling_adjustment"] = data["ScalingAdjustment"]
    if data.get("ScalingAdjustmentType") is not None:
        import capo_gamelift.types.scaling_adjustment_type

        out["scaling_adjustment_type"] = (
            capo_gamelift.types.scaling_adjustment_type.deserialize_aws_json_1_1(
                data["ScalingAdjustmentType"]
            )
        )
    if data.get("Threshold") is not None:
        out["threshold"] = float(data["Threshold"])
    if data.get("ComparisonOperator") is not None:
        import capo_gamelift.types.comparison_operator_type

        out["comparison_operator"] = (
            capo_gamelift.types.comparison_operator_type.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    if data.get("EvaluationPeriods") is not None:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if data.get("MetricName") is not None:
        import capo_gamelift.types.metric_name

        out["metric_name"] = capo_gamelift.types.metric_name.deserialize_aws_json_1_1(
            data["MetricName"]
        )
    if data.get("PolicyType") is not None:
        import capo_gamelift.types.policy_type

        out["policy_type"] = capo_gamelift.types.policy_type.deserialize_aws_json_1_1(
            data["PolicyType"]
        )
    if data.get("TargetConfiguration") is not None:
        import capo_gamelift.types.target_configuration

        out["target_configuration"] = (
            capo_gamelift.types.target_configuration.deserialize_aws_json_1_1(
                data["TargetConfiguration"]
            )
        )
    return out
