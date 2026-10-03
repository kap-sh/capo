"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.tags_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "capo_s3vectors.types.tags_map.TagsMap"
    """<p>The user-defined tags that are applied to the S3 Vectors resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import capo_s3vectors.types.tags_map

    out["tags"] = capo_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_s3vectors.types.tags_map

        out["tags"] = capo_s3vectors.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    return out
