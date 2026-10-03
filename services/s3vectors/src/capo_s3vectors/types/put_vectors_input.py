"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.put_vectors_input_list
    import capo_s3vectors.types.vector_bucket_name


class PutVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index where you want to write vectors. </p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The ARN of the vector index where you want to write vectors.</p>"""
    vectors: "capo_s3vectors.types.put_vectors_input_list.PutVectorsInputList"
    """<p>The vectors to add to a vector index. The number of vectors in a single request must not exceed the resource capacity, otherwise the request will be rejected with the error <code>ServiceUnavailableException</code> with the error message "Currently unable to handle the request".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    import capo_s3vectors.types.put_vectors_input_list

    out["vectors"] = capo_s3vectors.types.put_vectors_input_list.serialize_json(
        value["vectors"]
    )
    return out


def deserialize_json(data: dict) -> PutVectorsInput:
    out: PutVectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("vectors") is not None:
        import capo_s3vectors.types.put_vectors_input_list

        out["vectors"] = capo_s3vectors.types.put_vectors_input_list.deserialize_json(
            data["vectors"]
        )
    else:
        raise DeserializationError("PutVectorsInput.vectors required")
    return out
