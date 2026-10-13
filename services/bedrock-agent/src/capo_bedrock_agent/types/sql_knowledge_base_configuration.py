"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SqlKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.query_engine_type
    import capo_bedrock_agent.types.redshift_configuration


class SqlKnowledgeBaseConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.query_engine_type.QueryEngineType"
    """<p>The type of SQL database to connect to the knowledge base.</p>"""
    redshift_configuration: NotRequired[
        "capo_bedrock_agent.types.redshift_configuration.RedshiftConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base connected to an Amazon Redshift database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqlKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.query_engine_type

    out["type"] = capo_bedrock_agent.types.query_engine_type.serialize_json(
        value["type"]
    )
    if "redshift_configuration" in value:
        import capo_bedrock_agent.types.redshift_configuration

        out["redshiftConfiguration"] = (
            capo_bedrock_agent.types.redshift_configuration.serialize_json(
                value["redshift_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SqlKnowledgeBaseConfiguration:
    out: SqlKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.query_engine_type

        out["type"] = capo_bedrock_agent.types.query_engine_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("SqlKnowledgeBaseConfiguration.type required")
    if data.get("redshiftConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_configuration

        out["redshift_configuration"] = (
            capo_bedrock_agent.types.redshift_configuration.deserialize_json(
                data["redshiftConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SqlKnowledgeBaseConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "redshift_configuration" in value:
        import capo_bedrock_agent.types.redshift_configuration

        out["redshift_configuration"] = (
            capo_bedrock_agent.types.redshift_configuration.redact_sensitive(
                value["redshift_configuration"]
            )
        )
    return out
