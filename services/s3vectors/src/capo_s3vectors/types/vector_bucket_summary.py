"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorBucketSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name


class VectorBucketSummary(TypedDict, closed=True):
    vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket. </p>"""
    vector_bucket_arn: "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    """<p>The Amazon Resource Name (ARN) of the vector bucket. </p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector bucket was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorBucketSummary) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["vectorBucketArn"] = value["vector_bucket_arn"]
    import capo_s3vectors.types._prelude.timestamp

    out["creationTime"] = capo_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> VectorBucketSummary:
    out: VectorBucketSummary = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        out["vector_bucket_name"] = ""
    if data.get("vectorBucketArn") is not None:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    else:
        out["vector_bucket_arn"] = ""
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
