"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.list_vectors_max_results
    import capo_s3vectors.types.list_vectors_next_token
    import capo_s3vectors.types.list_vectors_segment_count
    import capo_s3vectors.types.list_vectors_segment_index
    import capo_s3vectors.types.vector_bucket_name


class ListVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket. </p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index.</p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon resource Name (ARN) of the vector index.</p>"""
    max_results: NotRequired[
        "capo_s3vectors.types.list_vectors_max_results.ListVectorsMaxResults"
    ]
    """<p>The maximum number of vectors to return on a page.</p> <p>If you don't specify <code>maxResults</code>, the <code>ListVectors</code> operation uses a default value of 500.</p> <p>If the processed dataset size exceeds 1 MB before reaching the <code>maxResults</code> value, the operation stops and returns the vectors that are retrieved up to that point, along with a <code>nextToken</code> that you can use in a subsequent request to retrieve the next set of results.</p>"""
    next_token: NotRequired[
        "capo_s3vectors.types.list_vectors_next_token.ListVectorsNextToken"
    ]
    """<p>Pagination token from a previous request. The value of this field is empty for an initial request.</p>"""
    segment_count: NotRequired[
        "capo_s3vectors.types.list_vectors_segment_count.ListVectorsSegmentCount"
    ]
    """<p>For a parallel <code>ListVectors</code> request, <code>segmentCount</code> represents the total number of vector segments into which the <code>ListVectors</code> operation will be divided. The value of <code>segmentCount</code> corresponds to the number of application workers that will perform the parallel <code>ListVectors</code> operation. For example, if you want to use four application threads to list vectors in a vector index, specify a <code>segmentCount</code> value of 4. </p> <p>If you specify a <code>segmentCount</code> value of 1, the <code>ListVectors</code> operation will be sequential rather than parallel.</p> <p>If you specify <code>segmentCount</code>, you must also specify <code>segmentIndex</code>.</p>"""
    segment_index: NotRequired[
        "capo_s3vectors.types.list_vectors_segment_index.ListVectorsSegmentIndex"
    ]
    """<p>For a parallel <code>ListVectors</code> request, <code>segmentIndex</code> is the index of the segment from which to list vectors in the current request. It identifies an individual segment to be listed by an application worker. </p> <p>Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to list vectors in a vector index, then the first thread specifies a <code>segmentIndex</code> value of 0, the second thread specifies 1, and so on. </p> <p>The value of <code>segmentIndex</code> must be less than the value provided for <code>segmentCount</code>. </p> <p>If you provide <code>segmentIndex</code>, you must also provide <code>segmentCount</code>.</p>"""
    return_data: NotRequired["bool"]
    """<p>If true, the vector data of each vector will be included in the response. The default value is <code>false</code>.</p>"""
    return_metadata: NotRequired["bool"]
    """<p>If true, the metadata associated with each vector will be included in the response. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "segment_count" in value:
        out["segmentCount"] = value["segment_count"]
    if "segment_index" in value:
        out["segmentIndex"] = value["segment_index"]
    if "return_data" in value:
        out["returnData"] = value["return_data"]
    if "return_metadata" in value:
        out["returnMetadata"] = value["return_metadata"]
    return out


def deserialize_json(data: dict) -> ListVectorsInput:
    out: ListVectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("segmentCount") is not None:
        out["segment_count"] = data["segmentCount"]
    if data.get("segmentIndex") is not None:
        out["segment_index"] = data["segmentIndex"]
    if data.get("returnData") is not None:
        out["return_data"] = data["returnData"]
    if data.get("returnMetadata") is not None:
        out["return_metadata"] = data["returnMetadata"]
    return out
