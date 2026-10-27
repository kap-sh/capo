"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionStreamS3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.sqs_arn
    import capo_opensearchserverless.types.stream_bucket_configs


class IngestionStreamS3Source(TypedDict, closed=True):
    sqs_arn: "capo_opensearchserverless.types.sqs_arn.SqsArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SQS queue that receives Amazon S3 event notifications for the source buckets.</p>"""
    buckets: NotRequired[
        "capo_opensearchserverless.types.stream_bucket_configs.StreamBucketConfigs"
    ]
    """<p>The configuration for each Amazon S3 bucket that the ingestion stream ingests data from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionStreamS3Source) -> dict:
    out: dict = {}
    out["sqsArn"] = value["sqs_arn"]
    if "buckets" in value:
        import capo_opensearchserverless.types.stream_bucket_configs

        out["buckets"] = (
            capo_opensearchserverless.types.stream_bucket_configs.serialize_aws_json_1_0(
                value["buckets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionStreamS3Source:
    out: IngestionStreamS3Source = {}  # type: ignore[typeddict-item]
    if data.get("sqsArn") is not None:
        out["sqs_arn"] = data["sqsArn"]
    else:
        out["sqs_arn"] = ""
    if data.get("buckets") is not None:
        import capo_opensearchserverless.types.stream_bucket_configs

        out["buckets"] = (
            capo_opensearchserverless.types.stream_bucket_configs.deserialize_aws_json_1_0(
                data["buckets"]
            )
        )
    return out
