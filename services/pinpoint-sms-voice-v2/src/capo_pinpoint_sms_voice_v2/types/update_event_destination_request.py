"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.event_destination_name
    import capo_pinpoint_sms_voice_v2.types.event_type_list
    import capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination
    import capo_pinpoint_sms_voice_v2.types.sns_destination


class UpdateEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The configuration set to update with the new event destination. Valid values for this can be the ConfigurationSetName or ConfigurationSetArn.</p>"""
    event_destination_name: (
        "capo_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName"
    )
    """<p>The name to use for the event destination.</p>"""
    enabled: NotRequired["bool"]
    """<p>When set to true logging is enabled.</p>"""
    matching_event_types: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList"
    ]
    """<p>An array of event types that determine which events to log.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>"""
    cloud_watch_logs_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    """<p>An object that contains information about an event destination that sends data to CloudWatch Logs.</p>"""
    kinesis_firehose_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Firehose.</p>"""
    sns_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
    ]
    """<p>An object that contains information about an event destination that sends data to Amazon SNS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEventDestinationRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["EventDestinationName"] = value["event_destination_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "matching_event_types" in value:
        import capo_pinpoint_sms_voice_v2.types.event_type_list

        out["MatchingEventTypes"] = (
            capo_pinpoint_sms_voice_v2.types.event_type_list.serialize_aws_json_1_0(
                value["matching_event_types"]
            )
        )
    if "cloud_watch_logs_destination" in value:
        import capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination

        out["CloudWatchLogsDestination"] = (
            capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.serialize_aws_json_1_0(
                value["cloud_watch_logs_destination"]
            )
        )
    if "kinesis_firehose_destination" in value:
        import capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.serialize_aws_json_1_0(
                value["kinesis_firehose_destination"]
            )
        )
    if "sns_destination" in value:
        import capo_pinpoint_sms_voice_v2.types.sns_destination

        out["SnsDestination"] = (
            capo_pinpoint_sms_voice_v2.types.sns_destination.serialize_aws_json_1_0(
                value["sns_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEventDestinationRequest:
    out: UpdateEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        out["configuration_set_name"] = ""
    if data.get("EventDestinationName") is not None:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        out["event_destination_name"] = ""
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("MatchingEventTypes") is not None:
        import capo_pinpoint_sms_voice_v2.types.event_type_list

        out["matching_event_types"] = (
            capo_pinpoint_sms_voice_v2.types.event_type_list.deserialize_aws_json_1_0(
                data["MatchingEventTypes"]
            )
        )
    if data.get("CloudWatchLogsDestination") is not None:
        import capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination

        out["cloud_watch_logs_destination"] = (
            capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.deserialize_aws_json_1_0(
                data["CloudWatchLogsDestination"]
            )
        )
    if data.get("KinesisFirehoseDestination") is not None:
        import capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.deserialize_aws_json_1_0(
                data["KinesisFirehoseDestination"]
            )
        )
    if data.get("SnsDestination") is not None:
        import capo_pinpoint_sms_voice_v2.types.sns_destination

        out["sns_destination"] = (
            capo_pinpoint_sms_voice_v2.types.sns_destination.deserialize_aws_json_1_0(
                data["SnsDestination"]
            )
        )
    return out
