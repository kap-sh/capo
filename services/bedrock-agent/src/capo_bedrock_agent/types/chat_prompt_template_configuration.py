"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ChatPromptTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.messages
    import capo_bedrock_agent.types.prompt_input_variables_list
    import capo_bedrock_agent.types.system_content_blocks
    import capo_bedrock_agent.types.tool_configuration


class ChatPromptTemplateConfiguration(TypedDict, closed=True):
    messages: "capo_bedrock_agent.types.messages.Messages"
    """<p>Contains messages in the chat for the prompt.</p>"""
    system: NotRequired[
        "capo_bedrock_agent.types.system_content_blocks.SystemContentBlocks"
    ]
    """<p>Contains system prompts to provide context to the model or to describe how it should behave.</p>"""
    input_variables: NotRequired[
        "capo_bedrock_agent.types.prompt_input_variables_list.PromptInputVariablesList"
    ]
    """<p>An array of the variables in the prompt template.</p>"""
    tool_configuration: NotRequired[
        "capo_bedrock_agent.types.tool_configuration.ToolConfiguration"
    ]
    """<p>Configuration information for the tools that the model can use when generating a response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatPromptTemplateConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.messages

    out["messages"] = capo_bedrock_agent.types.messages.serialize_json(
        value["messages"]
    )
    if "system" in value:
        import capo_bedrock_agent.types.system_content_blocks

        out["system"] = capo_bedrock_agent.types.system_content_blocks.serialize_json(
            value["system"]
        )
    if "input_variables" in value:
        import capo_bedrock_agent.types.prompt_input_variables_list

        out["inputVariables"] = (
            capo_bedrock_agent.types.prompt_input_variables_list.serialize_json(
                value["input_variables"]
            )
        )
    if "tool_configuration" in value:
        import capo_bedrock_agent.types.tool_configuration

        out["toolConfiguration"] = (
            capo_bedrock_agent.types.tool_configuration.serialize_json(
                value["tool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChatPromptTemplateConfiguration:
    out: ChatPromptTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_agent.types.messages

        out["messages"] = capo_bedrock_agent.types.messages.deserialize_json(
            data["messages"]
        )
    else:
        out["messages"] = []
    if data.get("system") is not None:
        import capo_bedrock_agent.types.system_content_blocks

        out["system"] = capo_bedrock_agent.types.system_content_blocks.deserialize_json(
            data["system"]
        )
    if data.get("inputVariables") is not None:
        import capo_bedrock_agent.types.prompt_input_variables_list

        out["input_variables"] = (
            capo_bedrock_agent.types.prompt_input_variables_list.deserialize_json(
                data["inputVariables"]
            )
        )
    if data.get("toolConfiguration") is not None:
        import capo_bedrock_agent.types.tool_configuration

        out["tool_configuration"] = (
            capo_bedrock_agent.types.tool_configuration.deserialize_json(
                data["toolConfiguration"]
            )
        )
    return out
