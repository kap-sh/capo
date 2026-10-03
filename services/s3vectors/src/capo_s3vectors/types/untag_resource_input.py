"""Generated from Smithy shape ``com.amazonaws.s3vectors#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.resource_arn
    import capo_s3vectors.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're removing tags from. The tagged resource can be a vector bucket or a vector index. </p>"""
    tag_keys: "capo_s3vectors.types.tag_key_list.TagKeyList"
    """<p>The array of tag keys that you're removing from the S3 Vectors resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
