"""Generated from Smithy shape ``com.amazonaws.lightsail#PutAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.comparison_operator
    import capo_lightsail.types.contact_protocols_list
    import capo_lightsail.types.double
    import capo_lightsail.types.integer
    import capo_lightsail.types.metric_name
    import capo_lightsail.types.notification_trigger_list
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list
    import capo_lightsail.types.treat_missing_data


class PutAlarmRequest(TypedDict, closed=True):
    alarm_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.</p>"""
    metric_name: "capo_lightsail.types.metric_name.MetricName"
    """<p>The name of the metric to associate with the alarm.</p> <p>You can configure up to two alarms per metric.</p> <p>The following metrics are available for each resource type:</p> <ul> <li> <p> <b>Instances</b>: <code>BurstCapacityPercentage</code>, <code>BurstCapacityTime</code>, <code>CPUUtilization</code>, <code>NetworkIn</code>, <code>NetworkOut</code>, <code>StatusCheckFailed</code>, <code>StatusCheckFailed_Instance</code>, and <code>StatusCheckFailed_System</code>.</p> </li> <li> <p> <b>Load balancers</b>: <code>ClientTLSNegotiationErrorCount</code>, <code>HealthyHostCount</code>, <code>UnhealthyHostCount</code>, <code>HTTPCode_LB_4XX_Count</code>, <code>HTTPCode_LB_5XX_Count</code>, <code>HTTPCode_Instance_2XX_Count</code>, <code>HTTPCode_Instance_3XX_Count</code>, <code>HTTPCode_Instance_4XX_Count</code>, <code>HTTPCode_Instance_5XX_Count</code>, <code>InstanceResponseTime</code>, <code>RejectedConnectionCount</code>, and <code>RequestCount</code>.</p> </li> <li> <p> <b>Relational databases</b>: <code>CPUUtilization</code>, <code>DatabaseConnections</code>, <code>DiskQueueDepth</code>, <code>FreeStorageSpace</code>, <code>NetworkReceiveThroughput</code>, and <code>NetworkTransmitThroughput</code>.</p> </li> </ul> <p>For more information about these metrics, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resource-health-metrics#available-metrics">Metrics available in Lightsail</a>.</p>"""
    monitored_resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail resource that will be monitored.</p> <p>Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.</p>"""
    comparison_operator: "capo_lightsail.types.comparison_operator.ComparisonOperator"
    """<p>The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.</p>"""
    threshold: "capo_lightsail.types.double.double"
    """<p>The value against which the specified statistic is compared.</p>"""
    evaluation_periods: "capo_lightsail.types.integer.integer"
    """<p>The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (<code>evaluationPeriods</code>) is the N.</p> <p>If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies the rolling period of time in which data points are evaluated.</p> <p>Each evaluation period is five minutes long. For example, specify an evaluation period of 24 to evaluate a metric over a rolling period of two hours.</p> <p>You can specify a minimum valuation period of 1 (5 minutes), and a maximum evaluation period of 288 (24 hours).</p>"""
    datapoints_to_alarm: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (<code>datapointsToAlarm</code>) is the M.</p>"""
    treat_missing_data: NotRequired[
        "capo_lightsail.types.treat_missing_data.TreatMissingData"
    ]
    """<p>Sets how this alarm will handle missing data points.</p> <p>An alarm can treat missing data in the following ways:</p> <ul> <li> <p> <code>breaching</code> - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>notBreaching</code> - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>ignore</code> - Ignore the missing data. Maintains the current alarm state.</p> </li> <li> <p> <code>missing</code> - Missing data is treated as missing.</p> </li> </ul> <p>If <code>treatMissingData</code> is not specified, the default behavior of <code>missing</code> is used.</p>"""
    contact_protocols: NotRequired[
        "capo_lightsail.types.contact_protocols_list.ContactProtocolsList"
    ]
    """<p>The contact protocols to use for the alarm, such as <code>Email</code>, <code>SMS</code> (text messaging), or both.</p> <p>A notification is sent via the specified contact protocol if notifications are enabled for the alarm, and when the alarm is triggered.</p> <p>A notification is not sent if a contact protocol is not specified, if the specified contact protocol is not configured in the Amazon Web Services Region, or if notifications are not enabled for the alarm using the <code>notificationEnabled</code> paramater.</p> <p>Use the <code>CreateContactMethod</code> action to configure a contact protocol in an Amazon Web Services Region.</p>"""
    notification_triggers: NotRequired[
        "capo_lightsail.types.notification_trigger_list.NotificationTriggerList"
    ]
    """<p>The alarm states that trigger a notification.</p> <p>An alarm has the following possible states:</p> <ul> <li> <p> <code>ALARM</code> - The metric is outside of the defined threshold.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.</p> </li> <li> <p> <code>OK</code> - The metric is within the defined threshold.</p> </li> </ul> <p>When you specify a notification trigger, the <code>ALARM</code> state must be specified. The <code>INSUFFICIENT_DATA</code> and <code>OK</code> states can be specified in addition to the <code>ALARM</code> state.</p> <ul> <li> <p>If you specify <code>OK</code> as an alarm trigger, a notification is sent when the alarm switches from an <code>ALARM</code> or <code>INSUFFICIENT_DATA</code> alarm state to an <code>OK</code> state. This can be thought of as an <i>all clear</i> alarm notification.</p> </li> <li> <p>If you specify <code>INSUFFICIENT_DATA</code> as the alarm trigger, a notification is sent when the alarm switches from an <code>OK</code> or <code>ALARM</code> alarm state to an <code>INSUFFICIENT_DATA</code> state.</p> </li> </ul> <p>The notification trigger defaults to <code>ALARM</code> if you don't specify this parameter.</p>"""
    notification_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the alarm is enabled.</p> <p>Notifications are enabled by default if you don't specify this parameter.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the alarm during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAlarmRequest) -> dict:
    out: dict = {}
    out["alarmName"] = value["alarm_name"]
    import capo_lightsail.types.metric_name

    out["metricName"] = capo_lightsail.types.metric_name.serialize_aws_json_1_1(
        value["metric_name"]
    )
    out["monitoredResourceName"] = value["monitored_resource_name"]
    import capo_lightsail.types.comparison_operator

    out["comparisonOperator"] = (
        capo_lightsail.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    out["threshold"] = (
        "NaN"
        if value["threshold"] != value["threshold"]
        else "Infinity"
        if value["threshold"] == float("inf")
        else "-Infinity"
        if value["threshold"] == float("-inf")
        else value["threshold"]
    )
    out["evaluationPeriods"] = value["evaluation_periods"]
    if "datapoints_to_alarm" in value:
        out["datapointsToAlarm"] = value["datapoints_to_alarm"]
    if "treat_missing_data" in value:
        import capo_lightsail.types.treat_missing_data

        out["treatMissingData"] = (
            capo_lightsail.types.treat_missing_data.serialize_aws_json_1_1(
                value["treat_missing_data"]
            )
        )
    if "contact_protocols" in value:
        import capo_lightsail.types.contact_protocols_list

        out["contactProtocols"] = (
            capo_lightsail.types.contact_protocols_list.serialize_aws_json_1_1(
                value["contact_protocols"]
            )
        )
    if "notification_triggers" in value:
        import capo_lightsail.types.notification_trigger_list

        out["notificationTriggers"] = (
            capo_lightsail.types.notification_trigger_list.serialize_aws_json_1_1(
                value["notification_triggers"]
            )
        )
    if "notification_enabled" in value:
        out["notificationEnabled"] = value["notification_enabled"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAlarmRequest:
    out: PutAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        raise DeserializationError("PutAlarmRequest.alarm_name required")
    if data.get("metricName") is not None:
        import capo_lightsail.types.metric_name

        out["metric_name"] = capo_lightsail.types.metric_name.deserialize_aws_json_1_1(
            data["metricName"]
        )
    else:
        raise DeserializationError("PutAlarmRequest.metric_name required")
    if data.get("monitoredResourceName") is not None:
        out["monitored_resource_name"] = data["monitoredResourceName"]
    else:
        raise DeserializationError("PutAlarmRequest.monitored_resource_name required")
    if data.get("comparisonOperator") is not None:
        import capo_lightsail.types.comparison_operator

        out["comparison_operator"] = (
            capo_lightsail.types.comparison_operator.deserialize_aws_json_1_1(
                data["comparisonOperator"]
            )
        )
    else:
        raise DeserializationError("PutAlarmRequest.comparison_operator required")
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    else:
        raise DeserializationError("PutAlarmRequest.threshold required")
    if data.get("evaluationPeriods") is not None:
        out["evaluation_periods"] = data["evaluationPeriods"]
    else:
        raise DeserializationError("PutAlarmRequest.evaluation_periods required")
    if data.get("datapointsToAlarm") is not None:
        out["datapoints_to_alarm"] = data["datapointsToAlarm"]
    if data.get("treatMissingData") is not None:
        import capo_lightsail.types.treat_missing_data

        out["treat_missing_data"] = (
            capo_lightsail.types.treat_missing_data.deserialize_aws_json_1_1(
                data["treatMissingData"]
            )
        )
    if data.get("contactProtocols") is not None:
        import capo_lightsail.types.contact_protocols_list

        out["contact_protocols"] = (
            capo_lightsail.types.contact_protocols_list.deserialize_aws_json_1_1(
                data["contactProtocols"]
            )
        )
    if data.get("notificationTriggers") is not None:
        import capo_lightsail.types.notification_trigger_list

        out["notification_triggers"] = (
            capo_lightsail.types.notification_trigger_list.deserialize_aws_json_1_1(
                data["notificationTriggers"]
            )
        )
    if data.get("notificationEnabled") is not None:
        out["notification_enabled"] = data["notificationEnabled"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
