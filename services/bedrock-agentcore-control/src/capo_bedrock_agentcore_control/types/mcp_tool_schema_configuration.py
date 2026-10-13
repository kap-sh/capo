"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpToolSchemaConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inline_payload
    import capo_bedrock_agentcore_control.types.s3_configuration


class _McpToolSchemaConfiguration_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class _McpToolSchemaConfiguration_inlinePayload(TypedDict, closed=True):
    inlinePayload: "capo_bedrock_agentcore_control.types.inline_payload.InlinePayload"


McpToolSchemaConfiguration: TypeAlias = (
    _McpToolSchemaConfiguration_s3 | _McpToolSchemaConfiguration_inlinePayload
)


# --- restJson1 ser/de ---
def serialize_json(value: McpToolSchemaConfiguration) -> dict:
    if "s3" in value:
        import capo_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "inlinePayload" in value:
        return {"inlinePayload": value["inlinePayload"]}
    else:
        raise SerializationError("McpToolSchemaConfiguration: no variant present")


def deserialize_json(data: dict) -> McpToolSchemaConfiguration:
    if data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("inlinePayload") is not None:
        return {"inlinePayload": data["inlinePayload"]}
    else:
        raise DeserializationError(
            "McpToolSchemaConfiguration: no recognized variant key"
        )


def redact_sensitive(value: McpToolSchemaConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inlinePayload" in value:
        out["inlinePayload"] = "*** Sensitive Data Redacted ***"
    return out
