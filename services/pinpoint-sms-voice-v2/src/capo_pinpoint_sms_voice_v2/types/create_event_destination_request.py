"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.event_destination_name
    import capo_pinpoint_sms_voice_v2.types.event_type_list
    import capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination
    import capo_pinpoint_sms_voice_v2.types.sns_destination


class CreateEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>Either the name of the configuration set or the configuration set ARN to apply event logging to. The ConfigurateSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>"""
    event_destination_name: (
        "capo_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName"
    )
    """<p>The name that identifies the event destination.</p>"""
    matching_event_types: (
        "capo_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList"
    )
    """<p>An array of event types that determine which events to log. If "ALL" is used, then End User Messaging SMS logs every event type.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>"""
    cloud_watch_logs_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Amazon CloudWatch Logs.</p>"""
    kinesis_firehose_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Amazon Data Firehose.</p>"""
    sns_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Amazon SNS.</p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEventDestinationRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["EventDestinationName"] = value["event_destination_name"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEventDestinationRequest:
    out: CreateEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "CreateEventDestinationRequest.configuration_set_name required"
        )
    if data.get("EventDestinationName") is not None:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        raise DeserializationError(
            "CreateEventDestinationRequest.event_destination_name required"
        )
    if data.get("MatchingEventTypes") is not None:
        import capo_pinpoint_sms_voice_v2.types.event_type_list

        out["matching_event_types"] = (
            capo_pinpoint_sms_voice_v2.types.event_type_list.deserialize_aws_json_1_0(
                data["MatchingEventTypes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEventDestinationRequest.matching_event_types required"
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
