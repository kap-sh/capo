"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.query_vectors_next_token
    import capo_s3vectors.types.top_k
    import capo_s3vectors.types.vector_bucket_name
    import capo_s3vectors.types.vector_data


class QueryVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index that you want to query. </p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The ARN of the vector index that you want to query.</p>"""
    top_k: "capo_s3vectors.types.top_k.TopK"
    """<p>The number of results to return for each query.</p>"""
    query_vector: "capo_s3vectors.types.vector_data.VectorData"
    """<p>The query vector. Ensure that the query vector has the same dimension as the dimension of the vector index that's being queried. For example, if your vector index contains vectors with 384 dimensions, your query vector must also have 384 dimensions. </p>"""
    filter: NotRequired["object"]
    """<p>Metadata filter to apply during the query. For more information about metadata keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-metadata-filtering.html">Metadata filtering</a> in the <i>Amazon S3 User Guide</i>. </p>"""
    return_metadata: "bool"
    """<p>Indicates whether to include metadata in the response. The default value is <code>false</code>.</p>"""
    return_distance: "bool"
    """<p>Indicates whether to include the computed distance in the response. The default value is <code>false</code>.</p>"""
    next_token: NotRequired[
        "capo_s3vectors.types.query_vectors_next_token.QueryVectorsNextToken"
    ]
    """<p>Pagination token from a previous request. The value of this field is empty for an initial request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    out["topK"] = value["top_k"]
    import capo_s3vectors.types.vector_data

    out["queryVector"] = capo_s3vectors.types.vector_data.serialize_json(
        value["query_vector"]
    )
    if "filter" in value:
        out["filter"] = value["filter"]
    out["returnMetadata"] = value.get("return_metadata", False)
    out["returnDistance"] = value.get("return_distance", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> QueryVectorsInput:
    out: QueryVectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    else:
        raise DeserializationError("QueryVectorsInput.top_k required")
    if data.get("queryVector") is not None:
        import capo_s3vectors.types.vector_data

        out["query_vector"] = capo_s3vectors.types.vector_data.deserialize_json(
            data["queryVector"]
        )
    else:
        raise DeserializationError("QueryVectorsInput.query_vector required")
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    if data.get("returnMetadata") is not None:
        out["return_metadata"] = data["returnMetadata"]
    else:
        out["return_metadata"] = False
    if data.get("returnDistance") is not None:
        out["return_distance"] = data["returnDistance"]
    else:
        out["return_distance"] = False
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
