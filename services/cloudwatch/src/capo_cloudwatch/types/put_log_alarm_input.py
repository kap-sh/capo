"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutLogAlarmInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.action_log_line_count
    import capo_cloudwatch.types.action_log_line_role_arn
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.comparison_operator
    import capo_cloudwatch.types.query_results_to_alarm
    import capo_cloudwatch.types.query_results_to_evaluate
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.scheduled_query_configuration
    import capo_cloudwatch.types.tag_list
    import capo_cloudwatch.types.threshold
    import capo_cloudwatch.types.treat_missing_data
    import capo_cloudwatch.types.warm_up_configuration


class PutLogAlarmInput(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name for the alarm. This name must be unique within the Amazon Web Services account and Region.</p>"""
    alarm_description: NotRequired[
        "capo_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>The description for the alarm.</p>"""
    scheduled_query_configuration: NotRequired[
        "capo_cloudwatch.types.scheduled_query_configuration.ScheduledQueryConfiguration"
    ]
    """<p>The configuration of the underlying CloudWatch Logs scheduled query that this alarm evaluates, including the query string, log groups, schedule, and aggregation expression.</p>"""
    action_log_line_count: NotRequired[
        "capo_cloudwatch.types.action_log_line_count.ActionLogLineCount"
    ]
    """<p>The number of log lines from the most recent scheduled query execution to include in alarm action notifications. Valid range is 0 through 50. The default is 0, which means no log lines are included.</p>"""
    action_log_line_role_arn: NotRequired[
        "capo_cloudwatch.types.action_log_line_role_arn.ActionLogLineRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Required when <code>ActionLogLineCount</code> is greater than 0.</p>"""
    actions_enabled: NotRequired["capo_cloudwatch.types.actions_enabled.ActionsEnabled"]
    """<p>Indicates whether actions should be executed during any changes to the alarm state. The default is <code>true</code>.</p>"""
    ok_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>"""
    alarm_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>Systems Manager actions:</b> </p> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i> </code> </p>"""
    insufficient_data_actions: NotRequired[
        "capo_cloudwatch.types.resource_list.ResourceList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values:</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>"""
    query_results_to_evaluate: NotRequired[
        "capo_cloudwatch.types.query_results_to_evaluate.QueryResultsToEvaluate"
    ]
    """<p>The number of most recent scheduled query results to evaluate against the threshold (the N in M-of-N evaluation). Valid range is 1 through 100.</p>"""
    query_results_to_alarm: NotRequired[
        "capo_cloudwatch.types.query_results_to_alarm.QueryResultsToAlarm"
    ]
    """<p>The number of query results, out of the most recent <code>QueryResultsToEvaluate</code> results, that must breach the threshold to trigger the alarm to transition to <code>ALARM</code> (the M in M-of-N evaluation). Must be less than or equal to <code>QueryResultsToEvaluate</code>.</p>"""
    threshold: NotRequired["capo_cloudwatch.types.threshold.Threshold"]
    """<p>The value to compare with the aggregated query result.</p>"""
    comparison_operator: NotRequired[
        "capo_cloudwatch.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand. Valid values are <code>GreaterThanThreshold</code>, <code>GreaterThanOrEqualToThreshold</code>, <code>LessThanThreshold</code>, and <code>LessThanOrEqualToThreshold</code>.</p>"""
    treat_missing_data: NotRequired[
        "capo_cloudwatch.types.treat_missing_data.TreatMissingData"
    ]
    """<p>Sets how this alarm is to handle missing data points. Valid values are <code>breaching</code>, <code>notBreaching</code>, <code>ignore</code>, and <code>missing</code>. If this parameter is omitted, the default behavior of <code>missing</code> is used.</p>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the alarm. You can use tags to categorize and manage your alarms.</p>"""
    warm_up_configuration: NotRequired[
        "capo_cloudwatch.types.warm_up_configuration.WarmUpConfiguration"
    ]
    """<p>The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. The warm-up period reduces alarm noise from missing data while a new resource or service starts publishing data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html">Alarm warm-up periods</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutLogAlarmInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "scheduled_query_configuration" in value:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["ScheduledQueryConfiguration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.serialize_aws_json_1_0(
                value["scheduled_query_configuration"]
            )
        )
    if "action_log_line_count" in value:
        out["ActionLogLineCount"] = value["action_log_line_count"]
    if "action_log_line_role_arn" in value:
        out["ActionLogLineRoleArn"] = value["action_log_line_role_arn"]
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
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        out["WarmUpConfiguration"] = (
            capo_cloudwatch.types.warm_up_configuration.serialize_aws_json_1_0(
                value["warm_up_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutLogAlarmInput:
    out: PutLogAlarmInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmDescription") is not None:
        out["alarm_description"] = data["AlarmDescription"]
    if data.get("ScheduledQueryConfiguration") is not None:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["scheduled_query_configuration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.deserialize_aws_json_1_0(
                data["ScheduledQueryConfiguration"]
            )
        )
    if data.get("ActionLogLineCount") is not None:
        out["action_log_line_count"] = data["ActionLogLineCount"]
    if data.get("ActionLogLineRoleArn") is not None:
        out["action_log_line_role_arn"] = data["ActionLogLineRoleArn"]
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
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("WarmUpConfiguration") is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_aws_json_1_0(
                data["WarmUpConfiguration"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutLogAlarmInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "alarm_description" in value:
        pairs.append((f"{key_prefix}AlarmDescription", str(value["alarm_description"])))
    if "scheduled_query_configuration" in value:
        import capo_cloudwatch.types.scheduled_query_configuration

        capo_cloudwatch.types.scheduled_query_configuration.serialize_query(
            value["scheduled_query_configuration"],
            pairs,
            f"{key_prefix}ScheduledQueryConfiguration",
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
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "warm_up_configuration" in value:
        import capo_cloudwatch.types.warm_up_configuration

        capo_cloudwatch.types.warm_up_configuration.serialize_query(
            value["warm_up_configuration"], pairs, f"{key_prefix}WarmUpConfiguration"
        )


def deserialize_query(el: Element) -> PutLogAlarmInput:
    out: PutLogAlarmInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_description = el.find("AlarmDescription")
    if child_alarm_description is not None:
        out["alarm_description"] = str(child_alarm_description.text or "")
    child_scheduled_query_configuration = el.find("ScheduledQueryConfiguration")
    if child_scheduled_query_configuration is not None:
        import capo_cloudwatch.types.scheduled_query_configuration

        out["scheduled_query_configuration"] = (
            capo_cloudwatch.types.scheduled_query_configuration.deserialize_query(
                child_scheduled_query_configuration
            )
        )
    child_action_log_line_count = el.find("ActionLogLineCount")
    if child_action_log_line_count is not None:
        out["action_log_line_count"] = int(child_action_log_line_count.text or "")
    child_action_log_line_role_arn = el.find("ActionLogLineRoleArn")
    if child_action_log_line_role_arn is not None:
        out["action_log_line_role_arn"] = str(child_action_log_line_role_arn.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_warm_up_configuration = el.find("WarmUpConfiguration")
    if child_warm_up_configuration is not None:
        import capo_cloudwatch.types.warm_up_configuration

        out["warm_up_configuration"] = (
            capo_cloudwatch.types.warm_up_configuration.deserialize_query(
                child_warm_up_configuration
            )
        )
    return out
