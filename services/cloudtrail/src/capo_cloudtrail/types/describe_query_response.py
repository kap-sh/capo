"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DescribeQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.delivery_s3_uri
    import capo_cloudtrail.types.delivery_status
    import capo_cloudtrail.types.error_message
    import capo_cloudtrail.types.prompt
    import capo_cloudtrail.types.query_statement
    import capo_cloudtrail.types.query_statistics_for_describe_query
    import capo_cloudtrail.types.query_status
    import capo_cloudtrail.types.uuid


class DescribeQueryResponse(TypedDict, closed=True):
    query_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p>The ID of the query.</p>"""
    query_string: NotRequired["capo_cloudtrail.types.query_statement.QueryStatement"]
    """<p>The SQL code of a query.</p>"""
    query_status: NotRequired["capo_cloudtrail.types.query_status.QueryStatus"]
    """<p>The status of a query. Values for <code>QueryStatus</code> include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code> </p>"""
    query_statistics: NotRequired[
        "capo_cloudtrail.types.query_statistics_for_describe_query.QueryStatisticsForDescribeQuery"
    ]
    """<p>Metadata about a query, including the number of events that were matched, the total number of events scanned, the query run time in milliseconds, and the query's creation time.</p>"""
    error_message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>The error message returned if a query failed.</p>"""
    delivery_s3_uri: NotRequired["capo_cloudtrail.types.delivery_s3_uri.DeliveryS3Uri"]
    """<p>The URI for the S3 bucket where CloudTrail delivered query results, if applicable.</p>"""
    delivery_status: NotRequired["capo_cloudtrail.types.delivery_status.DeliveryStatus"]
    """<p>The delivery status.</p>"""
    prompt: NotRequired["capo_cloudtrail.types.prompt.Prompt"]
    """<p> The prompt used for a generated query. For information about generated queries, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html">Create CloudTrail Lake queries from natural language prompts</a> in the <i>CloudTrail </i> user guide. </p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryResponse) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "query_status" in value:
        import capo_cloudtrail.types.query_status

        out["QueryStatus"] = capo_cloudtrail.types.query_status.serialize_aws_json_1_1(
            value["query_status"]
        )
    if "query_statistics" in value:
        import capo_cloudtrail.types.query_statistics_for_describe_query

        out["QueryStatistics"] = (
            capo_cloudtrail.types.query_statistics_for_describe_query.serialize_aws_json_1_1(
                value["query_statistics"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "delivery_s3_uri" in value:
        out["DeliveryS3Uri"] = value["delivery_s3_uri"]
    if "delivery_status" in value:
        import capo_cloudtrail.types.delivery_status

        out["DeliveryStatus"] = (
            capo_cloudtrail.types.delivery_status.serialize_aws_json_1_1(
                value["delivery_status"]
            )
        )
    if "prompt" in value:
        out["Prompt"] = value["prompt"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryResponse:
    out: DescribeQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    if data.get("QueryStatus") is not None:
        import capo_cloudtrail.types.query_status

        out["query_status"] = (
            capo_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    if data.get("QueryStatistics") is not None:
        import capo_cloudtrail.types.query_statistics_for_describe_query

        out["query_statistics"] = (
            capo_cloudtrail.types.query_statistics_for_describe_query.deserialize_aws_json_1_1(
                data["QueryStatistics"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("DeliveryS3Uri") is not None:
        out["delivery_s3_uri"] = data["DeliveryS3Uri"]
    if data.get("DeliveryStatus") is not None:
        import capo_cloudtrail.types.delivery_status

        out["delivery_status"] = (
            capo_cloudtrail.types.delivery_status.deserialize_aws_json_1_1(
                data["DeliveryStatus"]
            )
        )
    if data.get("Prompt") is not None:
        out["prompt"] = data["Prompt"]
    if data.get("EventDataStoreOwnerAccountId") is not None:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
