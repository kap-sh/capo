"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutCompositeAlarmInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.alarm_arn
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_rule
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.suppressor_period
    import capo_cloudwatch.types.tag_list


class PutCompositeAlarmInput(TypedDict, closed=True):
    actions_enabled: NotRequired["capo_cloudwatch.types.actions_enabled.ActionsEnabled"]
    """<p>Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is <code>TRUE</code>.</p>"""
    alarm_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul> <p> <b>Systems Manager actions:</b> </p> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i> </code> </p> <p> <b>Start a Amazon Q Developer operational investigation</b> </p> <p> <code>arn:aws:aiops:<i>region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code> </p>"""
    alarm_description: NotRequired[
        "capo_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>The description for the composite alarm.</p>"""
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name for the composite alarm. This name must be unique within the Region.</p>"""
    alarm_rule: NotRequired["capo_cloudwatch.types.alarm_rule.AlarmRule"]
    """<p>An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.</p> <p>You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.</p> <p>Functions can include the following:</p> <ul> <li> <p> <code>ALARM("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in ALARM state.</p> </li> <li> <p> <code>OK("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in OK state.</p> </li> <li> <p> <code>INSUFFICIENT_DATA("<i>alarm-name</i> or <i>alarm-ARN</i>")</code> is TRUE if the named alarm is in INSUFFICIENT_DATA state.</p> </li> <li> <p> <code>TRUE</code> always evaluates to TRUE.</p> </li> <li> <p> <code>FALSE</code> always evaluates to FALSE.</p> </li> </ul> <p>TRUE and FALSE are useful for testing a complex <code>AlarmRule</code> structure, and for testing your alarm actions.</p> <p>Alarm names specified in <code>AlarmRule</code> can be surrounded with double-quotes ("), but do not have to be.</p> <p>The following are some examples of <code>AlarmRule</code>:</p> <ul> <li> <p> <code>ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)</code> specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.</p> </li> <li> <p> <code>ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)</code> specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.</p> </li> <li> <p> <code>(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh)</code> goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.</p> </li> </ul> <p>The <code>AlarmRule</code> can specify as many as 100 "children" alarms. The <code>AlarmRule</code> expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.</p>"""
    insufficient_data_actions: NotRequired[
        "capo_cloudwatch.types.resource_list.ResourceList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>"""
    ok_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: ]</p> <p> <b>Amazon SNS actions:</b> </p> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> </p> <p> <b>Lambda actions:</b> </p> <ul> <li> <p>Invoke the latest version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i> </code> </p> </li> <li> <p>Invoke a specific version of a Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>version-number</i> </code> </p> </li> <li> <p>Invoke a function by using an alias Lambda function: <code>arn:aws:lambda:<i>region</i>:<i>account-id</i>:function:<i>function-name</i>:<i>alias-name</i> </code> </p> </li> </ul>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>"""
    actions_suppressor: NotRequired["capo_cloudwatch.types.alarm_arn.AlarmArn"]
    """<p> Actions will be suppressed if the suppressor alarm is in the <code>ALARM</code> state. <code>ActionsSuppressor</code> can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. </p>"""
    actions_suppressor_wait_period: NotRequired[
        "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
    ]
    """<p> The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>WaitPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>"""
    actions_suppressor_extension_period: NotRequired[
        "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
    ]
    """<p> The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>ExtensionPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutCompositeAlarmInput) -> dict:
    out: dict = {}
    if "actions_enabled" in value:
        out["ActionsEnabled"] = value["actions_enabled"]
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["AlarmActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["alarm_actions"]
            )
        )
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_rule" in value:
        out["AlarmRule"] = value["alarm_rule"]
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["InsufficientDataActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["insufficient_data_actions"]
            )
        )
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["OKActions"] = capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
            value["ok_actions"]
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "actions_suppressor" in value:
        out["ActionsSuppressor"] = value["actions_suppressor"]
    if "actions_suppressor_wait_period" in value:
        out["ActionsSuppressorWaitPeriod"] = value["actions_suppressor_wait_period"]
    if "actions_suppressor_extension_period" in value:
        out["ActionsSuppressorExtensionPeriod"] = value[
            "actions_suppressor_extension_period"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutCompositeAlarmInput:
    out: PutCompositeAlarmInput = {}  # type: ignore[typeddict-item]
    if data.get("ActionsEnabled") is not None:
        out["actions_enabled"] = data["ActionsEnabled"]
    if data.get("AlarmActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["AlarmActions"]
            )
        )
    if data.get("AlarmDescription") is not None:
        out["alarm_description"] = data["AlarmDescription"]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("AlarmRule") is not None:
        out["alarm_rule"] = data["AlarmRule"]
    if data.get("InsufficientDataActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["InsufficientDataActions"]
            )
        )
    if data.get("OKActions") is not None:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["OKActions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ActionsSuppressor") is not None:
        out["actions_suppressor"] = data["ActionsSuppressor"]
    if data.get("ActionsSuppressorWaitPeriod") is not None:
        out["actions_suppressor_wait_period"] = data["ActionsSuppressorWaitPeriod"]
    if data.get("ActionsSuppressorExtensionPeriod") is not None:
        out["actions_suppressor_extension_period"] = data[
            "ActionsSuppressorExtensionPeriod"
        ]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutCompositeAlarmInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "actions_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ActionsEnabled",
                "true" if value["actions_enabled"] else "false",
            )
        )
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["alarm_actions"], pairs, f"{key_prefix}AlarmActions"
        )
    if "alarm_description" in value:
        pairs.append((f"{key_prefix}AlarmDescription", str(value["alarm_description"])))
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "alarm_rule" in value:
        pairs.append((f"{key_prefix}AlarmRule", str(value["alarm_rule"])))
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["insufficient_data_actions"],
            pairs,
            f"{key_prefix}InsufficientDataActions",
        )
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["ok_actions"], pairs, f"{key_prefix}OKActions"
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "actions_suppressor" in value:
        pairs.append(
            (f"{key_prefix}ActionsSuppressor", str(value["actions_suppressor"]))
        )
    if "actions_suppressor_wait_period" in value:
        pairs.append(
            (
                f"{key_prefix}ActionsSuppressorWaitPeriod",
                str(value["actions_suppressor_wait_period"]),
            )
        )
    if "actions_suppressor_extension_period" in value:
        pairs.append(
            (
                f"{key_prefix}ActionsSuppressorExtensionPeriod",
                str(value["actions_suppressor_extension_period"]),
            )
        )


