"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ExecuteScheduledQueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.client_token
    import capo_timestream_query.types.scheduled_query_insights
    import capo_timestream_query.types.time


class ExecuteScheduledQueryRequest(TypedDict, closed=True):
    scheduled_query_arn: (
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>ARN of the scheduled query.</p>"""
    invocation_time: "capo_timestream_query.types.time.Time"
    """<p>The timestamp in UTC. Query will be run as if it was invoked at this timestamp. </p>"""
    client_token: NotRequired["capo_timestream_query.types.client_token.ClientToken"]
    """<p>Not used. </p>"""
    query_insights: NotRequired[
        "capo_timestream_query.types.scheduled_query_insights.ScheduledQueryInsights"
    ]
    """<p>Encapsulates settings for enabling <code>QueryInsights</code>.</p> <p>Enabling <code>QueryInsights</code> returns insights and metrics as a part of the Amazon SNS notification for the query that you executed. You can use <code>QueryInsights</code> to tune your query performance and cost.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    import capo_timestream_query.types.time

    out["InvocationTime"] = capo_timestream_query.types.time.serialize_aws_json_1_0(
        value["invocation_time"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "query_insights" in value:
        import capo_timestream_query.types.scheduled_query_insights

        out["QueryInsights"] = (
            capo_timestream_query.types.scheduled_query_insights.serialize_aws_json_1_0(
                value["query_insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteScheduledQueryRequest:
    out: ExecuteScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledQueryArn") is not None:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        out["scheduled_query_arn"] = ""
    if data.get("InvocationTime") is not None:
        import capo_timestream_query.types.time

        out["invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["InvocationTime"]
            )
        )
    else:
        import datetime

        out["invocation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("QueryInsights") is not None:
        import capo_timestream_query.types.scheduled_query_insights

        out["query_insights"] = (
            capo_timestream_query.types.scheduled_query_insights.deserialize_aws_json_1_0(
                data["QueryInsights"]
            )
        )
    return out


def redact_sensitive(value: ExecuteScheduledQueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
