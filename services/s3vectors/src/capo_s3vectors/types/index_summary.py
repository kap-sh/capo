"""Generated from Smithy shape ``com.amazonaws.s3vectors#IndexSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.vector_bucket_name


class IndexSummary(TypedDict, closed=True):
    vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: "capo_s3vectors.types.index_name.IndexName"
    """<p>The name of the vector index.</p>"""
    index_arn: "capo_s3vectors.types.index_arn.IndexArn"
    """<p>The Amazon Resource Name (ARN) of the vector index.</p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector index was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexSummary) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["indexName"] = value["index_name"]
    out["indexArn"] = value["index_arn"]
    import capo_s3vectors.types._prelude.timestamp

    out["creationTime"] = capo_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> IndexSummary:
    out: IndexSummary = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        out["vector_bucket_name"] = ""
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        out["index_name"] = ""
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    else:
        out["index_arn"] = ""
    if data.get("creationTime") is not None:
        import capo_s3vectors.types._prelude.timestamp

        out["creation_time"] = capo_s3vectors.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
