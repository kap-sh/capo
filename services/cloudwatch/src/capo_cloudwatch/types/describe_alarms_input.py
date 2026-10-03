"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.action_prefix
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_name_prefix
    import capo_cloudwatch.types.alarm_names
    import capo_cloudwatch.types.alarm_types
    import capo_cloudwatch.types.max_records
    import capo_cloudwatch.types.next_token
    import capo_cloudwatch.types.state_value


class DescribeAlarmsInput(TypedDict, closed=True):
    alarm_names: NotRequired["capo_cloudwatch.types.alarm_names.AlarmNames"]
    """<p>The names of the alarms to retrieve information about.</p>"""
    alarm_name_prefix: NotRequired[
        "capo_cloudwatch.types.alarm_name_prefix.AlarmNamePrefix"
    ]
    """<p>An alarm name prefix. If you specify this parameter, you receive information about all alarms that have names that start with this prefix.</p> <p>If this parameter is specified, you cannot specify <code>AlarmNames</code>.</p>"""
    alarm_types: NotRequired["capo_cloudwatch.types.alarm_types.AlarmTypes"]
    """<p>Use this parameter to specify whether you want the operation to return metric alarms, composite alarms, or log alarms. If you omit this parameter, only metric alarms are returned, even if composite alarms or log alarms exist in the account.</p> <p>For example, if you omit this parameter or specify <code>MetricAlarms</code>, the operation returns only a list of metric alarms. It does not return any composite alarms or log alarms, even if they exist in the account.</p> <p>If you specify <code>CompositeAlarms</code>, the operation returns only a list of composite alarms, and does not return any metric alarms or log alarms.</p> <p>If you specify <code>LogAlarms</code>, the operation returns only a list of log alarms, and does not return any metric alarms or composite alarms.</p>"""
    children_of_alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>If you use this parameter and specify the name of a composite alarm, the operation returns information about the "children" alarms of the alarm you specify. These are the metric alarms and composite alarms referenced in the <code>AlarmRule</code> field of the composite alarm that you specify in <code>ChildrenOfAlarmName</code>. Information about the composite alarm that you name in <code>ChildrenOfAlarmName</code> is not returned.</p> <p>If you specify <code>ChildrenOfAlarmName</code>, you cannot specify any other parameters in the request except for <code>MaxRecords</code> and <code>NextToken</code>. If you do so, you receive a validation error.</p> <note> <p>Only the <code>Alarm Name</code>, <code>ARN</code>, <code>StateValue</code> (OK/ALARM/INSUFFICIENT_DATA), and <code>StateUpdatedTimestamp</code> information are returned by this operation when you use this parameter. To get complete information about these alarms, perform another <code>DescribeAlarms</code> operation and specify the parent alarm names in the <code>AlarmNames</code> parameter.</p> </note>"""
    parents_of_alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>If you use this parameter and specify the name of a metric or composite alarm, the operation returns information about the "parent" alarms of the alarm you specify. These are the composite alarms that have <code>AlarmRule</code> parameters that reference the alarm named in <code>ParentsOfAlarmName</code>. Information about the alarm that you specify in <code>ParentsOfAlarmName</code> is not returned.</p> <p>If you specify <code>ParentsOfAlarmName</code>, you cannot specify any other parameters in the request except for <code>MaxRecords</code> and <code>NextToken</code>. If you do so, you receive a validation error.</p> <note> <p>Only the Alarm Name and ARN are returned by this operation when you use this parameter. To get complete information about these alarms, perform another <code>DescribeAlarms</code> operation and specify the parent alarm names in the <code>AlarmNames</code> parameter.</p> </note>"""
    state_value: NotRequired["capo_cloudwatch.types.state_value.StateValue"]
    """<p>Specify this parameter to receive information only about alarms that are currently in the state that you specify.</p>"""
    action_prefix: NotRequired["capo_cloudwatch.types.action_prefix.ActionPrefix"]
    """<p>Use this parameter to filter the results of the operation to only those alarms that use a certain alarm action. For example, you could specify the ARN of an SNS topic to find all alarms that send notifications to that topic.</p>"""
    max_records: NotRequired["capo_cloudwatch.types.max_records.MaxRecords"]
    """<p>The maximum number of alarm descriptions to retrieve.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsInput) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_cloudwatch.types.alarm_names

        out["AlarmNames"] = capo_cloudwatch.types.alarm_names.serialize_aws_json_1_0(
            value["alarm_names"]
        )
    if "alarm_name_prefix" in value:
        out["AlarmNamePrefix"] = value["alarm_name_prefix"]
    if "alarm_types" in value:
        import capo_cloudwatch.types.alarm_types

        out["AlarmTypes"] = capo_cloudwatch.types.alarm_types.serialize_aws_json_1_0(
            value["alarm_types"]
        )
    if "children_of_alarm_name" in value:
        out["ChildrenOfAlarmName"] = value["children_of_alarm_name"]
    if "parents_of_alarm_name" in value:
        out["ParentsOfAlarmName"] = value["parents_of_alarm_name"]
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        out["StateValue"] = capo_cloudwatch.types.state_value.serialize_aws_json_1_0(
            value["state_value"]
        )
    if "action_prefix" in value:
        out["ActionPrefix"] = value["action_prefix"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsInput:
    out: DescribeAlarmsInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmNames") is not None:
        import capo_cloudwatch.types.alarm_names

        out["alarm_names"] = capo_cloudwatch.types.alarm_names.deserialize_aws_json_1_0(
            data["AlarmNames"]
        )
    if data.get("AlarmNamePrefix") is not None:
        out["alarm_name_prefix"] = data["AlarmNamePrefix"]
    if data.get("AlarmTypes") is not None:
        import capo_cloudwatch.types.alarm_types

        out["alarm_types"] = capo_cloudwatch.types.alarm_types.deserialize_aws_json_1_0(
            data["AlarmTypes"]
        )
    if data.get("ChildrenOfAlarmName") is not None:
        out["children_of_alarm_name"] = data["ChildrenOfAlarmName"]
    if data.get("ParentsOfAlarmName") is not None:
        out["parents_of_alarm_name"] = data["ParentsOfAlarmName"]
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_aws_json_1_0(
            data["StateValue"]
        )
    if data.get("ActionPrefix") is not None:
        out["action_prefix"] = data["ActionPrefix"]
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_names" in value:
        import capo_cloudwatch.types.alarm_names

        capo_cloudwatch.types.alarm_names.serialize_query(
            value["alarm_names"], pairs, f"{key_prefix}AlarmNames"
        )
    if "alarm_name_prefix" in value:
        pairs.append((f"{key_prefix}AlarmNamePrefix", str(value["alarm_name_prefix"])))
    if "alarm_types" in value:
        import capo_cloudwatch.types.alarm_types

        capo_cloudwatch.types.alarm_types.serialize_query(
            value["alarm_types"], pairs, f"{key_prefix}AlarmTypes"
        )
    if "children_of_alarm_name" in value:
        pairs.append(
            (f"{key_prefix}ChildrenOfAlarmName", str(value["children_of_alarm_name"]))
        )
    if "parents_of_alarm_name" in value:
        pairs.append(
            (f"{key_prefix}ParentsOfAlarmName", str(value["parents_of_alarm_name"]))
        )
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        capo_cloudwatch.types.state_value.serialize_query(
            value["state_value"], pairs, f"{key_prefix}StateValue"
        )
    if "action_prefix" in value:
        pairs.append((f"{key_prefix}ActionPrefix", str(value["action_prefix"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmsInput:
    out: DescribeAlarmsInput = {}  # type: ignore[typeddict-item]
    child_alarm_names = el.find("AlarmNames")
    if child_alarm_names is not None:
        import capo_cloudwatch.types.alarm_names

        out["alarm_names"] = capo_cloudwatch.types.alarm_names.deserialize_query(
            child_alarm_names
        )
    child_alarm_name_prefix = el.find("AlarmNamePrefix")
    if child_alarm_name_prefix is not None:
        out["alarm_name_prefix"] = str(child_alarm_name_prefix.text or "")
    child_alarm_types = el.find("AlarmTypes")
    if child_alarm_types is not None:
        import capo_cloudwatch.types.alarm_types

        out["alarm_types"] = capo_cloudwatch.types.alarm_types.deserialize_query(
            child_alarm_types
        )
    child_children_of_alarm_name = el.find("ChildrenOfAlarmName")
    if child_children_of_alarm_name is not None:
        out["children_of_alarm_name"] = str(child_children_of_alarm_name.text or "")
    child_parents_of_alarm_name = el.find("ParentsOfAlarmName")
    if child_parents_of_alarm_name is not None:
        out["parents_of_alarm_name"] = str(child_parents_of_alarm_name.text or "")
    child_state_value = el.find("StateValue")
    if child_state_value is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_query(
            child_state_value
        )
    child_action_prefix = el.find("ActionPrefix")
    if child_action_prefix is not None:
        out["action_prefix"] = str(child_action_prefix.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
