"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bucket_owner_account_id
    import capo_bedrock_agent.types.s3_object_uri


class CustomS3Location(TypedDict, closed=True):
    uri: "capo_bedrock_agent.types.s3_object_uri.S3ObjectUri"
    """<p>The S3 URI of the file containing the content to ingest.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_bedrock_agent.types.bucket_owner_account_id.BucketOwnerAccountId"
    ]
    """<p>The identifier of the Amazon Web Services account that owns the S3 bucket containing the content to ingest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomS3Location) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    return out


def deserialize_json(data: dict) -> CustomS3Location:
    out: CustomS3Location = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    return out
