"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveResultEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response
    import capo_bedrock_agent_runtime.types.agentic_retrieve_results
    import capo_bedrock_agent_runtime.types.next_token


class AgenticRetrieveResultEvent(TypedDict, closed=True):
    results: "capo_bedrock_agent_runtime.types.agentic_retrieve_results.AgenticRetrieveResults"
    """<p>The list of retrieved result items.</p>"""
    generated_response: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response.AgenticRetrieveGeneratedResponse"
    ]
    """<p>The generated response. Present only when generateResponse is true.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>Opaque continuation token for paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveResultEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_results

    out["results"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_results.serialize_json(
            value["results"]
        )
    )
    if "generated_response" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response

        out["generatedResponse"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response.serialize_json(
                value["generated_response"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveResultEvent:
    out: AgenticRetrieveResultEvent = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_results

        out["results"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_results.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    if data.get("generatedResponse") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response

        out["generated_response"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_generated_response.deserialize_json(
                data["generatedResponse"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def serialize_event_json(value: AgenticRetrieveResultEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "result",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AgenticRetrieveResultEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AgenticRetrieveResultEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
