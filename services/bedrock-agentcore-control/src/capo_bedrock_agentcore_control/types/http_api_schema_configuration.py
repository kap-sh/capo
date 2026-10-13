"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpApiSchemaConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_schema_configuration


class HttpApiSchemaConfiguration(TypedDict, closed=True):
    source: "capo_bedrock_agentcore_control.types.api_schema_configuration.ApiSchemaConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: HttpApiSchemaConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.api_schema_configuration

    out["source"] = (
        capo_bedrock_agentcore_control.types.api_schema_configuration.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> HttpApiSchemaConfiguration:
    out: HttpApiSchemaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        out["source"] = (
            capo_bedrock_agentcore_control.types.api_schema_configuration.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("HttpApiSchemaConfiguration.source required")
    return out


def redact_sensitive(value: HttpApiSchemaConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        out["source"] = (
            capo_bedrock_agentcore_control.types.api_schema_configuration.redact_sensitive(
                value["source"]
            )
        )
    return out
