"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpToolSchemaConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inline_payload
    import capo_bedrock_agentcore_control.types.s3_configuration


class _McpToolSchemaConfiguration_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class _McpToolSchemaConfiguration_inlinePayload(TypedDict, closed=True):
    inlinePayload: "capo_bedrock_agentcore_control.types.inline_payload.InlinePayload"


McpToolSchemaConfiguration: TypeAlias = (
    _McpToolSchemaConfiguration_s3
    | _McpToolSchemaConfiguration_inlinePayload
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: McpToolSchemaConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"McpToolSchemaConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "McpToolSchemaConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: McpToolSchemaConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "inlinePayload" in value:
        out["inlinePayload"] = "*** Sensitive Data Redacted ***"
    return out
