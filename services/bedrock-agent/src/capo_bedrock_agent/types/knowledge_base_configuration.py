"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.kendra_knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_type
    import capo_bedrock_agent.types.managed_knowledge_base_configuration
    import capo_bedrock_agent.types.sql_knowledge_base_configuration
    import capo_bedrock_agent.types.vector_knowledge_base_configuration


class KnowledgeBaseConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of data that the data source is converted into for the knowledge base. Choose <code>MANAGED</code> to create a managed knowledge base.</p>"""
    vector_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.vector_knowledge_base_configuration.VectorKnowledgeBaseConfiguration"
    ]
    """<p>Contains details about the model that's used to convert the data source into vector embeddings.</p>"""
    managed_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.managed_knowledge_base_configuration.ManagedKnowledgeBaseConfiguration"
    ]
    """<p>Contains configuration details for a knowledge base that uses a vector store fully managed by Amazon Bedrock. Specify this object when the knowledge base type is MANAGED.</p>"""
    kendra_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.kendra_knowledge_base_configuration.KendraKnowledgeBaseConfiguration"
    ]
    """<p>Settings for an Amazon Kendra knowledge base.</p>"""
    sql_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.sql_knowledge_base_configuration.SqlKnowledgeBaseConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base connected to an SQL database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base_type

    out["type"] = capo_bedrock_agent.types.knowledge_base_type.serialize_json(
        value["type"]
    )
    if "vector_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.vector_knowledge_base_configuration

        out["vectorKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.vector_knowledge_base_configuration.serialize_json(
                value["vector_knowledge_base_configuration"]
            )
        )
    if "managed_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.managed_knowledge_base_configuration

        out["managedKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.managed_knowledge_base_configuration.serialize_json(
                value["managed_knowledge_base_configuration"]
            )
        )
    if "kendra_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.kendra_knowledge_base_configuration

        out["kendraKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.kendra_knowledge_base_configuration.serialize_json(
                value["kendra_knowledge_base_configuration"]
            )
        )
    if "sql_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.sql_knowledge_base_configuration

        out["sqlKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.sql_knowledge_base_configuration.serialize_json(
                value["sql_knowledge_base_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseConfiguration:
    out: KnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.knowledge_base_type

        out["type"] = capo_bedrock_agent.types.knowledge_base_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.knowledge_base_type.KnowledgeBaseType", ""
        )
    if data.get("vectorKnowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.vector_knowledge_base_configuration

        out["vector_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.vector_knowledge_base_configuration.deserialize_json(
                data["vectorKnowledgeBaseConfiguration"]
            )
        )
    if data.get("managedKnowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.managed_knowledge_base_configuration

        out["managed_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.managed_knowledge_base_configuration.deserialize_json(
                data["managedKnowledgeBaseConfiguration"]
            )
        )
    if data.get("kendraKnowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.kendra_knowledge_base_configuration

        out["kendra_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.kendra_knowledge_base_configuration.deserialize_json(
                data["kendraKnowledgeBaseConfiguration"]
            )
        )
    if data.get("sqlKnowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.sql_knowledge_base_configuration

        out["sql_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.sql_knowledge_base_configuration.deserialize_json(
                data["sqlKnowledgeBaseConfiguration"]
            )
        )
    return out


def redact_sensitive(value: KnowledgeBaseConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.sql_knowledge_base_configuration

        out["sql_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.sql_knowledge_base_configuration.redact_sensitive(
                value["sql_knowledge_base_configuration"]
            )
        )
    return out
