"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.query_generation_configuration
    import capo_bedrock_agent.types.redshift_query_engine_configuration
    import capo_bedrock_agent.types.redshift_query_engine_storage_configurations


class RedshiftConfiguration(TypedDict, closed=True):
    storage_configurations: "capo_bedrock_agent.types.redshift_query_engine_storage_configurations.RedshiftQueryEngineStorageConfigurations"
    """<p>Specifies configurations for Amazon Redshift database storage.</p>"""
    query_engine_configuration: "capo_bedrock_agent.types.redshift_query_engine_configuration.RedshiftQueryEngineConfiguration"
    """<p>Specifies configurations for an Amazon Redshift query engine.</p>"""
    query_generation_configuration: NotRequired[
        "capo_bedrock_agent.types.query_generation_configuration.QueryGenerationConfiguration"
    ]
    """<p>Specifies configurations for generating queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.redshift_query_engine_storage_configurations

    out["storageConfigurations"] = (
        capo_bedrock_agent.types.redshift_query_engine_storage_configurations.serialize_json(
            value["storage_configurations"]
        )
    )
    import capo_bedrock_agent.types.redshift_query_engine_configuration

    out["queryEngineConfiguration"] = (
        capo_bedrock_agent.types.redshift_query_engine_configuration.serialize_json(
            value["query_engine_configuration"]
        )
    )
    if "query_generation_configuration" in value:
        import capo_bedrock_agent.types.query_generation_configuration

        out["queryGenerationConfiguration"] = (
            capo_bedrock_agent.types.query_generation_configuration.serialize_json(
                value["query_generation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftConfiguration:
    out: RedshiftConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageConfigurations") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_storage_configurations

        out["storage_configurations"] = (
            capo_bedrock_agent.types.redshift_query_engine_storage_configurations.deserialize_json(
                data["storageConfigurations"]
            )
        )
    else:
        out["storage_configurations"] = []
    if data.get("queryEngineConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_configuration

        out["query_engine_configuration"] = (
            capo_bedrock_agent.types.redshift_query_engine_configuration.deserialize_json(
                data["queryEngineConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftConfiguration.query_engine_configuration required"
        )
    if data.get("queryGenerationConfiguration") is not None:
        import capo_bedrock_agent.types.query_generation_configuration

        out["query_generation_configuration"] = (
            capo_bedrock_agent.types.query_generation_configuration.deserialize_json(
                data["queryGenerationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: RedshiftConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_generation_configuration" in value:
        import capo_bedrock_agent.types.query_generation_configuration

        out["query_generation_configuration"] = (
            capo_bedrock_agent.types.query_generation_configuration.redact_sensitive(
                value["query_generation_configuration"]
            )
        )
    return out
