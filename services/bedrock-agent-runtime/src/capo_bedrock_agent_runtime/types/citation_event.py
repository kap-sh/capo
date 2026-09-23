"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CitationEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.citation
    import capo_bedrock_agent_runtime.types.generated_response_part
    import capo_bedrock_agent_runtime.types.retrieved_references


class CitationEvent(TypedDict, closed=True):
    citation: NotRequired["capo_bedrock_agent_runtime.types.citation.Citation"]
    """<p>The citation.</p>"""
    generated_response_part: NotRequired[
        "capo_bedrock_agent_runtime.types.generated_response_part.GeneratedResponsePart"
    ]
    """<p>The generated response to the citation event.</p>"""
    retrieved_references: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieved_references.RetrievedReferences"
    ]
    """<p>The retrieved references of the citation event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationEvent) -> dict:
    out: dict = {}
    if "citation" in value:
        import capo_bedrock_agent_runtime.types.citation

        out["citation"] = capo_bedrock_agent_runtime.types.citation.serialize_json(
            value["citation"]
        )
    if "generated_response_part" in value:
        import capo_bedrock_agent_runtime.types.generated_response_part

        out["generatedResponsePart"] = (
            capo_bedrock_agent_runtime.types.generated_response_part.serialize_json(
                value["generated_response_part"]
            )
        )
    if "retrieved_references" in value:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrievedReferences"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.serialize_json(
                value["retrieved_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> CitationEvent:
    out: CitationEvent = {}  # type: ignore[typeddict-item]
    if data.get("citation") is not None:
        import capo_bedrock_agent_runtime.types.citation

        out["citation"] = capo_bedrock_agent_runtime.types.citation.deserialize_json(
            data["citation"]
        )
    if data.get("generatedResponsePart") is not None:
        import capo_bedrock_agent_runtime.types.generated_response_part

        out["generated_response_part"] = (
            capo_bedrock_agent_runtime.types.generated_response_part.deserialize_json(
                data["generatedResponsePart"]
            )
        )
    if data.get("retrievedReferences") is not None:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.deserialize_json(
                data["retrievedReferences"]
            )
        )
    return out


def serialize_event_json(value: CitationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "citation",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CitationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CitationEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
