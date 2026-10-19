"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TextPromptTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cache_point_block
    import capo_bedrock_agent.types.prompt_input_variables_list
    import capo_bedrock_agent.types.text_prompt


class TextPromptTemplateConfiguration(TypedDict, closed=True):
    text: "capo_bedrock_agent.types.text_prompt.TextPrompt"
    """<p>The message for the prompt.</p>"""
    cache_point: NotRequired[
        "capo_bedrock_agent.types.cache_point_block.CachePointBlock"
    ]
    """<p>A cache checkpoint within a template configuration.</p>"""
    input_variables: NotRequired[
        "capo_bedrock_agent.types.prompt_input_variables_list.PromptInputVariablesList"
    ]
    """<p>An array of the variables in the prompt template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextPromptTemplateConfiguration) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "cache_point" in value:
        import capo_bedrock_agent.types.cache_point_block

        out["cachePoint"] = capo_bedrock_agent.types.cache_point_block.serialize_json(
            value["cache_point"]
        )
    if "input_variables" in value:
        import capo_bedrock_agent.types.prompt_input_variables_list

        out["inputVariables"] = (
            capo_bedrock_agent.types.prompt_input_variables_list.serialize_json(
                value["input_variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextPromptTemplateConfiguration:
    out: TextPromptTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("cachePoint") is not None:
        import capo_bedrock_agent.types.cache_point_block

        out["cache_point"] = (
            capo_bedrock_agent.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        )
    if data.get("inputVariables") is not None:
        import capo_bedrock_agent.types.prompt_input_variables_list

        out["input_variables"] = (
            capo_bedrock_agent.types.prompt_input_variables_list.deserialize_json(
                data["inputVariables"]
            )
        )
    return out
