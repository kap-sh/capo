"""Generated from Smithy shape ``com.amazonaws.s3tables#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.resource_arn
    import capo_s3tables.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_s3tables.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're removing tags from. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p>"""
    tag_keys: "capo_s3tables.types.tag_key_list.TagKeyList"
    """<p>The array of tag keys that you're removing from the S3 Tables resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
