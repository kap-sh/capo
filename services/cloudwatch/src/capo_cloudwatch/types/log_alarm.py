"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LogAlarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.action_log_line_count
    import capo_cloudwatch.types.action_log_line_role_arn
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.alarm_arn
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.comparison_operator
    import capo_cloudwatch.types.evaluation_state
    import capo_cloudwatch.types.query_results_to_alarm
    import capo_cloudwatch.types.query_results_to_evaluate
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.scheduled_query_configuration
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.state_reason_data
    import capo_cloudwatch.types.state_value
    import capo_cloudwatch.types.threshold
    import capo_cloudwatch.types.timestamp
    import capo_cloudwatch.types.treat_missing_data
    import capo_cloudwatch.types.warm_up_configuration


class LogAlarm(TypedDict, closed=True):
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
    scheduled_query_configuration: NotRequired[
        "capo_cloudwatch.types.scheduled_query_configuration.ScheduledQueryConfiguration"
    ]
    """<p>The configuration of the underlying CloudWatch Logs scheduled query, including the query string, log groups, schedule, aggregation expression, and the ARN of the managed scheduled query.</p>"""
    query_results_to_evaluate: NotRequired[
        "capo_cloudwatch.types.query_results_to_evaluate.QueryResultsToEvaluate"
    ]
    """<p>The number of most recent scheduled query results that the alarm evaluates against the threshold (the N in M-of-N evaluation).</p>"""
    query_results_to_alarm: NotRequired[
        "capo_cloudwatch.types.query_results_to_alarm.QueryResultsToAlarm"
    ]
    """<p>The number of query results, out of the most recent <code>QueryResultsToEvaluate</code> results, that must breach the threshold to trigger the alarm to transition to <code>ALARM</code> (the M in M-of-N evaluation).</p>"""
    threshold: NotRequired["capo_cloudwatch.types.threshold.Threshold"]
    """<p>The value to compare with the aggregated query result.</p>"""
    comparison_operator: NotRequired[
        "capo_cloudwatch.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand.</p>"""
    treat_missing_data: NotRequired[
        "capo_cloudwatch.types.treat_missing_data.TreatMissingData"
    ]
    """<p>How this alarm handles missing data points. Valid values are <code>breaching</code>, <code>notBreaching</code>, <code>ignore</code>, and <code>missing</code>.</p>"""
    state_transitioned_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the alarm's <code>StateValue</code> most recently changed.</p>"""
    evaluation_state: NotRequired[
        "capo_cloudwatch.types.evaluation_state.EvaluationState"
    ]
    """<p>If the value of this field is <code>EVALUATION_ERROR</code>, it indicates configuration errors in the alarm setup that require review and correction. Refer to the <code>StateReason</code> field of the alarm for more details.</p> <p>If the value of this field is <code>EVALUATION_FAILURE</code>, it indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved.</p> <p>If the value of this field is <code>PARTIAL_DATA</code>, it indicates that the query returned the maximum 500 contributor groups but more matched. The alarm evaluates the available contributors, but results might be incomplete.</p>"""
    action_log_line_count: NotRequired[
        "capo_cloudwatch.types.action_log_line_count.ActionLogLineCount"
    ]
    """<p>The number of log lines from the most recent scheduled query execution that are included in alarm action notifications. Valid range is 0 through 50. A value of 0 means no log lines are included.</p>"""
    action_log_line_role_arn: NotRequired[
        "capo_cloudwatch.types.action_log_line_role_arn.ActionLogLineRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Set when <code>ActionLogLineCount</code> is greater than 0.</p>"""
    warm_up_configuration: NotRequired[
        "capo_cloudwatch.types.warm_up_configuration.WarmUpConfiguration"
    ]
    """<p>The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. During the warm-up period, the alarm stays in <code>INSUFFICIENT_DATA</code> and does not perform alarm actions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html">Alarm warm-up periods</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogAlarm) -> dict:
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
    if "scheduled_query_configuration" in value:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["ScheduledQueryConfiguration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.serialize_aws_json_1_0(
                value["scheduled_query_configuration"]
            )
        )
    if "query_results_to_evaluate" in value:
        out["QueryResultsToEvaluate"] = value["query_results_to_evaluate"]
    if "query_results_to_alarm" in value:
        out["QueryResultsToAlarm"] = value["query_results_to_alarm"]
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
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateTransitionedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_transitioned_timestamp"]
            )
        )
    if "evaluation_state" in value:
        import capo_cloudwatch.types.evaluation_state

        out["EvaluationState"] = (
            capo_cloudwatch.types.evaluation_state.serialize_aws_json_1_0(
                value["evaluation_state"]
            )
        )
    if "action_log_line_count" in value:
        out["ActionLogLineCount"] = value["action_log_line_count"]
    if "action_log_line_role_arn" in value:
        out["ActionLogLineRoleArn"] = value["action_log_line_role_arn"]
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        out["WarmUpConfiguration"] = (
            capo_cloudwatch.types.warm_up_configuration.serialize_aws_json_1_0(
                value["warm_up_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LogAlarm:
    out: LogAlarm = {}  # type: ignore[typeddict-item]
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
    if data.get("ScheduledQueryConfiguration") is not None:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["scheduled_query_configuration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.deserialize_aws_json_1_0(
                data["ScheduledQueryConfiguration"]
            )
        )
    if data.get("QueryResultsToEvaluate") is not None:
        out["query_results_to_evaluate"] = data["QueryResultsToEvaluate"]
    if data.get("QueryResultsToAlarm") is not None:
        out["query_results_to_alarm"] = data["QueryResultsToAlarm"]
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
    if data.get("StateTransitionedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateTransitionedTimestamp"]
            )
        )
    if data.get("EvaluationState") is not None:
        import capo_cloudwatch.types.evaluation_state

        out["evaluation_state"] = (
            capo_cloudwatch.types.evaluation_state.deserialize_aws_json_1_0(
                data["EvaluationState"]
            )
        )
    if data.get("ActionLogLineCount") is not None:
        out["action_log_line_count"] = data["ActionLogLineCount"]
    if data.get("ActionLogLineRoleArn") is not None:
        out["action_log_line_role_arn"] = data["ActionLogLineRoleArn"]
    if data.get("WarmUpConfiguration") is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_aws_json_1_0(
                data["WarmUpConfiguration"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(value: LogAlarm, pairs: list[tuple[str, str]], prefix: str) -> None:
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
    if "scheduled_query_configuration" in value:
        import capo_cloudwatch.types.scheduled_query_configuration

        capo_cloudwatch.types.scheduled_query_configuration.serialize_query(
            value["scheduled_query_configuration"],
            pairs,
            f"{key_prefix}ScheduledQueryConfiguration",
        )
    if "query_results_to_evaluate" in value:
        pairs.append(
            (
                f"{key_prefix}QueryResultsToEvaluate",
                str(value["query_results_to_evaluate"]),
            )
        )
    if "query_results_to_alarm" in value:
        pairs.append(
            (f"{key_prefix}QueryResultsToAlarm", str(value["query_results_to_alarm"]))
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
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_transitioned_timestamp"],
            pairs,
            f"{key_prefix}StateTransitionedTimestamp",
        )
    if "evaluation_state" in value:
        import capo_cloudwatch.types.evaluation_state

        capo_cloudwatch.types.evaluation_state.serialize_query(
            value["evaluation_state"], pairs, f"{key_prefix}EvaluationState"
        )
    if "action_log_line_count" in value:
        pairs.append(
            (f"{key_prefix}ActionLogLineCount", str(value["action_log_line_count"]))
        )
    if "action_log_line_role_arn" in value:
        pairs.append(
            (
                f"{key_prefix}ActionLogLineRoleArn",
                str(value["action_log_line_role_arn"]),
            )
        )
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        capo_cloudwatch.types.warm_up_configuration.serialize_query(
            value["warm_up_configuration"], pairs, f"{key_prefix}WarmUpConfiguration"
        )


def deserialize_query(el: Element) -> LogAlarm:
    out: LogAlarm = {}  # type: ignore[typeddict-item]
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
    child_scheduled_query_configuration = el.find("ScheduledQueryConfiguration")
    if child_scheduled_query_configuration is not None:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["scheduled_query_configuration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.deserialize_query(
                child_scheduled_query_configuration
            )
        )
    child_query_results_to_evaluate = el.find("QueryResultsToEvaluate")
    if child_query_results_to_evaluate is not None:
        out["query_results_to_evaluate"] = int(
            child_query_results_to_evaluate.text or ""
        )
    child_query_results_to_alarm = el.find("QueryResultsToAlarm")
    if child_query_results_to_alarm is not None:
        out["query_results_to_alarm"] = int(child_query_results_to_alarm.text or "")
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
    child_state_transitioned_timestamp = el.find("StateTransitionedTimestamp")
    if child_state_transitioned_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_transitioned_timestamp
            )
        )
    child_evaluation_state = el.find("EvaluationState")
    if child_evaluation_state is not None:
        import capo_cloudwatch.types.evaluation_state

        out["evaluation_state"] = (
            capo_cloudwatch.types.evaluation_state.deserialize_query(
                child_evaluation_state
            )
        )
    child_action_log_line_count = el.find("ActionLogLineCount")
    if child_action_log_line_count is not None:
        out["action_log_line_count"] = int(child_action_log_line_count.text or "")
    child_action_log_line_role_arn = el.find("ActionLogLineRoleArn")
    if child_action_log_line_role_arn is not None:
        out["action_log_line_role_arn"] = str(child_action_log_line_role_arn.text or "")
    child_warm_up_configuration = el.find("WarmUpConfiguration")
    if child_warm_up_configuration is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_query(
                child_warm_up_configuration
            )
        )
    return out
