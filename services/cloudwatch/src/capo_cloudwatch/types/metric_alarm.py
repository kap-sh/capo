"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricAlarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.alarm_arn
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.comparison_operator
    import capo_cloudwatch.types.datapoints_to_alarm
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.evaluate_low_sample_count_percentile
    import capo_cloudwatch.types.evaluation_criteria
    import capo_cloudwatch.types.evaluation_interval
    import capo_cloudwatch.types.evaluation_periods
    import capo_cloudwatch.types.evaluation_state
    import capo_cloudwatch.types.evaluation_window
    import capo_cloudwatch.types.extended_statistic
    import capo_cloudwatch.types.metric_data_queries
    import capo_cloudwatch.types.metric_id
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.state_reason_data
    import capo_cloudwatch.types.state_value
    import capo_cloudwatch.types.statistic
    import capo_cloudwatch.types.threshold
    import capo_cloudwatch.types.timestamp
    import capo_cloudwatch.types.treat_missing_data
    import capo_cloudwatch.types.warm_up_configuration


class MetricAlarm(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""
    alarm_arn: NotRequired["capo_cloudwatch.types.alarm_arn.AlarmArn"]
    """<p>The Amazon Resource Name (ARN) of the alarm.</p>"""
    alarm_description: NotRequired[
        "capo_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>The description of the alarm.</p>"""
    alarm_configuration_updated_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p>The time stamp of the last update to the alarm configuration.</p>"""
    actions_enabled: NotRequired["capo_cloudwatch.types.actions_enabled.ActionsEnabled"]
    """<p>Indicates whether actions should be executed during any changes to the alarm state.</p>"""
    ok_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    alarm_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    insufficient_data_actions: NotRequired[
        "capo_cloudwatch.types.resource_list.ResourceList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    state_value: NotRequired["capo_cloudwatch.types.state_value.StateValue"]
    """<p>The state value for the alarm.</p>"""
    state_reason: NotRequired["capo_cloudwatch.types.state_reason.StateReason"]
    """<p>An explanation for the alarm state, in text format.</p>"""
    state_reason_data: NotRequired[
        "capo_cloudwatch.types.state_reason_data.StateReasonData"
    ]
    """<p>An explanation for the alarm state, in JSON format.</p>"""
    state_updated_timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp of the last update to the value of either the <code>StateValue</code> or <code>EvaluationState</code> parameters.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric associated with the alarm, if this is an alarm based on a single metric.</p>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric associated with the alarm.</p>"""
    statistic: NotRequired["capo_cloudwatch.types.statistic.Statistic"]
    """<p>The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use <code>ExtendedStatistic</code>.</p>"""
    extended_statistic: NotRequired[
        "capo_cloudwatch.types.extended_statistic.ExtendedStatistic"
    ]
    """<p>The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions for the metric associated with the alarm.</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The period, in seconds, over which the statistic is applied.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The unit of the metric associated with the alarm.</p>"""
    evaluation_periods: NotRequired[
        "capo_cloudwatch.types.evaluation_periods.EvaluationPeriods"
    ]
    """<p>The number of periods over which data is compared to the specified threshold.</p>"""
    datapoints_to_alarm: NotRequired[
        "capo_cloudwatch.types.datapoints_to_alarm.DatapointsToAlarm"
    ]
    """<p>The number of data points that must be breaching to trigger the alarm.</p>"""
    threshold: NotRequired["capo_cloudwatch.types.threshold.Threshold"]
    """<p>The value to compare with the specified statistic.</p>"""
    comparison_operator: NotRequired[
        "capo_cloudwatch.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.</p>"""
    treat_missing_data: NotRequired[
        "capo_cloudwatch.types.treat_missing_data.TreatMissingData"
    ]
    """<p>Sets how this alarm is to handle missing data points. The valid values are <code>breaching</code>, <code>notBreaching</code>, <code>ignore</code>, and <code>missing</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data">Configuring how CloudWatch alarms treat missing data</a>.</p> <p>If this parameter is omitted, the default behavior of <code>missing</code> is used.</p> <note> <p>This parameter is not applicable to PromQL alarms.</p> </note>"""
    evaluate_low_sample_count_percentile: NotRequired[
        "capo_cloudwatch.types.evaluate_low_sample_count_percentile.EvaluateLowSampleCountPercentile"
    ]
    """<p>Used only for alarms based on percentiles. If <code>ignore</code>, the alarm state does not change during periods with too few data points to be statistically significant. If <code>evaluate</code> or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.</p>"""
    metrics: NotRequired["capo_cloudwatch.types.metric_data_queries.MetricDataQueries"]
    """<p>An array of MetricDataQuery structures, used in an alarm based on a metric math expression. Each structure either retrieves a metric or performs a math expression. One item in the Metrics array is the math expression that the alarm watches. This expression by designated by having <code>ReturnData</code> set to true.</p>"""
    threshold_metric_id: NotRequired["capo_cloudwatch.types.metric_id.MetricId"]
    """<p>In an alarm based on an anomaly detection model, this is the ID of the <code>ANOMALY_DETECTION_BAND</code> function used as the threshold for the alarm.</p>"""
    evaluation_state: NotRequired[
        "capo_cloudwatch.types.evaluation_state.EvaluationState"
    ]
    """<p>If the value of this field is <code>PARTIAL_DATA</code>, it indicates that not all the available data was able to be retrieved due to quota limitations. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html">Create alarms on Metrics Insights queries</a>.</p> <p>If the value of this field is <code>EVALUATION_ERROR</code>, it indicates configuration errors in alarm setup that require review and correction. Refer to StateReason field of the alarm for more details.</p> <p>If the value of this field is <code>EVALUATION_FAILURE</code>, it indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved </p>"""
    state_transitioned_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the alarm's <code>StateValue</code> most recently changed.</p>"""
    evaluation_window: NotRequired[
        "capo_cloudwatch.types.evaluation_window.EvaluationWindow"
    ]
    """<p>The evaluation window that the alarm uses to select the range of metric data that it evaluates. This is either a sliding window or a wall clock window. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html">Alarm evaluation windows</a> in the <i>CloudWatch User Guide</i>.</p>"""
    warm_up_configuration: NotRequired[
        "capo_cloudwatch.types.warm_up_configuration.WarmUpConfiguration"
    ]
    """<p>The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. During the warm-up period, the alarm stays in <code>INSUFFICIENT_DATA</code> and does not perform alarm actions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html">Alarm warm-up periods</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""
    evaluation_criteria: NotRequired[
        "capo_cloudwatch.types.evaluation_criteria.EvaluationCriteria"
    ]
    """<p>The evaluation criteria for the alarm.</p>"""
    evaluation_interval: NotRequired[
        "capo_cloudwatch.types.evaluation_interval.EvaluationInterval"
    ]
    """<p>The frequency, in seconds, at which the alarm is evaluated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricAlarm) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_arn" in value:
        out["AlarmArn"] = value["alarm_arn"]
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "alarm_configuration_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["AlarmConfigurationUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["alarm_configuration_updated_timestamp"]
            )
        )
    if "actions_enabled" in value:
        out["ActionsEnabled"] = value["actions_enabled"]
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["OKActions"] = capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
            value["ok_actions"]
        )
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["AlarmActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["alarm_actions"]
            )
        )
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["InsufficientDataActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["insufficient_data_actions"]
            )
        )
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        out["StateValue"] = capo_cloudwatch.types.state_value.serialize_aws_json_1_0(
            value["state_value"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_data" in value:
        out["StateReasonData"] = value["state_reason_data"]
    if "state_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_updated_timestamp"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "statistic" in value:
        import capo_cloudwatch.types.statistic

        out["Statistic"] = capo_cloudwatch.types.statistic.serialize_aws_json_1_0(
            value["statistic"]
        )
    if "extended_statistic" in value:
        out["ExtendedStatistic"] = value["extended_statistic"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "datapoints_to_alarm" in value:
        out["DatapointsToAlarm"] = value["datapoints_to_alarm"]
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
        import capo_cloudwatch.types.comparison_operator

        out["ComparisonOperator"] = (
            capo_cloudwatch.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison_operator"]
            )
        )
    if "treat_missing_data" in value:
        out["TreatMissingData"] = value["treat_missing_data"]
    if "evaluate_low_sample_count_percentile" in value:
        out["EvaluateLowSampleCountPercentile"] = value[
            "evaluate_low_sample_count_percentile"
        ]
    if "metrics" in value:
        import capo_cloudwatch.types.metric_data_queries

        out["Metrics"] = (
            capo_cloudwatch.types.metric_data_queries.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "threshold_metric_id" in value:
        out["ThresholdMetricId"] = value["threshold_metric_id"]
    if "evaluation_state" in value:
        import capo_cloudwatch.types.evaluation_state

        out["EvaluationState"] = (
            capo_cloudwatch.types.evaluation_state.serialize_aws_json_1_0(
                value["evaluation_state"]
            )
        )
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateTransitionedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_transitioned_timestamp"]
            )
        )
    if "evaluation_window" in value:
        import capo_cloudwatch.types.evaluation_window

        out["EvaluationWindow"] = (
            capo_cloudwatch.types.evaluation_window.serialize_aws_json_1_0(
                value["evaluation_window"]
            )
        )
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        out["WarmUpConfiguration"] = (
            capo_cloudwatch.types.warm_up_configuration.serialize_aws_json_1_0(
                value["warm_up_configuration"]
            )
        )
    if "evaluation_criteria" in value:
        import capo_cloudwatch.types.evaluation_criteria

        out["EvaluationCriteria"] = (
            capo_cloudwatch.types.evaluation_criteria.serialize_aws_json_1_0(
                value["evaluation_criteria"]
            )
        )
    if "evaluation_interval" in value:
        out["EvaluationInterval"] = value["evaluation_interval"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricAlarm:
    out: MetricAlarm = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmArn") is not None:
        out["alarm_arn"] = data["AlarmArn"]
    if data.get("AlarmDescription") is not None:
        out["alarm_description"] = data["AlarmDescription"]
    if data.get("AlarmConfigurationUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["alarm_configuration_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["AlarmConfigurationUpdatedTimestamp"]
            )
        )
    if data.get("ActionsEnabled") is not None:
        out["actions_enabled"] = data["ActionsEnabled"]
    if data.get("OKActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["OKActions"]
            )
        )
    if data.get("AlarmActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["AlarmActions"]
            )
        )
    if data.get("InsufficientDataActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["InsufficientDataActions"]
            )
        )
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_aws_json_1_0(
            data["StateValue"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonData") is not None:
        out["state_reason_data"] = data["StateReasonData"]
    if data.get("StateUpdatedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["state_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateUpdatedTimestamp"]
            )
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Statistic") is not None:
        import capo_cloudwatch.types.statistic

        out["statistic"] = capo_cloudwatch.types.statistic.deserialize_aws_json_1_0(
            data["Statistic"]
        )
    if data.get("ExtendedStatistic") is not None:
        out["extended_statistic"] = data["ExtendedStatistic"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    if data.get("EvaluationPeriods") is not None:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if data.get("DatapointsToAlarm") is not None:
        out["datapoints_to_alarm"] = data["DatapointsToAlarm"]
    if data.get("Threshold") is not None:
        out["threshold"] = float(data["Threshold"])
    if data.get("ComparisonOperator") is not None:
        import capo_cloudwatch.types.comparison_operator

        out["comparison_operator"] = (
            capo_cloudwatch.types.comparison_operator.deserialize_aws_json_1_0(
                data["ComparisonOperator"]
            )
        )
    if data.get("TreatMissingData") is not None:
        out["treat_missing_data"] = data["TreatMissingData"]
    if data.get("EvaluateLowSampleCountPercentile") is not None:
        out["evaluate_low_sample_count_percentile"] = data[
            "EvaluateLowSampleCountPercentile"
        ]
    if data.get("Metrics") is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metrics"] = (
            capo_cloudwatch.types.metric_data_queries.deserialize_aws_json_1_0(
                data["Metrics"]
            )
        )
    if data.get("ThresholdMetricId") is not None:
        out["threshold_metric_id"] = data["ThresholdMetricId"]
    if data.get("EvaluationState") is not None:
        import capo_cloudwatch.types.evaluation_state

        out["evaluation_state"] = (
            capo_cloudwatch.types.evaluation_state.deserialize_aws_json_1_0(
                data["EvaluationState"]
            )
        )
    if data.get("StateTransitionedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateTransitionedTimestamp"]
            )
        )
    if data.get("EvaluationWindow") is not None:
        import capo_cloudwatch.types.evaluation_window

        out["evaluation_window"] = (
            capo_cloudwatch.types.evaluation_window.deserialize_aws_json_1_0(
                data["EvaluationWindow"]
            )
        )
    if data.get("WarmUpConfiguration") is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_aws_json_1_0(
                data["WarmUpConfiguration"]
            )
        )
    if data.get("EvaluationCriteria") is not None:
        import capo_cloudwatch.types.evaluation_criteria

        out["evaluation_criteria"] = (
            capo_cloudwatch.types.evaluation_criteria.deserialize_aws_json_1_0(
                data["EvaluationCriteria"]
            )
        )
    if data.get("EvaluationInterval") is not None:
        out["evaluation_interval"] = data["EvaluationInterval"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricAlarm, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "alarm_arn" in value:
        pairs.append((f"{key_prefix}AlarmArn", str(value["alarm_arn"])))
    if "alarm_description" in value:
        pairs.append((f"{key_prefix}AlarmDescription", str(value["alarm_description"])))
    if "alarm_configuration_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["alarm_configuration_updated_timestamp"],
            pairs,
            f"{key_prefix}AlarmConfigurationUpdatedTimestamp",
        )
    if "actions_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ActionsEnabled",
                "true" if value["actions_enabled"] else "false",
            )
        )
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["ok_actions"], pairs, f"{key_prefix}OKActions"
        )
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["alarm_actions"], pairs, f"{key_prefix}AlarmActions"
        )
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["insufficient_data_actions"],
            pairs,
            f"{key_prefix}InsufficientDataActions",
        )
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        capo_cloudwatch.types.state_value.serialize_query(
            value["state_value"], pairs, f"{key_prefix}StateValue"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "state_reason_data" in value:
        pairs.append((f"{key_prefix}StateReasonData", str(value["state_reason_data"])))
    if "state_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_updated_timestamp"],
            pairs,
            f"{key_prefix}StateUpdatedTimestamp",
        )
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "statistic" in value:
        import capo_cloudwatch.types.statistic

        capo_cloudwatch.types.statistic.serialize_query(
            value["statistic"], pairs, f"{key_prefix}Statistic"
        )
    if "extended_statistic" in value:
        pairs.append(
            (f"{key_prefix}ExtendedStatistic", str(value["extended_statistic"]))
        )
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )
    if "evaluation_periods" in value:
        pairs.append(
            (f"{key_prefix}EvaluationPeriods", str(value["evaluation_periods"]))
        )
    if "datapoints_to_alarm" in value:
        pairs.append(
            (f"{key_prefix}DatapointsToAlarm", str(value["datapoints_to_alarm"]))
        )
    if "threshold" in value:
        pairs.append(
            (
                f"{key_prefix}Threshold",
                (
                    "NaN"
                    if value["threshold"] != value["threshold"]
                    else "Infinity"
                    if value["threshold"] == float("inf")
                    else "-Infinity"
                    if value["threshold"] == float("-inf")
                    else str(value["threshold"])
                ),
            )
        )
    if "comparison_operator" in value:
        import capo_cloudwatch.types.comparison_operator

        capo_cloudwatch.types.comparison_operator.serialize_query(
            value["comparison_operator"], pairs, f"{key_prefix}ComparisonOperator"
        )
    if "treat_missing_data" in value:
        pairs.append(
            (f"{key_prefix}TreatMissingData", str(value["treat_missing_data"]))
        )
    if "evaluate_low_sample_count_percentile" in value:
        pairs.append(
            (
                f"{key_prefix}EvaluateLowSampleCountPercentile",
                str(value["evaluate_low_sample_count_percentile"]),
            )
        )
    if "metrics" in value:
        import capo_cloudwatch.types.metric_data_queries

        capo_cloudwatch.types.metric_data_queries.serialize_query(
            value["metrics"], pairs, f"{key_prefix}Metrics"
        )
    if "threshold_metric_id" in value:
        pairs.append(
            (f"{key_prefix}ThresholdMetricId", str(value["threshold_metric_id"]))
        )
    if "evaluation_state" in value:
        import capo_cloudwatch.types.evaluation_state

        capo_cloudwatch.types.evaluation_state.serialize_query(
            value["evaluation_state"], pairs, f"{key_prefix}EvaluationState"
        )
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_transitioned_timestamp"],
            pairs,
            f"{key_prefix}StateTransitionedTimestamp",
        )
    if "evaluation_window" in value:
        import capo_cloudwatch.types.evaluation_window

        capo_cloudwatch.types.evaluation_window.serialize_query(
            value["evaluation_window"], pairs, f"{key_prefix}EvaluationWindow"
        )
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        capo_cloudwatch.types.warm_up_configuration.serialize_query(
            value["warm_up_configuration"], pairs, f"{key_prefix}WarmUpConfiguration"
        )
    if "evaluation_criteria" in value:
        import capo_cloudwatch.types.evaluation_criteria

        capo_cloudwatch.types.evaluation_criteria.serialize_query(
            value["evaluation_criteria"], pairs, f"{key_prefix}EvaluationCriteria"
        )
    if "evaluation_interval" in value:
        pairs.append(
            (f"{key_prefix}EvaluationInterval", str(value["evaluation_interval"]))
        )


