"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutSubscriptionFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.apply_on_transformed_logs
    import capo_cloudwatch_logs.types.destination_arn
    import capo_cloudwatch_logs.types.distribution
    import capo_cloudwatch_logs.types.emit_system_fields
    import capo_cloudwatch_logs.types.field_selection_criteria
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.role_arn


class PutSubscriptionFilterRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName"
    """<p>A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in <code>filterName</code>. To find the name of the filter currently associated with a log group, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.html">DescribeSubscriptionFilters</a>.</p>"""
    filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    """<p>A filter pattern for subscribing to a filtered stream of log events.</p>"""
    destination_arn: "capo_cloudwatch_logs.types.destination_arn.DestinationArn"
    """<p>The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:</p> <ul> <li> <p>An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.</p> <p>If you're setting up a cross-account subscription, the destination must have an IAM policy associated with it. The IAM policy must allow the sender to send logs to the destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html">PutDestinationPolicy</a>.</p> </li> <li> <p>A Kinesis Data Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>A Lambda function belonging to the same account as the subscription filter, for same-account delivery.</p> </li> </ul>"""
    role_arn: NotRequired["capo_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.</p>"""
    distribution: NotRequired["capo_cloudwatch_logs.types.distribution.Distribution"]
    """<p>The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis data stream. </p>"""
    apply_on_transformed_logs: (
        "capo_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
    )
    """<p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>.</p> <p>If the log group uses either a log-group level or account-level transformer, and you specify <code>true</code>, the subscription filter will be applied on the transformed version of the log events instead of the original ingested log events.</p>"""
    field_selection_criteria: NotRequired[
        "capo_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
    ]
    """<p>A filter expression that specifies which log events should be processed by this subscription filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like <code>=</code>, <code>!=</code>, <code>AND</code>, <code>OR</code>, <code>IN</code>, <code>NOT IN</code>. Example: <code>@aws.region NOT IN ["cn-north-1"]</code> or <code>@aws.account = "123456789012" AND @aws.region = "us-east-1"</code>. Maximum length: 2000 characters.</p>"""
    emit_system_fields: NotRequired[
        "capo_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
    ]
    """<p>A list of system fields to include in the log events sent to the subscription destination. Valid values are <code>@aws.account</code>, <code>@aws.region</code>, and <code>@source.log</code>. These fields provide source information for centralized log data in the forwarded payload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSubscriptionFilterRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["filterName"] = value["filter_name"]
    out["filterPattern"] = value["filter_pattern"]
    out["destinationArn"] = value["destination_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "distribution" in value:
        import capo_cloudwatch_logs.types.distribution

        out["distribution"] = (
            capo_cloudwatch_logs.types.distribution.serialize_aws_json_1_1(
                value["distribution"]
            )
        )
    out["applyOnTransformedLogs"] = value.get("apply_on_transformed_logs", False)
    if "field_selection_criteria" in value:
        out["fieldSelectionCriteria"] = value["field_selection_criteria"]
    if "emit_system_fields" in value:
        import capo_cloudwatch_logs.types.emit_system_fields

        out["emitSystemFields"] = (
            capo_cloudwatch_logs.types.emit_system_fields.serialize_aws_json_1_1(
                value["emit_system_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSubscriptionFilterRequest:
    out: PutSubscriptionFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError(
            "PutSubscriptionFilterRequest.log_group_name required"
        )
    if data.get("filterName") is not None:
        out["filter_name"] = data["filterName"]
    else:
        raise DeserializationError("PutSubscriptionFilterRequest.filter_name required")
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    else:
        raise DeserializationError(
            "PutSubscriptionFilterRequest.filter_pattern required"
        )
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "PutSubscriptionFilterRequest.destination_arn required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("distribution") is not None:
        import capo_cloudwatch_logs.types.distribution

        out["distribution"] = (
            capo_cloudwatch_logs.types.distribution.deserialize_aws_json_1_1(
                data["distribution"]
            )
        )
    if data.get("applyOnTransformedLogs") is not None:
        out["apply_on_transformed_logs"] = data["applyOnTransformedLogs"]
    else:
        out["apply_on_transformed_logs"] = False
    if data.get("fieldSelectionCriteria") is not None:
        out["field_selection_criteria"] = data["fieldSelectionCriteria"]
    if data.get("emitSystemFields") is not None:
        import capo_cloudwatch_logs.types.emit_system_fields

        out["emit_system_fields"] = (
            capo_cloudwatch_logs.types.emit_system_fields.deserialize_aws_json_1_1(
                data["emitSystemFields"]
            )
        )
    return out
