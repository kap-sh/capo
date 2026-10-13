"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolArguments``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.input_content_block_list
    import capo_bedrock_agentcore.types.language_runtime
    import capo_bedrock_agentcore.types.max_len_string
    import capo_bedrock_agentcore.types.programming_language
    import capo_bedrock_agentcore.types.string_list


class ToolArguments(TypedDict, closed=True):
    code: NotRequired["capo_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The code to execute in a code interpreter session. This is the source code in the specified programming language that will be executed by the code interpreter.</p>"""
    language: NotRequired[
        "capo_bedrock_agentcore.types.programming_language.ProgrammingLanguage"
    ]
    """<p>The programming language of the code to execute. This tells the code interpreter which language runtime to use for execution.</p>"""
    clear_context: NotRequired["bool"]
    """<p>Whether to clear the context for the tool.</p>"""
    command: NotRequired["capo_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The command to execute with the tool.</p>"""
    path: NotRequired["capo_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The path for the tool operation.</p>"""
    paths: NotRequired["capo_bedrock_agentcore.types.string_list.StringList"]
    """<p>The paths for the tool operation.</p>"""
    content: NotRequired[
        "capo_bedrock_agentcore.types.input_content_block_list.InputContentBlockList"
    ]
    """<p>The content for the tool operation.</p>"""
    directory_path: NotRequired[
        "capo_bedrock_agentcore.types.max_len_string.MaxLenString"
    ]
    """<p>The directory path for the tool operation.</p>"""
    task_id: NotRequired["capo_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The identifier of the task for the tool operation.</p>"""
    runtime: NotRequired[
        "capo_bedrock_agentcore.types.language_runtime.LanguageRuntime"
    ]
    """<p>The runtime environment to use for code execution. If not specified, defaults to <code>deno</code> for JavaScript and TypeScript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolArguments) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "language" in value:
        import capo_bedrock_agentcore.types.programming_language

        out["language"] = (
            capo_bedrock_agentcore.types.programming_language.serialize_json(
                value["language"]
            )
        )
    if "clear_context" in value:
        out["clearContext"] = value["clear_context"]
    if "command" in value:
        out["command"] = value["command"]
    if "path" in value:
        out["path"] = value["path"]
    if "paths" in value:
        import capo_bedrock_agentcore.types.string_list

        out["paths"] = capo_bedrock_agentcore.types.string_list.serialize_json(
            value["paths"]
        )
    if "content" in value:
        import capo_bedrock_agentcore.types.input_content_block_list

        out["content"] = (
            capo_bedrock_agentcore.types.input_content_block_list.serialize_json(
                value["content"]
            )
        )
    if "directory_path" in value:
        out["directoryPath"] = value["directory_path"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "runtime" in value:
        import capo_bedrock_agentcore.types.language_runtime

        out["runtime"] = capo_bedrock_agentcore.types.language_runtime.serialize_json(
            value["runtime"]
        )
    return out


def deserialize_json(data: dict) -> ToolArguments:
    out: ToolArguments = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("language") is not None:
        import capo_bedrock_agentcore.types.programming_language

        out["language"] = (
            capo_bedrock_agentcore.types.programming_language.deserialize_json(
                data["language"]
            )
        )
    if data.get("clearContext") is not None:
        out["clear_context"] = data["clearContext"]
    if data.get("command") is not None:
        out["command"] = data["command"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("paths") is not None:
        import capo_bedrock_agentcore.types.string_list

        out["paths"] = capo_bedrock_agentcore.types.string_list.deserialize_json(
            data["paths"]
        )
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.input_content_block_list

        out["content"] = (
            capo_bedrock_agentcore.types.input_content_block_list.deserialize_json(
                data["content"]
            )
        )
    if data.get("directoryPath") is not None:
        out["directory_path"] = data["directoryPath"]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("runtime") is not None:
        import capo_bedrock_agentcore.types.language_runtime

        out["runtime"] = capo_bedrock_agentcore.types.language_runtime.deserialize_json(
            data["runtime"]
        )
    return out


def redact_sensitive(value: ToolArguments) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.input_content_block_list

        out["content"] = (
            capo_bedrock_agentcore.types.input_content_block_list.redact_sensitive(
                value["content"]
            )
        )
    return out
