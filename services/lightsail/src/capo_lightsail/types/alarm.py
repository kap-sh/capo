"""Generated from Smithy shape ``com.amazonaws.lightsail#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.alarm_state
    import capo_lightsail.types.boolean
    import capo_lightsail.types.comparison_operator
    import capo_lightsail.types.contact_protocols_list
    import capo_lightsail.types.double
    import capo_lightsail.types.integer
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.metric_name
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.monitored_resource_info
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.notification_trigger_list
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list
    import capo_lightsail.types.treat_missing_data


class Alarm(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the alarm.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the alarm.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the alarm was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that lists information about the location of the alarm.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type of the alarm.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail alarm. This code enables our support team to look up your Lightsail information more easily.</p>"""
    monitored_resource_info: NotRequired[
        "capo_lightsail.types.monitored_resource_info.MonitoredResourceInfo"
    ]
    """<p>An object that lists information about the resource monitored by the alarm.</p>"""
    comparison_operator: NotRequired[
        "capo_lightsail.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The arithmetic operation used when comparing the specified statistic and threshold.</p>"""
    evaluation_periods: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of periods over which data is compared to the specified threshold.</p>"""
    period: NotRequired["capo_lightsail.types.metric_period.MetricPeriod"]
    """<p>The period, in seconds, over which the statistic is applied.</p>"""
    threshold: NotRequired["capo_lightsail.types.double.double"]
    """<p>The value against which the specified statistic is compared.</p>"""
    datapoints_to_alarm: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of data points that must not within the specified threshold to trigger the alarm.</p>"""
    treat_missing_data: NotRequired[
        "capo_lightsail.types.treat_missing_data.TreatMissingData"
    ]
    """<p>Specifies how the alarm handles missing data points.</p> <p>An alarm can treat missing data in the following ways:</p> <ul> <li> <p> <code>breaching</code> - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>notBreaching</code> - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>ignore</code> - Ignore the missing data. Maintains the current alarm state.</p> </li> <li> <p> <code>missing</code> - Missing data is treated as missing.</p> </li> </ul>"""
    statistic: NotRequired["capo_lightsail.types.metric_statistic.MetricStatistic"]
    """<p>The statistic for the metric associated with the alarm.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""
    metric_name: NotRequired["capo_lightsail.types.metric_name.MetricName"]
    """<p>The name of the metric associated with the alarm.</p>"""
    state: NotRequired["capo_lightsail.types.alarm_state.AlarmState"]
    """<p>The current state of the alarm.</p> <p>An alarm has the following possible states:</p> <ul> <li> <p> <code>ALARM</code> - The metric is outside of the defined threshold.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.</p> </li> <li> <p> <code>OK</code> - The metric is within the defined threshold.</p> </li> </ul>"""
    unit: NotRequired["capo_lightsail.types.metric_unit.MetricUnit"]
    """<p>The unit of the metric associated with the alarm.</p>"""
    contact_protocols: NotRequired[
        "capo_lightsail.types.contact_protocols_list.ContactProtocolsList"
    ]
    """<p>The contact protocols for the alarm, such as <code>Email</code>, <code>SMS</code> (text messaging), or both.</p>"""
    notification_triggers: NotRequired[
        "capo_lightsail.types.notification_trigger_list.NotificationTriggerList"
    ]
    """<p>The alarm states that trigger a notification.</p>"""
    notification_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the alarm is enabled.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarm) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "monitored_resource_info" in value:
        import capo_lightsail.types.monitored_resource_info

        out["monitoredResourceInfo"] = (
            capo_lightsail.types.monitored_resource_info.serialize_aws_json_1_1(
                value["monitored_resource_info"]
            )
        )
    if "comparison_operator" in value:
        import capo_lightsail.types.comparison_operator

        out["comparisonOperator"] = (
            capo_lightsail.types.comparison_operator.serialize_aws_json_1_1(
                value["comparison_operator"]
            )
        )
    if "evaluation_periods" in value:
        out["evaluationPeriods"] = value["evaluation_periods"]
    if "period" in value:
        out["period"] = value["period"]
    if "threshold" in value:
        out["threshold"] = (
            "NaN"
            if value["threshold"] != value["threshold"]
            else "Infinity"
            if value["threshold"] == float("inf")
            else "-Infinity"
            if value["threshold"] == float("-inf")
            else value["threshold"]
        )
    if "datapoints_to_alarm" in value:
        out["datapointsToAlarm"] = value["datapoints_to_alarm"]
    if "treat_missing_data" in value:
        import capo_lightsail.types.treat_missing_data

        out["treatMissingData"] = (
            capo_lightsail.types.treat_missing_data.serialize_aws_json_1_1(
                value["treat_missing_data"]
            )
        )
    if "statistic" in value:
        import capo_lightsail.types.metric_statistic

        out["statistic"] = capo_lightsail.types.metric_statistic.serialize_aws_json_1_1(
            value["statistic"]
        )
    if "metric_name" in value:
        import capo_lightsail.types.metric_name

        out["metricName"] = capo_lightsail.types.metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    if "state" in value:
        import capo_lightsail.types.alarm_state

        out["state"] = capo_lightsail.types.alarm_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "unit" in value:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(
            value["unit"]
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


def deserialize_aws_json_1_1(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("monitoredResourceInfo") is not None:
        import capo_lightsail.types.monitored_resource_info

        out["monitored_resource_info"] = (
            capo_lightsail.types.monitored_resource_info.deserialize_aws_json_1_1(
                data["monitoredResourceInfo"]
            )
        )
    if data.get("comparisonOperator") is not None:
        import capo_lightsail.types.comparison_operator

        out["comparison_operator"] = (
            capo_lightsail.types.comparison_operator.deserialize_aws_json_1_1(
                data["comparisonOperator"]
            )
        )
    if data.get("evaluationPeriods") is not None:
        out["evaluation_periods"] = data["evaluationPeriods"]
    if data.get("period") is not None:
        out["period"] = data["period"]
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    if data.get("datapointsToAlarm") is not None:
        out["datapoints_to_alarm"] = data["datapointsToAlarm"]
    if data.get("treatMissingData") is not None:
        import capo_lightsail.types.treat_missing_data

        out["treat_missing_data"] = (
            capo_lightsail.types.treat_missing_data.deserialize_aws_json_1_1(
                data["treatMissingData"]
            )
        )
    if data.get("statistic") is not None:
        import capo_lightsail.types.metric_statistic

        out["statistic"] = (
            capo_lightsail.types.metric_statistic.deserialize_aws_json_1_1(
                data["statistic"]
            )
        )
    if data.get("metricName") is not None:
        import capo_lightsail.types.metric_name

        out["metric_name"] = capo_lightsail.types.metric_name.deserialize_aws_json_1_1(
            data["metricName"]
        )
    if data.get("state") is not None:
        import capo_lightsail.types.alarm_state

        out["state"] = capo_lightsail.types.alarm_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if data.get("unit") is not None:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
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
