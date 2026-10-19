"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.text_to_sql_configuration_type
    import capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration


class TextToSqlConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.text_to_sql_configuration_type.TextToSqlConfigurationType"
    """<p>The type of resource to use in transformation.</p>"""
    knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.TextToSqlKnowledgeBaseConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base to use in transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextToSqlConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.text_to_sql_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.text_to_sql_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "knowledge_base_configuration" in value:
        import capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration

        out["knowledgeBaseConfiguration"] = (
            capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.serialize_json(
                value["knowledge_base_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextToSqlConfiguration:
    out: TextToSqlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.text_to_sql_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.text_to_sql_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.text_to_sql_configuration_type.TextToSqlConfigurationType",
            "",
        )
    if data.get("knowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    return out
