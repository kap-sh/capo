"""Generated from Smithy shape ``com.amazonaws.s3vectors#UpdateMetadataConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.metadata_configuration_add
    import capo_s3vectors.types.metadata_configuration_delete
    import capo_s3vectors.types.vector_bucket_name


class UpdateMetadataConfigurationInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index.</p>"""
    index_name: NotRequired["capo_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index to update.</p>"""
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon Resource Name (ARN) of the vector index to update.</p>"""
    add: NotRequired[
        "capo_s3vectors.types.metadata_configuration_add.MetadataConfigurationAdd"
    ]
    """<p>Text search configurations to add to the vector index.</p>"""
    delete: NotRequired[
        "capo_s3vectors.types.metadata_configuration_delete.MetadataConfigurationDelete"
    ]
    """<p>Text search configurations to delete from the vector index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMetadataConfigurationInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    if "add" in value:
        import capo_s3vectors.types.metadata_configuration_add

        out["add"] = capo_s3vectors.types.metadata_configuration_add.serialize_json(
            value["add"]
        )
    if "delete" in value:
        import capo_s3vectors.types.metadata_configuration_delete

        out["delete"] = (
            capo_s3vectors.types.metadata_configuration_delete.serialize_json(
                value["delete"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMetadataConfigurationInput:
    out: UpdateMetadataConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("vectorBucketName") is not None:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("add") is not None:
        import capo_s3vectors.types.metadata_configuration_add

        out["add"] = capo_s3vectors.types.metadata_configuration_add.deserialize_json(
            data["add"]
        )
    if data.get("delete") is not None:
        import capo_s3vectors.types.metadata_configuration_delete

        out["delete"] = (
            capo_s3vectors.types.metadata_configuration_delete.deserialize_json(
                data["delete"]
            )
        )
    return out
