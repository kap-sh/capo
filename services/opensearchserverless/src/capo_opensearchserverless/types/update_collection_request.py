"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.vector_options


class UpdateCollectionRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection.</p>"""
    vector_options: NotRequired[
        "capo_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    deletion_protection: NotRequired[
        "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "vector_options" in value:
        import capo_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            capo_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionRequest:
    out: UpdateCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("vectorOptions") is not None:
        import capo_opensearchserverless.types.vector_options

        out["vector_options"] = (
            capo_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
