"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorBucketPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name
    import capo_s3vectors.types.vector_bucket_policy


class PutVectorBucketPolicyInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket.</p>"""
    vector_bucket_arn: NotRequired[
        "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the vector bucket.</p>"""
    policy: "capo_s3vectors.types.vector_bucket_policy.VectorBucketPolicy"
    """<p>The <code>JSON</code> that defines the policy. For more information about bucket policies for S3 Vectors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bucket-policy.html">Managing vector bucket policies</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorBucketPolicyInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutVectorBucketPolicyInput:
    out: PutVectorBucketPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("vectorBucketArn") is not None:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutVectorBucketPolicyInput.policy required")
    return out