def deserialize_query(el: Element) -> PutCompositeAlarmInput:
    out: PutCompositeAlarmInput = {}  # type: ignore[typeddict-item]
    child_actions_enabled = el.find("ActionsEnabled")
    if child_actions_enabled is not None:
        out["actions_enabled"] = (child_actions_enabled.text or "").lower() == "true"
    child_alarm_actions = el.find("AlarmActions")
    if child_alarm_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_alarm_actions
        )
    child_alarm_description = el.find("AlarmDescription")
    if child_alarm_description is not None:
        out["alarm_description"] = str(child_alarm_description.text or "")
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_rule = el.find("AlarmRule")
    if child_alarm_rule is not None:
        out["alarm_rule"] = str(child_alarm_rule.text or "")
    child_insufficient_data_actions = el.find("InsufficientDataActions")
    if child_insufficient_data_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_query(
                child_insufficient_data_actions
            )
        )
    child_ok_actions = el.find("OKActions")
    if child_ok_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_ok_actions
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_actions_suppressor = el.find("ActionsSuppressor")
    if child_actions_suppressor is not None:
        out["actions_suppressor"] = str(child_actions_suppressor.text or "")
    child_actions_suppressor_wait_period = el.find("ActionsSuppressorWaitPeriod")
    if child_actions_suppressor_wait_period is not None:
        out["actions_suppressor_wait_period"] = int(
            child_actions_suppressor_wait_period.text or ""
        )
    child_actions_suppressor_extension_period = el.find(
        "ActionsSuppressorExtensionPeriod"
    )
    if child_actions_suppressor_extension_period is not None:
        out["actions_suppressor_extension_period"] = int(
            child_actions_suppressor_extension_period.text or ""
        )
    return out
