"""Generated from Smithy shape ``com.amazonaws.bedrockagent#S3DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bucket_owner_account_id
    import capo_bedrock_agent.types.s3_bucket_arn
    import capo_bedrock_agent.types.s3_prefixes


class S3DataSourceConfiguration(TypedDict, closed=True):
    bucket_arn: "capo_bedrock_agent.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that contains your data.</p>"""
    inclusion_prefixes: NotRequired["capo_bedrock_agent.types.s3_prefixes.S3Prefixes"]
    """<p>A list of S3 prefixes to include certain files or content. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html">Organizing objects using prefixes</a>.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_bedrock_agent.types.bucket_owner_account_id.BucketOwnerAccountId"
    ]
    """<p>The account ID for the owner of the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataSourceConfiguration) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    if "inclusion_prefixes" in value:
        import capo_bedrock_agent.types.s3_prefixes

        out["inclusionPrefixes"] = capo_bedrock_agent.types.s3_prefixes.serialize_json(
            value["inclusion_prefixes"]
        )
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    return out


def deserialize_json(data: dict) -> S3DataSourceConfiguration:
    out: S3DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    else:
        raise DeserializationError("S3DataSourceConfiguration.bucket_arn required")
    if data.get("inclusionPrefixes") is not None:
        import capo_bedrock_agent.types.s3_prefixes

        out["inclusion_prefixes"] = (
            capo_bedrock_agent.types.s3_prefixes.deserialize_json(
                data["inclusionPrefixes"]
            )
        )
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    return out
