"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.delete_vectors_input_list
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.vector_bucket_name


class DeleteVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index that contains a vector you want to delete.</p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The ARN of the vector index that contains a vector you want to delete.</p>"""
    keys: "capo_s3vectors.types.delete_vectors_input_list.DeleteVectorsInputList"
    """<p>The keys of the vectors to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    import capo_s3vectors.types.delete_vectors_input_list

    out["keys"] = capo_s3vectors.types.delete_vectors_input_list.serialize_json(
        value["keys"]
    )
    return out


def deserialize_json(data: dict) -> DeleteVectorsInput:
    out: DeleteVectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("keys") is not None:
        import capo_s3vectors.types.delete_vectors_input_list

        out["keys"] = capo_s3vectors.types.delete_vectors_input_list.deserialize_json(
            data["keys"]
        )
    else:
        out["keys"] = []
    return out
