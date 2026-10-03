"""Generated from Smithy shape ``com.amazonaws.s3vectors#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.resource_arn
    import capo_s3vectors.types.tags_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're applying tags to. The tagged resource can be a vector bucket or a vector index. </p>"""
    tags: "capo_s3vectors.types.tags_map.TagsMap"
    """<p>The user-defined tag that you want to add to the specified S3 Vectors resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_s3vectors.types.tags_map

    out["tags"] = capo_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_s3vectors.types.tags_map

        out["tags"] = capo_s3vectors.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
