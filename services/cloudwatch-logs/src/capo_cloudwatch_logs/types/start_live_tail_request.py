"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.input_log_stream_names
    import capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers


class StartLiveTailRequest(TypedDict, closed=True):
    log_group_identifiers: "capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers.StartLiveTailLogGroupIdentifiers"
    """<p>An array where each item in the array is a log group to include in the Live Tail session.</p> <p>Specify each log group by its ARN. </p> <p>If you specify an ARN, the ARN can't end with an asterisk (*).</p> <note> <p> You can include up to 10 log groups.</p> </note>"""
    log_stream_names: NotRequired[
        "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
    ]
    """<p>If you specify this parameter, then only log events in the log streams that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNamePrefixes</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>"""
    log_stream_name_prefixes: NotRequired[
        "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
    ]
    """<p>If you specify this parameter, then only log events in the log streams that have names that start with the prefixes that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNames</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>"""
    log_event_filter_pattern: NotRequired[
        "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    """<p>An optional pattern to use to filter the results to include only log events that match the pattern. For example, a filter pattern of <code>error 404</code> causes only log events that include both <code>error</code> and <code>404</code> to be included in the Live Tail stream.</p> <p>Regular expression filter patterns are supported.</p> <p>For more information about filter pattern syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter and Pattern Syntax</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLiveTailRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers

    out["logGroupIdentifiers"] = (
        capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers.serialize_aws_json_1_1(
            value["log_group_identifiers"]
        )
    )
    if "log_stream_names" in value:
        import capo_cloudwatch_logs.types.input_log_stream_names

        out["logStreamNames"] = (
            capo_cloudwatch_logs.types.input_log_stream_names.serialize_aws_json_1_1(
                value["log_stream_names"]
            )
        )
    if "log_stream_name_prefixes" in value:
        import capo_cloudwatch_logs.types.input_log_stream_names

        out["logStreamNamePrefixes"] = (
            capo_cloudwatch_logs.types.input_log_stream_names.serialize_aws_json_1_1(
                value["log_stream_name_prefixes"]
            )
        )
    if "log_event_filter_pattern" in value:
        out["logEventFilterPattern"] = value["log_event_filter_pattern"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLiveTailRequest:
    out: StartLiveTailRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "StartLiveTailRequest.log_group_identifiers required"
        )
    if data.get("logStreamNames") is not None:
        import capo_cloudwatch_logs.types.input_log_stream_names

        out["log_stream_names"] = (
            capo_cloudwatch_logs.types.input_log_stream_names.deserialize_aws_json_1_1(
                data["logStreamNames"]
            )
        )
    if data.get("logStreamNamePrefixes") is not None:
        import capo_cloudwatch_logs.types.input_log_stream_names

        out["log_stream_name_prefixes"] = (
            capo_cloudwatch_logs.types.input_log_stream_names.deserialize_aws_json_1_1(
                data["logStreamNamePrefixes"]
            )
        )
    if data.get("logEventFilterPattern") is not None:
        out["log_event_filter_pattern"] = data["logEventFilterPattern"]
    return out
