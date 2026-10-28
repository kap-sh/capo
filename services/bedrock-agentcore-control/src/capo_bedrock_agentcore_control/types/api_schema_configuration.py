"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiSchemaConfiguration``."""

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


class ApiSchemaConfigurationS3Member(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class ApiSchemaConfigurationInlinePayloadMember(TypedDict, closed=True):
    inlinePayload: "capo_bedrock_agentcore_control.types.inline_payload.InlinePayload"


ApiSchemaConfiguration: TypeAlias = (
    ApiSchemaConfigurationS3Member
    | ApiSchemaConfigurationInlinePayloadMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ApiSchemaConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ApiSchemaConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
        raise SerializationError("ApiSchemaConfiguration: no variant present")


def deserialize_json(data: dict) -> ApiSchemaConfiguration:
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("ApiSchemaConfiguration: no recognized variant key")


def redact_sensitive(value: ApiSchemaConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inlinePayload" in value:
        out["inlinePayload"] = "*** Sensitive Data Redacted ***"
    return out
