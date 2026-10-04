"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorBucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_s3vectors.types.encryption_configuration
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name


class VectorBucket(TypedDict, closed=True):
    vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket. </p>"""
    vector_bucket_arn: "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    """<p>The Amazon Resource Name (ARN) of the vector bucket. </p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector bucket was created. </p>"""
    encryption_configuration: NotRequired[
        "capo_s3vectors.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the vector bucket.</p>"""
    default_index_mode: NotRequired["capo_s3vectors.types.index_mode.IndexMode"]
    """<p>The mode that is automatically assigned to new vector indexes in the vector bucket. Changing the default index mode doesn't affect existing vector indexes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorBucket) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["vectorBucketArn"] = value["vector_bucket_arn"]
    import capo_s3vectors.types._prelude.timestamp

    out["creationTime"] = capo_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "encryption_configuration" in value:
        import capo_s3vectors.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_s3vectors.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "default_index_mode" in value:
        import capo_s3vectors.types.index_mode

        out["defaultIndexMode"] = capo_s3vectors.types.index_mode.serialize_json(
            value["default_index_mode"]
        )
    return out


def deserialize_json(data: dict) -> VectorBucket:
    out: VectorBucket = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("VectorBucket.vector_bucket_name required")
    if data.get("vectorBucketArn") is not None:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    else:
        raise DeserializationError("VectorBucket.vector_bucket_arn required")
    if data.get("creationTime") is not None:
        import capo_s3vectors.types._prelude.timestamp

        out["creation_time"] = capo_s3vectors.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("VectorBucket.creation_time required")
    if data.get("encryptionConfiguration") is not None:
        import capo_s3vectors.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3vectors.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("defaultIndexMode") is not None:
        import capo_s3vectors.types.index_mode

        out["default_index_mode"] = capo_s3vectors.types.index_mode.deserialize_json(
            data["defaultIndexMode"]
        )
    return out
