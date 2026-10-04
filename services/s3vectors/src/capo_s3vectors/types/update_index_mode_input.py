"""Generated from Smithy shape ``com.amazonaws.s3vectors#UpdateIndexModeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.vector_bucket_name


class UpdateIndexModeInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index.</p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index to update.</p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon Resource Name (ARN) of the vector index to update.</p>"""
    index_mode: "capo_s3vectors.types.index_mode.IndexMode"
    """<p>The new mode for the vector index.</p> <p>Valid values:</p> <ul> <li> <p> <code>CLASSIC</code> - Applies metadata filters during the vector search. You can specify <code>CLASSIC</code> only for a vector index in a vector bucket created before September 30, 2026.</p> </li> <li> <p> <code>ENHANCED</code> - Applies metadata filters before the vector search.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexModeInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    import capo_s3vectors.types.index_mode

    out["indexMode"] = capo_s3vectors.types.index_mode.serialize_json(
        value["index_mode"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIndexModeInput:
    out: UpdateIndexModeInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("indexMode") is not None:
        import capo_s3vectors.types.index_mode

        out["index_mode"] = capo_s3vectors.types.index_mode.deserialize_json(
            data["indexMode"]
        )
    else:
        raise DeserializationError("UpdateIndexModeInput.index_mode required")
    return out
