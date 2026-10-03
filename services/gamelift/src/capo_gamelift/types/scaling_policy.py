"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.comparison_operator_type
    import capo_gamelift.types.double
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.integer
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.location_update_status
    import capo_gamelift.types.metric_name
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.policy_type
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.scaling_adjustment_type
    import capo_gamelift.types.scaling_status_type
    import capo_gamelift.types.target_configuration


class ScalingPolicy(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that is associated with this scaling policy.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.</p>"""
    status: NotRequired["capo_gamelift.types.scaling_status_type.ScalingStatusType"]
    """<p>Current status of the scaling policy. The scaling policy can be in force only when in an <code>ACTIVE</code> status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.</p> <ul> <li> <p> <b>ACTIVE</b> -- The scaling policy can be used for auto-scaling a fleet.</p> </li> <li> <p> <b>UPDATE_REQUESTED</b> -- A request to update the scaling policy has been received.</p> </li> <li> <p> <b>UPDATING</b> -- A change is being made to the scaling policy.</p> </li> <li> <p> <b>DELETE_REQUESTED</b> -- A request to delete the scaling policy has been received.</p> </li> <li> <p> <b>DELETING</b> -- The scaling policy is being deleted.</p> </li> <li> <p> <b>DELETED</b> -- The scaling policy has been deleted.</p> </li> <li> <p> <b>ERROR</b> -- An error occurred in creating the policy. It should be removed and recreated.</p> </li> </ul>"""
    scaling_adjustment: NotRequired["capo_gamelift.types.integer.Integer"]
    """<p>Amount of adjustment to make, based on the scaling adjustment type.</p>"""
    scaling_adjustment_type: NotRequired[
        "capo_gamelift.types.scaling_adjustment_type.ScalingAdjustmentType"
    ]
    """<p>The type of adjustment to make to a fleet's instance count.</p> <ul> <li> <p> <b>ChangeInCapacity</b> -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.</p> </li> <li> <p> <b>ExactCapacity</b> -- set the instance count to the scaling adjustment value.</p> </li> <li> <p> <b>PercentChangeInCapacity</b> -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.</p> </li> </ul>"""
    comparison_operator: NotRequired[
        "capo_gamelift.types.comparison_operator_type.ComparisonOperatorType"
    ]
    """<p>Comparison operator to use when measuring a metric against the threshold value.</p>"""
    threshold: NotRequired["capo_gamelift.types.double.Double"]
    """<p>Metric value used to trigger a scaling event.</p>"""
    evaluation_periods: NotRequired[
        "capo_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.</p>"""
    metric_name: NotRequired["capo_gamelift.types.metric_name.MetricName"]
    """<p>Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html">Monitor Amazon GameLift Servers with Amazon CloudWatch</a>. </p> <ul> <li> <p> <b>ActivatingGameSessions</b> -- Game sessions in the process of being created.</p> </li> <li> <p> <b>ActiveGameSessions</b> -- Game sessions that are currently running.</p> </li> <li> <p> <b>ActiveInstances</b> -- Fleet instances that are currently running at least one game session.</p> </li> <li> <p> <b>AvailableGameSessions</b> -- Additional game sessions that fleet could host simultaneously, given current capacity.</p> </li> <li> <p> <b>AvailablePlayerSessions</b> -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.</p> </li> <li> <p> <b>CurrentPlayerSessions</b> -- Player slots in active game sessions that are being used by a player or are reserved for a player. </p> </li> <li> <p> <b>IdleInstances</b> -- Active instances that are currently hosting zero game sessions. </p> </li> <li> <p> <b>PercentAvailableGameSessions</b> -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.</p> </li> <li> <p> <b>PercentIdleInstances</b> -- Percentage of the total number of active instances that are hosting zero game sessions.</p> </li> <li> <p> <b>QueueDepth</b> -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.</p> </li> <li> <p> <b>WaitTime</b> -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination. </p> </li> </ul>"""
    policy_type: NotRequired["capo_gamelift.types.policy_type.PolicyType"]
    """<p>The type of scaling policy to create. For a target-based policy, set the parameter <i>MetricName</i> to 'PercentAvailableGameSessions' and specify a <i>TargetConfiguration</i>. For a rule-based policy set the following parameters: <i>MetricName</i>, <i>ComparisonOperator</i>, <i>Threshold</i>, <i>EvaluationPeriods</i>, <i>ScalingAdjustmentType</i>, and <i>ScalingAdjustment</i>.</p>"""
    target_configuration: NotRequired[
        "capo_gamelift.types.target_configuration.TargetConfiguration"
    ]
    """<p>An object that contains settings for a target-based scaling policy.</p>"""
    update_status: NotRequired[
        "capo_gamelift.types.location_update_status.LocationUpdateStatus"
    ]
    """<p>The current status of the fleet's scaling policies in a requested fleet location. The status <code>PENDING_UPDATE</code> indicates that an update was requested for the fleet but has not yet been completed for the location.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p> The fleet location. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicy) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_gamelift.types.scaling_status_type

        out["Status"] = capo_gamelift.types.scaling_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "scaling_adjustment" in value:
        out["ScalingAdjustment"] = value["scaling_adjustment"]
    if "scaling_adjustment_type" in value:
        import capo_gamelift.types.scaling_adjustment_type

        out["ScalingAdjustmentType"] = (
            capo_gamelift.types.scaling_adjustment_type.serialize_aws_json_1_1(
                value["scaling_adjustment_type"]
            )
        )
    if "comparison_operator" in value:
        import capo_gamelift.types.comparison_operator_type

        out["ComparisonOperator"] = (
            capo_gamelift.types.comparison_operator_type.serialize_aws_json_1_1(
                value["comparison_operator"]
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
    if "update_status" in value:
        import capo_gamelift.types.location_update_status

        out["UpdateStatus"] = (
            capo_gamelift.types.location_update_status.serialize_aws_json_1_1(
                value["update_status"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicy:
    out: ScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_gamelift.types.scaling_status_type

        out["status"] = (
            capo_gamelift.types.scaling_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ScalingAdjustment") is not None:
        out["scaling_adjustment"] = data["ScalingAdjustment"]
    if data.get("ScalingAdjustmentType") is not None:
        import capo_gamelift.types.scaling_adjustment_type

        out["scaling_adjustment_type"] = (
            capo_gamelift.types.scaling_adjustment_type.deserialize_aws_json_1_1(
                data["ScalingAdjustmentType"]
            )
        )
    if data.get("ComparisonOperator") is not None:
        import capo_gamelift.types.comparison_operator_type

        out["comparison_operator"] = (
            capo_gamelift.types.comparison_operator_type.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    if data.get("Threshold") is not None:
        out["threshold"] = float(data["Threshold"])
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
    if data.get("UpdateStatus") is not None:
        import capo_gamelift.types.location_update_status

        out["update_status"] = (
            capo_gamelift.types.location_update_status.deserialize_aws_json_1_1(
                data["UpdateStatus"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
