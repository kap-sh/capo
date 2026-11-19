"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryVectorsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.query_text_list
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
    query_vector: NotRequired["capo_s3vectors.types.vector_data.VectorData"]
    """<p>The query vector for vector similarity search. The query vector must have the same dimension as the vector index. For example, if the vector index has 384 dimensions, the query vector must also have 384 dimensions. You can omit this parameter when you supply <code>queryTexts</code> to perform a full-text-only search. A request must include <code>queryVector</code>, <code>queryTexts</code>, or both.</p>"""
    filter: NotRequired["object"]
    """<p>Metadata filter to apply during the query. For more information about metadata keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-metadata-filtering.html">Metadata filtering</a> in the <i>Amazon S3 User Guide</i>. </p>"""
    query_mode: NotRequired["capo_s3vectors.types.index_mode.IndexMode"]
    """<p>The mode to use to process the query. If you don't specify a query mode, the operation uses the mode that's currently configured for the vector index.</p> <p>Valid values:</p> <ul> <li> <p> <code>CLASSIC</code> - Applies metadata filters during the vector search. You can't specify <code>CLASSIC</code> for an <code>ENHANCED</code> index.</p> </li> <li> <p> <code>ENHANCED</code> - Applies metadata filters before the vector search.</p> </li> </ul>"""
    return_metadata: NotRequired["bool"]
    """<p>Indicates whether to include metadata in the response. The default value is <code>false</code>.</p>"""
    return_distance: NotRequired["bool"]
    """<p>Indicates whether to include the computed distance in the response. The default value is <code>false</code>.</p>"""
    query_texts: NotRequired["capo_s3vectors.types.query_text_list.QueryTextList"]
    """<p>Full-text queries for searchable metadata keys. Omit <code>queryVector</code> to run a full-text-only search, or provide both fields to run a hybrid search. Each entry must target a distinct searchable metadata key.</p>"""
    return_scores: NotRequired["bool"]
    """<p>Indicates whether to include relevance scores in the response. Full-text-only results can include BM25 scores. Hybrid results can also include a Reciprocal Rank Fusion (RRF) score and vector distance. This setting doesn't add scores to vector-only requests. The default value is <code>false</code>.</p>"""
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
    if "query_vector" in value:
        import capo_s3vectors.types.vector_data

        out["queryVector"] = capo_s3vectors.types.vector_data.serialize_json(
            value["query_vector"]
        )
    if "filter" in value:
        out["filter"] = value["filter"]
    if "query_mode" in value:
        import capo_s3vectors.types.index_mode

        out["queryMode"] = capo_s3vectors.types.index_mode.serialize_json(
            value["query_mode"]
        )
    if "return_metadata" in value:
        out["returnMetadata"] = value["return_metadata"]
    if "return_distance" in value:
        out["returnDistance"] = value["return_distance"]
    if "query_texts" in value:
        import capo_s3vectors.types.query_text_list

        out["queryTexts"] = capo_s3vectors.types.query_text_list.serialize_json(
            value["query_texts"]
        )
    if "return_scores" in value:
        out["returnScores"] = value["return_scores"]
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
        out["top_k"] = 0
    if data.get("queryVector") is not None:
        import capo_s3vectors.types.vector_data

        out["query_vector"] = capo_s3vectors.types.vector_data.deserialize_json(
            data["queryVector"]
        )
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    if data.get("queryMode") is not None:
        import capo_s3vectors.types.index_mode

        out["query_mode"] = capo_s3vectors.types.index_mode.deserialize_json(
            data["queryMode"]
        )
    if data.get("returnMetadata") is not None:
        out["return_metadata"] = data["returnMetadata"]
    if data.get("returnDistance") is not None:
        out["return_distance"] = data["returnDistance"]
    if data.get("queryTexts") is not None:
        import capo_s3vectors.types.query_text_list

        out["query_texts"] = capo_s3vectors.types.query_text_list.deserialize_json(
            data["queryTexts"]
        )
    if data.get("returnScores") is not None:
        out["return_scores"] = data["returnScores"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: QueryVectorsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_texts" in value:
        import capo_s3vectors.types.query_text_list

        out["query_texts"] = capo_s3vectors.types.query_text_list.redact_sensitive(
            value["query_texts"]
        )
    return out
