"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CreateScheduledQueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.client_token
    import capo_timestream_query.types.error_report_configuration
    import capo_timestream_query.types.notification_configuration
    import capo_timestream_query.types.query_string
    import capo_timestream_query.types.schedule_configuration
    import capo_timestream_query.types.scheduled_query_name
    import capo_timestream_query.types.string_value2048
    import capo_timestream_query.types.tag_list
    import capo_timestream_query.types.target_configuration


class CreateScheduledQueryRequest(TypedDict, closed=True):
    name: "capo_timestream_query.types.scheduled_query_name.ScheduledQueryName"
    """<p>Name of the scheduled query.</p>"""
    query_string: "capo_timestream_query.types.query_string.QueryString"
    """<p>The query string to run. Parameter names can be specified in the query string <code>@</code> character followed by an identifier. The named Parameter <code>@scheduled_runtime</code> is reserved and can be used in the query to get the time at which the query is scheduled to run.</p> <p>The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of <code>@scheduled_runtime</code> paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the <code>@scheduled_runtime</code> parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</p>"""
    schedule_configuration: (
        "capo_timestream_query.types.schedule_configuration.ScheduleConfiguration"
    )
    """<p>The schedule configuration for the query.</p>"""
    notification_configuration: "capo_timestream_query.types.notification_configuration.NotificationConfiguration"
    """<p>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it. </p>"""
    target_configuration: NotRequired[
        "capo_timestream_query.types.target_configuration.TargetConfiguration"
    ]
    """<p>Configuration used for writing the result of a query.</p>"""
    client_token: NotRequired["capo_timestream_query.types.client_token.ClientToken"]
    """<p>Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. </p> <ul> <li> <p> If CreateScheduledQuery is called without a <code>ClientToken</code>, the Query SDK generates a <code>ClientToken</code> on your behalf.</p> </li> <li> <p> After 8 hours, any request with the same <code>ClientToken</code> is treated as a new request. </p> </li> </ul>"""
    scheduled_query_execution_role_arn: (
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN for the IAM role that Timestream will assume when running the scheduled query. </p>"""
    tags: NotRequired["capo_timestream_query.types.tag_list.TagList"]
    """<p>A list of key-value pairs to label the scheduled query.</p>"""
    kms_key_id: NotRequired[
        "capo_timestream_query.types.string_value2048.StringValue2048"
    ]
    """<p>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with <i>alias/</i> </p> <p>If ErrorReportConfiguration uses <code>SSE_KMS</code> as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</p>"""
    error_report_configuration: "capo_timestream_query.types.error_report_configuration.ErrorReportConfiguration"
    """<p>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["QueryString"] = value["query_string"]
    import capo_timestream_query.types.schedule_configuration

    out["ScheduleConfiguration"] = (
        capo_timestream_query.types.schedule_configuration.serialize_aws_json_1_0(
            value["schedule_configuration"]
        )
    )
    import capo_timestream_query.types.notification_configuration

    out["NotificationConfiguration"] = (
        capo_timestream_query.types.notification_configuration.serialize_aws_json_1_0(
            value["notification_configuration"]
        )
    )
    if "target_configuration" in value:
        import capo_timestream_query.types.target_configuration

        out["TargetConfiguration"] = (
            capo_timestream_query.types.target_configuration.serialize_aws_json_1_0(
                value["target_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ScheduledQueryExecutionRoleArn"] = value["scheduled_query_execution_role_arn"]
    if "tags" in value:
        import capo_timestream_query.types.tag_list

        out["Tags"] = capo_timestream_query.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import capo_timestream_query.types.error_report_configuration

    out["ErrorReportConfiguration"] = (
        capo_timestream_query.types.error_report_configuration.serialize_aws_json_1_0(
            value["error_report_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledQueryRequest:
    out: CreateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("ScheduleConfiguration") is not None:
        import capo_timestream_query.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_timestream_query.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.schedule_configuration required"
        )
    if data.get("NotificationConfiguration") is not None:
        import capo_timestream_query.types.notification_configuration

        out["notification_configuration"] = (
            capo_timestream_query.types.notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.notification_configuration required"
        )
    if data.get("TargetConfiguration") is not None:
        import capo_timestream_query.types.target_configuration

        out["target_configuration"] = (
            capo_timestream_query.types.target_configuration.deserialize_aws_json_1_0(
                data["TargetConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ScheduledQueryExecutionRoleArn") is not None:
        out["scheduled_query_execution_role_arn"] = data[
            "ScheduledQueryExecutionRoleArn"
        ]
    else:
        out["scheduled_query_execution_role_arn"] = ""
    if data.get("Tags") is not None:
        import capo_timestream_query.types.tag_list

        out["tags"] = capo_timestream_query.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ErrorReportConfiguration") is not None:
        import capo_timestream_query.types.error_report_configuration

        out["error_report_configuration"] = (
            capo_timestream_query.types.error_report_configuration.deserialize_aws_json_1_0(
                data["ErrorReportConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.error_report_configuration required"
        )
    return out


def redact_sensitive(value: CreateScheduledQueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
