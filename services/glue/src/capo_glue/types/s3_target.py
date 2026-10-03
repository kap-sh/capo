"""Generated from Smithy shape ``com.amazonaws.glue#S3Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_name
    import capo_glue.types.event_queue_arn
    import capo_glue.types.nullable_integer
    import capo_glue.types.path
    import capo_glue.types.path_list


class S3Target(TypedDict, closed=True):
    path: NotRequired["capo_glue.types.path.Path"]
    """<p>The path to the Amazon S3 target.</p>"""
    exclusions: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">Catalog Tables with a Crawler</a>.</p>"""
    connection_name: NotRequired["capo_glue.types.connection_name.ConnectionName"]
    """<p>The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).</p>"""
    sample_size: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.</p>"""
    event_queue_arn: NotRequired["capo_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon SQS ARN. For example, <code>arn:aws:sqs:region:account:sqs</code>.</p>"""
    dlq_event_queue_arn: NotRequired["capo_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon dead-letter SQS ARN. For example, <code>arn:aws:sqs:region:account:deadLetterQueue</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Target) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "exclusions" in value:
        import capo_glue.types.path_list

        out["Exclusions"] = capo_glue.types.path_list.serialize_aws_json_1_1(
            value["exclusions"]
        )
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "sample_size" in value:
        out["SampleSize"] = value["sample_size"]
    if "event_queue_arn" in value:
        out["EventQueueArn"] = value["event_queue_arn"]
    if "dlq_event_queue_arn" in value:
        out["DlqEventQueueArn"] = value["dlq_event_queue_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Target:
    out: S3Target = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Exclusions") is not None:
        import capo_glue.types.path_list

        out["exclusions"] = capo_glue.types.path_list.deserialize_aws_json_1_1(
            data["Exclusions"]
        )
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("SampleSize") is not None:
        out["sample_size"] = data["SampleSize"]
    if data.get("EventQueueArn") is not None:
        out["event_queue_arn"] = data["EventQueueArn"]
    if data.get("DlqEventQueueArn") is not None:
        out["dlq_event_queue_arn"] = data["DlqEventQueueArn"]
    return out
