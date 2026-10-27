"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_status
    import capo_opensearchserverless.types.collection_type
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.vector_options


class UpdateCollectionDetail(TypedDict, closed=True):
    id: NotRequired["capo_opensearchserverless.types.collection_id.CollectionId"]
    """<p>The unique identifier of the collection.</p>"""
    name: NotRequired["capo_opensearchserverless.types.collection_name.CollectionName"]
    """<p>The name of the collection.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.collection_status.CollectionStatus"
    ]
    """<p>The current status of the collection.</p>"""
    type: NotRequired["capo_opensearchserverless.types.collection_type.CollectionType"]
    """<p>The collection type.</p>"""
    description: NotRequired["str"]
    """<p>The description of the collection.</p>"""
    vector_options: NotRequired[
        "capo_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Key Management Service (Amazon Web Services KMS) key used to encrypt the collection.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    created_date: NotRequired["int"]
    """<p>The date and time when the collection was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the collection was last modified.</p>"""
    deletion_protection: NotRequired[
        "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether deletion protection is <code>ENABLED</code> or <code>DISABLED</code> for the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "vector_options" in value:
        import capo_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            capo_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionDetail:
    out: UpdateCollectionDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("vectorOptions") is not None:
        import capo_opensearchserverless.types.vector_options

        out["vector_options"] = (
            capo_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdDate") is not None:
        out["created_date"] = data["createdDate"]
    if data.get("lastModifiedDate") is not None:
        out["last_modified_date"] = data["lastModifiedDate"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    return out
