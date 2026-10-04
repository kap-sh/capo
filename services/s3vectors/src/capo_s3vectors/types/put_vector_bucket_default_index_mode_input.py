"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorBucketDefaultIndexModeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name


class PutVectorBucketDefaultIndexModeInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket to update.</p>"""
    vector_bucket_arn: NotRequired[
        "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the vector bucket to update.</p>"""
    default_index_mode: "capo_s3vectors.types.index_mode.IndexMode"
    """<p>The default mode to assign to new vector indexes in the vector bucket. This change doesn't affect existing vector indexes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorBucketDefaultIndexModeInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    import capo_s3vectors.types.index_mode

    out["defaultIndexMode"] = capo_s3vectors.types.index_mode.serialize_json(
        value["default_index_mode"]
    )
    return out


def deserialize_json(data: dict) -> PutVectorBucketDefaultIndexModeInput:
    out: PutVectorBucketDefaultIndexModeInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("vectorBucketArn") is not None:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if data.get("defaultIndexMode") is not None:
        import capo_s3vectors.types.index_mode

        out["default_index_mode"] = capo_s3vectors.types.index_mode.deserialize_json(
            data["defaultIndexMode"]
        )
    else:
        raise DeserializationError(
            "PutVectorBucketDefaultIndexModeInput.default_index_mode required"
        )
    return out
