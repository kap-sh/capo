"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutLogEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.entity
    import capo_cloudwatch_logs.types.input_log_events
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_stream_name
    import capo_cloudwatch_logs.types.sequence_token


class PutLogEventsRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
    """<p>The name of the log stream.</p>"""
    log_events: "capo_cloudwatch_logs.types.input_log_events.InputLogEvents"
    """<p>The log events.</p>"""
    sequence_token: NotRequired[
        "capo_cloudwatch_logs.types.sequence_token.SequenceToken"
    ]
    """<p>The sequence token obtained from the response of the previous <code>PutLogEvents</code> call.</p> <important> <p>The <code>sequenceToken</code> parameter is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are now accepted and never return <code>InvalidSequenceTokenException</code> or <code>DataAlreadyAcceptedException</code> even if the sequence token is not valid.</p> </important>"""
    entity: NotRequired["capo_cloudwatch_logs.types.entity.Entity"]
    """<p>The entity associated with the log events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLogEventsRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["logStreamName"] = value["log_stream_name"]
    import capo_cloudwatch_logs.types.input_log_events

    out["logEvents"] = (
        capo_cloudwatch_logs.types.input_log_events.serialize_aws_json_1_1(
            value["log_events"]
        )
    )
    if "sequence_token" in value:
        out["sequenceToken"] = value["sequence_token"]
    if "entity" in value:
        import capo_cloudwatch_logs.types.entity

        out["entity"] = capo_cloudwatch_logs.types.entity.serialize_aws_json_1_1(
            value["entity"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLogEventsRequest:
    out: PutLogEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("logStreamName") is not None:
        out["log_stream_name"] = data["logStreamName"]
    else:
        out["log_stream_name"] = ""
    if data.get("logEvents") is not None:
        import capo_cloudwatch_logs.types.input_log_events

        out["log_events"] = (
            capo_cloudwatch_logs.types.input_log_events.deserialize_aws_json_1_1(
                data["logEvents"]
            )
        )
    else:
        out["log_events"] = []
    if data.get("sequenceToken") is not None:
        out["sequence_token"] = data["sequenceToken"]
    if data.get("entity") is not None:
        import capo_cloudwatch_logs.types.entity

        out["entity"] = capo_cloudwatch_logs.types.entity.deserialize_aws_json_1_1(
            data["entity"]
        )
    return out
