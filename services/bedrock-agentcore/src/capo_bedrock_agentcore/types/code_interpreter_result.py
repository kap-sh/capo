"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterResult``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.content_block_list
    import capo_bedrock_agentcore.types.tool_result_structured_content


class CodeInterpreterResult(TypedDict, closed=True):
    content: "capo_bedrock_agentcore.types.content_block_list.ContentBlockList"
    """<p>The textual content of the execution result. This includes standard output from the code execution, such as print statements, console output, and text representations of results.</p>"""
    structured_content: NotRequired[
        "capo_bedrock_agentcore.types.tool_result_structured_content.ToolResultStructuredContent"
    ]
    """<p>The structured content of the execution result. This includes additional metadata about the execution, such as execution time, memory usage, and structured representations of output data. The format depends on the specific code interpreter and execution context.</p>"""
    is_error: NotRequired["bool"]
    """<p>Indicates whether the result represents an error. If true, the content contains error messages or exception information. If false, the content contains successful execution results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterResult) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.content_block_list

    out["content"] = capo_bedrock_agentcore.types.content_block_list.serialize_json(
        value["content"]
    )
    if "structured_content" in value:
        import capo_bedrock_agentcore.types.tool_result_structured_content

        out["structuredContent"] = (
            capo_bedrock_agentcore.types.tool_result_structured_content.serialize_json(
                value["structured_content"]
            )
        )
    if "is_error" in value:
        out["isError"] = value["is_error"]
    return out


def deserialize_json(data: dict) -> CodeInterpreterResult:
    out: CodeInterpreterResult = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.content_block_list

        out["content"] = (
            capo_bedrock_agentcore.types.content_block_list.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("CodeInterpreterResult.content required")
    if data.get("structuredContent") is not None:
        import capo_bedrock_agentcore.types.tool_result_structured_content

        out["structured_content"] = (
            capo_bedrock_agentcore.types.tool_result_structured_content.deserialize_json(
                data["structuredContent"]
            )
        )
    if data.get("isError") is not None:
        out["is_error"] = data["isError"]
    return out


def serialize_event_json(value: CodeInterpreterResult) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "result",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CodeInterpreterResult:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CodeInterpreterResult = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
