"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateIndexInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.data_type
    import capo_s3vectors.types.dimension
    import capo_s3vectors.types.distance_metric
    import capo_s3vectors.types.encryption_configuration
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.metadata_configuration
    import capo_s3vectors.types.tags_map
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name


class CreateIndexInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket to create the vector index in. </p>"""
    vector_bucket_arn: NotRequired[
        "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the vector bucket to create the vector index in.</p>"""
    index_name: "capo_s3vectors.types.index_name.IndexName"
    """<p>The name of the vector index to create. </p>"""
    data_type: "capo_s3vectors.types.data_type.DataType"
    """<p>The data type of the vectors to be inserted into the vector index. </p>"""
    dimension: "capo_s3vectors.types.dimension.Dimension"
    """<p>The dimensions of the vectors to be inserted into the vector index. </p>"""
    distance_metric: "capo_s3vectors.types.distance_metric.DistanceMetric"
    """<p>The distance metric to be used for similarity search. </p>"""
    metadata_configuration: NotRequired[
        "capo_s3vectors.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>The metadata configuration for the vector index. </p>"""
    encryption_configuration: NotRequired[
        "capo_s3vectors.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.</p>"""
    tags: NotRequired["capo_s3vectors.types.tags_map.TagsMap"]
    """<p>An array of user-defined tags that you would like to apply to the vector index that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateIndex</code> permission to create a vector index with tags.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    out["indexName"] = value["index_name"]
    import capo_s3vectors.types.data_type

    out["dataType"] = capo_s3vectors.types.data_type.serialize_json(value["data_type"])
    out["dimension"] = value["dimension"]
    import capo_s3vectors.types.distance_metric

    out["distanceMetric"] = capo_s3vectors.types.distance_metric.serialize_json(
        value["distance_metric"]
    )
    if "metadata_configuration" in value:
        import capo_s3vectors.types.metadata_configuration

        out["metadataConfiguration"] = (
            capo_s3vectors.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_s3vectors.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_s3vectors.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_s3vectors.types.tags_map

        out["tags"] = capo_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIndexInput:
    out: CreateIndexInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("vectorBucketArn") is not None:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("CreateIndexInput.index_name required")
    if data.get("dataType") is not None:
        import capo_s3vectors.types.data_type

        out["data_type"] = capo_s3vectors.types.data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("CreateIndexInput.data_type required")
    if data.get("dimension") is not None:
        out["dimension"] = data["dimension"]
    else:
        raise DeserializationError("CreateIndexInput.dimension required")
    if data.get("distanceMetric") is not None:
        import capo_s3vectors.types.distance_metric

        out["distance_metric"] = capo_s3vectors.types.distance_metric.deserialize_json(
            data["distanceMetric"]
        )
    else:
        raise DeserializationError("CreateIndexInput.distance_metric required")
    if data.get("metadataConfiguration") is not None:
        import capo_s3vectors.types.metadata_configuration

        out["metadata_configuration"] = (
            capo_s3vectors.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_s3vectors.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3vectors.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_s3vectors.types.tags_map

        out["tags"] = capo_s3vectors.types.tags_map.deserialize_json(data["tags"])
    return out
