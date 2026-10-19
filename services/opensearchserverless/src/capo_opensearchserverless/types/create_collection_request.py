"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_type
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.encryption_config
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags
    import capo_opensearchserverless.types.vector_options


class CreateCollectionRequest(TypedDict, closed=True):
    name: "capo_opensearchserverless.types.collection_name.CollectionName"
    """<p>Name of the collection.</p>"""
    type: NotRequired["capo_opensearchserverless.types.collection_type.CollectionType"]
    """<p>The type of collection.</p>"""
    description: NotRequired["str"]
    """<p>Description of the collection.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>"""
    standby_replicas: NotRequired[
        "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Indicates whether standby replicas should be used for a collection.</p>"""
    vector_options: NotRequired[
        "capo_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    collection_group_name: NotRequired[
        "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group to associate with the collection.</p>"""
    encryption_config: NotRequired[
        "capo_opensearchserverless.types.encryption_config.EncryptionConfig"
    ]
    """<p>Encryption settings for the collection.</p>"""
    deletion_protection: NotRequired[
        "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "vector_options" in value:
        import capo_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            capo_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    if "encryption_config" in value:
        import capo_opensearchserverless.types.encryption_config

        out["encryptionConfig"] = (
            capo_opensearchserverless.types.encryption_config.serialize_aws_json_1_0(
                value["encryption_config"]
            )
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionRequest:
    out: CreateCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("standbyReplicas") is not None:
        out["standby_replicas"] = data["standbyReplicas"]
    if data.get("vectorOptions") is not None:
        import capo_opensearchserverless.types.vector_options

        out["vector_options"] = (
            capo_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if data.get("collectionGroupName") is not None:
        out["collection_group_name"] = data["collectionGroupName"]
    if data.get("encryptionConfig") is not None:
        import capo_opensearchserverless.types.encryption_config

        out["encryption_config"] = (
            capo_opensearchserverless.types.encryption_config.deserialize_aws_json_1_0(
                data["encryptionConfig"]
            )
        )
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
