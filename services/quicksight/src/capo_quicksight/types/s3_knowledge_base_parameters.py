"""Generated from Smithy shape ``com.amazonaws.quicksight#S3KnowledgeBaseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.metadata_files_location
    import capo_quicksight.types.role_arn
    import capo_quicksight.types.s3_bucket


class S3KnowledgeBaseParameters(TypedDict, closed=True):
    role_arn: NotRequired["capo_quicksight.types.role_arn.RoleArn"]
    """<p>Use the <code>RoleArn</code> structure to override an account-wide role for a specific S3 Knowledge Base data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use <code>RoleArn</code> to bypass the account-wide role and allow S3 access for the single S3 Knowledge Base data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.</p>"""
    bucket_url: "capo_quicksight.types.s3_bucket.S3Bucket"
    """<p>The URL of the S3 bucket that contains the knowledge base data.</p>"""
    metadata_files_location: NotRequired[
        "capo_quicksight.types.metadata_files_location.MetadataFilesLocation"
    ]
    """<p>The Amazon S3 location (prefix) of per-document metadata files. Each metadata file describes a single source document and its indexable attributes, such as title, category, and version. This is not the global ACL configuration file. To apply a single global ACL file to the entire knowledge base, use the access control configuration instead.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3KnowledgeBaseParameters) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    out["BucketUrl"] = value["bucket_url"]
    if "metadata_files_location" in value:
        out["MetadataFilesLocation"] = value["metadata_files_location"]
    return out


def deserialize_json(data: dict) -> S3KnowledgeBaseParameters:
    out: S3KnowledgeBaseParameters = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("BucketUrl") is not None:
        out["bucket_url"] = data["BucketUrl"]
    else:
        out["bucket_url"] = ""
    if data.get("MetadataFilesLocation") is not None:
        out["metadata_files_location"] = data["MetadataFilesLocation"]
    return out
