"""Generated from Smithy shape ``com.amazonaws.wisdom#KnowledgeBaseData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.arn
    import capo_wisdom.types.description
    import capo_wisdom.types.knowledge_base_status
    import capo_wisdom.types.knowledge_base_type
    import capo_wisdom.types.name
    import capo_wisdom.types.rendering_configuration
    import capo_wisdom.types.server_side_encryption_configuration
    import capo_wisdom.types.source_configuration
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class KnowledgeBaseData(TypedDict, closed=True):
    knowledge_base_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    knowledge_base_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_type: "capo_wisdom.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of knowledge base.</p>"""
    status: "capo_wisdom.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base.</p>"""
    last_content_modification_time: NotRequired["datetime.datetime"]
    """<p>An epoch timestamp indicating the most recent content modification inside the knowledge base. If no content exists in a knowledge base, this value is unset.</p>"""
    source_configuration: NotRequired[
        "capo_wisdom.types.source_configuration.SourceConfiguration"
    ]
    """<p>Source configuration information about the knowledge base.</p>"""
    rendering_configuration: NotRequired[
        "capo_wisdom.types.rendering_configuration.RenderingConfiguration"
    ]
    """<p>Information about how to render the content.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>"""
    description: NotRequired["capo_wisdom.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseData) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["name"] = value["name"]
    out["knowledgeBaseType"] = value["knowledge_base_type"]
    out["status"] = value["status"]
    if "last_content_modification_time" in value:
        out["lastContentModificationTime"] = value[
            "last_content_modification_time"
        ].timestamp()
    if "source_configuration" in value:
        import capo_wisdom.types.source_configuration

        out["sourceConfiguration"] = (
            capo_wisdom.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "rendering_configuration" in value:
        import capo_wisdom.types.rendering_configuration

        out["renderingConfiguration"] = (
            capo_wisdom.types.rendering_configuration.serialize_json(
                value["rendering_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import capo_wisdom.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_wisdom.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> KnowledgeBaseData:
    out: KnowledgeBaseData = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_id required")
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("KnowledgeBaseData.name required")
    if data.get("knowledgeBaseType") is not None:
        out["knowledge_base_type"] = data["knowledgeBaseType"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("KnowledgeBaseData.status required")
    if data.get("lastContentModificationTime") is not None:
        import datetime

        out["last_content_modification_time"] = datetime.datetime.fromtimestamp(
            float(data["lastContentModificationTime"]), tz=datetime.timezone.utc
        )
    if data.get("sourceConfiguration") is not None:
        import capo_wisdom.types.source_configuration

        out["source_configuration"] = (
            capo_wisdom.types.source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if data.get("renderingConfiguration") is not None:
        import capo_wisdom.types.rendering_configuration

        out["rendering_configuration"] = (
            capo_wisdom.types.rendering_configuration.deserialize_json(
                data["renderingConfiguration"]
            )
        )
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_wisdom.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_wisdom.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out
