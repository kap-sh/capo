"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.failure_reasons
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_arn
    import capo_bedrock_agent.types.knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_role_arn
    import capo_bedrock_agent.types.knowledge_base_status
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.storage_configuration


class KnowledgeBase(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_arn: "capo_bedrock_agent.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the knowledge base.</p>"""
    role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>"""
    knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    """<p>Contains details about the embeddings configuration of the knowledge base.</p>"""
    storage_configuration: NotRequired[
        "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
    ]
    """<p>Contains details about the storage configuration of the knowledge base.</p>"""
    status: "capo_bedrock_agent.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base. The following statuses are possible:</p> <ul> <li> <p>CREATING – The knowledge base is being created.</p> </li> <li> <p>ACTIVE – The knowledge base is ready to be queried.</p> </li> <li> <p>DELETING – The knowledge base is being deleted.</p> </li> <li> <p>UPDATING – The knowledge base is being updated.</p> </li> <li> <p>FAILED – The knowledge base API operation failed.</p> </li> </ul>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the knowledge base was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the knowledge base was last updated.</p>"""
    failure_reasons: NotRequired[
        "capo_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>A list of reasons that the API operation on the knowledge base failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBase) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import capo_bedrock_agent.types.knowledge_base_configuration

    out["knowledgeBaseConfiguration"] = (
        capo_bedrock_agent.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "storage_configuration" in value:
        import capo_bedrock_agent.types.storage_configuration

        out["storageConfiguration"] = (
            capo_bedrock_agent.types.storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    import capo_bedrock_agent.types.knowledge_base_status

    out["status"] = capo_bedrock_agent.types.knowledge_base_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "failure_reasons" in value:
        import capo_bedrock_agent.types.failure_reasons

        out["failureReasons"] = capo_bedrock_agent.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBase:
    out: KnowledgeBase = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("knowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent.types.knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBase.knowledge_base_configuration required"
        )
    if data.get("storageConfiguration") is not None:
        import capo_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            capo_bedrock_agent.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_bedrock_agent.types.knowledge_base_status

        out["status"] = capo_bedrock_agent.types.knowledge_base_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.knowledge_base_status.KnowledgeBaseStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("failureReasons") is not None:
        import capo_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            capo_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out


def redact_sensitive(value: KnowledgeBase) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent.types.knowledge_base_configuration.redact_sensitive(
                value["knowledge_base_configuration"]
            )
        )
    if "storage_configuration" in value:
        import capo_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            capo_bedrock_agent.types.storage_configuration.redact_sensitive(
                value["storage_configuration"]
            )
        )
    return out