def deserialize_query(el: Element) -> MetricAlarm:
    out: MetricAlarm = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_arn = el.find("AlarmArn")
    if child_alarm_arn is not None:
        out["alarm_arn"] = str(child_alarm_arn.text or "")
    child_alarm_description = el.find("AlarmDescription")
    if child_alarm_description is not None:
        out["alarm_description"] = str(child_alarm_description.text or "")
    child_alarm_configuration_updated_timestamp = el.find(
        "AlarmConfigurationUpdatedTimestamp"
    )
    if child_alarm_configuration_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["alarm_configuration_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_alarm_configuration_updated_timestamp
            )
        )
    child_actions_enabled = el.find("ActionsEnabled")
    if child_actions_enabled is not None:
        out["actions_enabled"] = (child_actions_enabled.text or "").lower() == "true"
    child_ok_actions = el.find("OKActions")
    if child_ok_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_ok_actions
        )
    child_alarm_actions = el.find("AlarmActions")
    if child_alarm_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_alarm_actions
        )
    child_insufficient_data_actions = el.find("InsufficientDataActions")
    if child_insufficient_data_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_query(
                child_insufficient_data_actions
            )
        )
    child_state_value = el.find("StateValue")
    if child_state_value is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_query(
            child_state_value
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_state_reason_data = el.find("StateReasonData")
    if child_state_reason_data is not None:
        out["state_reason_data"] = str(child_state_reason_data.text or "")
    child_state_updated_timestamp = el.find("StateUpdatedTimestamp")
    if child_state_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_updated_timestamp
            )
        )
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_cloudwatch.types.statistic

        out["statistic"] = capo_cloudwatch.types.statistic.deserialize_query(
            child_statistic
        )
    child_extended_statistic = el.find("ExtendedStatistic")
    if child_extended_statistic is not None:
        out["extended_statistic"] = str(child_extended_statistic.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    child_evaluation_periods = el.find("EvaluationPeriods")
    if child_evaluation_periods is not None:
        out["evaluation_periods"] = int(child_evaluation_periods.text or "")
    child_datapoints_to_alarm = el.find("DatapointsToAlarm")
    if child_datapoints_to_alarm is not None:
        out["datapoints_to_alarm"] = int(child_datapoints_to_alarm.text or "")
    child_threshold = el.find("Threshold")
    if child_threshold is not None:
        out["threshold"] = float(child_threshold.text or "")
    child_comparison_operator = el.find("ComparisonOperator")
    if child_comparison_operator is not None:
        import capo_cloudwatch.types.comparison_operator

        out["comparison_operator"] = (
            capo_cloudwatch.types.comparison_operator.deserialize_query(
                child_comparison_operator
            )
        )
    child_treat_missing_data = el.find("TreatMissingData")
    if child_treat_missing_data is not None:
        out["treat_missing_data"] = str(child_treat_missing_data.text or "")
    child_evaluate_low_sample_count_percentile = el.find(
        "EvaluateLowSampleCountPercentile"
    )
    if child_evaluate_low_sample_count_percentile is not None:
        out["evaluate_low_sample_count_percentile"] = str(
            child_evaluate_low_sample_count_percentile.text or ""
        )
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_cloudwatch.types.metric_data_queries

        out["metrics"] = capo_cloudwatch.types.metric_data_queries.deserialize_query(
            child_metrics
        )
    child_threshold_metric_id = el.find("ThresholdMetricId")
    if child_threshold_metric_id is not None:
        out["threshold_metric_id"] = str(child_threshold_metric_id.text or "")
    child_evaluation_state = el.find("EvaluationState")
    if child_evaluation_state is not None:
        import capo_cloudwatch.types.evaluation_state

        out["evaluation_state"] = (
            capo_cloudwatch.types.evaluation_state.deserialize_query(
                child_evaluation_state
            )
        )
    child_state_transitioned_timestamp = el.find("StateTransitionedTimestamp")
    if child_state_transitioned_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_transitioned_timestamp
            )
        )
    child_evaluation_window = el.find("EvaluationWindow")
    if child_evaluation_window is not None:
        import capo_cloudwatch.types.evaluation_window

        out["evaluation_window"] = (
            capo_cloudwatch.types.evaluation_window.deserialize_query(
                child_evaluation_window
            )
        )
    child_warm_up_configuration = el.find("WarmUpConfiguration")
    if child_warm_up_configuration is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_query(
                child_warm_up_configuration
            )
        )
    child_evaluation_criteria = el.find("EvaluationCriteria")
    if child_evaluation_criteria is not None:
        import capo_cloudwatch.types.evaluation_criteria

        out["evaluation_criteria"] = (
            capo_cloudwatch.types.evaluation_criteria.deserialize_query(
                child_evaluation_criteria
            )
        )
    child_evaluation_interval = el.find("EvaluationInterval")
    if child_evaluation_interval is not None:
        out["evaluation_interval"] = int(child_evaluation_interval.text or "")
    return out
