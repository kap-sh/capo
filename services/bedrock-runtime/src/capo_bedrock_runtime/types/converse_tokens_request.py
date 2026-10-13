"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseTokensRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.messages
    import capo_bedrock_runtime.types.system_content_blocks
    import capo_bedrock_runtime.types.tool_configuration


class ConverseTokensRequest(TypedDict, closed=True):
    messages: NotRequired["capo_bedrock_runtime.types.messages.Messages"]
    """<p>An array of messages to count tokens for.</p>"""
    system: NotRequired[
        "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
    ]
    """<p>The system content blocks to count tokens for. System content provides instructions or context to the model about how it should behave or respond. The token count will include any system content provided.</p>"""
    tool_config: NotRequired[
        "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
    ]
    """<p>The toolConfig of Converse input request to count tokens for. Configuration information for the tools that the model can use when generating a response.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>The additionalModelRequestFields of Converse input request to count tokens for. Use this field when you want to pass additional parameters that the model supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseTokensRequest) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_bedrock_runtime.types.messages

        out["messages"] = capo_bedrock_runtime.types.messages.serialize_json(
            value["messages"]
        )
    if "system" in value:
        import capo_bedrock_runtime.types.system_content_blocks

        out["system"] = capo_bedrock_runtime.types.system_content_blocks.serialize_json(
            value["system"]
        )
    if "tool_config" in value:
        import capo_bedrock_runtime.types.tool_configuration

        out["toolConfig"] = (
            capo_bedrock_runtime.types.tool_configuration.serialize_json(
                value["tool_config"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> ConverseTokensRequest:
    out: ConverseTokensRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_runtime.types.messages

        out["messages"] = capo_bedrock_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    if data.get("system") is not None:
        import capo_bedrock_runtime.types.system_content_blocks

        out["system"] = (
            capo_bedrock_runtime.types.system_content_blocks.deserialize_json(
                data["system"]
            )
        )
    if data.get("toolConfig") is not None:
        import capo_bedrock_runtime.types.tool_configuration

        out["tool_config"] = (
            capo_bedrock_runtime.types.tool_configuration.deserialize_json(
                data["toolConfig"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out


def redact_sensitive(value: ConverseTokensRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_bedrock_runtime.types.messages

        out["messages"] = capo_bedrock_runtime.types.messages.redact_sensitive(
            value["messages"]
        )
    if "system" in value:
        import capo_bedrock_runtime.types.system_content_blocks

        out["system"] = (
            capo_bedrock_runtime.types.system_content_blocks.redact_sensitive(
                value["system"]
            )
        )
    return out
