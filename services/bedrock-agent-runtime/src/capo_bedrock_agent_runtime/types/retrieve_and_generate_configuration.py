"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_type


class RetrieveAndGenerateConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.retrieve_and_generate_type.RetrieveAndGenerateType"
    """<p>The type of resource that contains your data for retrieving information and generating responses.</p> <note> <p>If you choose to use <code>EXTERNAL_SOURCES</code>, then currently only Anthropic Claude 3 Sonnet models for knowledge bases are supported.</p> </note>"""
    knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration.KnowledgeBaseRetrieveAndGenerateConfiguration"
    ]
    """<p>Contains details about the knowledge base for retrieving information and generating responses.</p>"""
    external_sources_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration.ExternalSourcesRetrieveAndGenerateConfiguration"
    ]
    """<p>The configuration for the external source wrapper object in the <code>retrieveAndGenerate</code> function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.retrieve_and_generate_type.serialize_json(
            value["type"]
        )
    )
    if "knowledge_base_configuration" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration

        out["knowledgeBaseConfiguration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration.serialize_json(
                value["knowledge_base_configuration"]
            )
        )
    if "external_sources_configuration" in value:
        import capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration

        out["externalSourcesConfiguration"] = (
            capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration.serialize_json(
                value["external_sources_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateConfiguration:
    out: RetrieveAndGenerateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_type.RetrieveAndGenerateType",
            "",
        )
    if data.get("knowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    if data.get("externalSourcesConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration

        out["external_sources_configuration"] = (
            capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration.deserialize_json(
                data["externalSourcesConfiguration"]
            )
        )
    return out


def redact_sensitive(value: RetrieveAndGenerateConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieve_and_generate_configuration.redact_sensitive(
                value["knowledge_base_configuration"]
            )
        )
    if "external_sources_configuration" in value:
        import capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration

        out["external_sources_configuration"] = (
            capo_bedrock_agent_runtime.types.external_sources_retrieve_and_generate_configuration.redact_sensitive(
                value["external_sources_configuration"]
            )
        )
    return out
