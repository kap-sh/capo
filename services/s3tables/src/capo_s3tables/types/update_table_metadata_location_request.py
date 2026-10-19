"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMetadataLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name
    import capo_s3tables.types.version_token


class UpdateTableMetadataLocationRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket. </p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace of the table.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table. </p>"""
    metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation"
    """<p>The new metadata location for the table. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMetadataLocationRequest) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    out["metadataLocation"] = value["metadata_location"]
    return out


def deserialize_json(data: dict) -> UpdateTableMetadataLocationRequest:
    out: UpdateTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("metadataLocation") is not None:
        out["metadata_location"] = data["metadataLocation"]
    else:
        out["metadata_location"] = ""
    return out
