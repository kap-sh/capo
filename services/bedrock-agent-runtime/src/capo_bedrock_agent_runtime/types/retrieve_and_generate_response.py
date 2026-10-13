"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.citations
    import capo_bedrock_agent_runtime.types.guadrail_action
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_output
    import capo_bedrock_agent_runtime.types.session_id


class RetrieveAndGenerateResponse(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>"""
    output: "capo_bedrock_agent_runtime.types.retrieve_and_generate_output.RetrieveAndGenerateOutput"
    """<p>Contains the response generated from querying the knowledge base.</p>"""
    citations: NotRequired["capo_bedrock_agent_runtime.types.citations.Citations"]
    """<p>A list of segments of the generated response that are based on sources in the knowledge base, alongside information about the sources.</p>"""
    guardrail_action: NotRequired[
        "capo_bedrock_agent_runtime.types.guadrail_action.GuadrailAction"
    ]
    """<p>Specifies if there is a guardrail intervention in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_output

    out["output"] = (
        capo_bedrock_agent_runtime.types.retrieve_and_generate_output.serialize_json(
            value["output"]
        )
    )
    if "citations" in value:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.serialize_json(
            value["citations"]
        )
    if "guardrail_action" in value:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["guardrailAction"] = (
            capo_bedrock_agent_runtime.types.guadrail_action.serialize_json(
                value["guardrail_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateResponse:
    out: RetrieveAndGenerateResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("RetrieveAndGenerateResponse.session_id required")
    if data.get("output") is not None:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_output

        out["output"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_output.deserialize_json(
                data["output"]
            )
        )
    else:
        raise DeserializationError("RetrieveAndGenerateResponse.output required")
    if data.get("citations") is not None:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.deserialize_json(
            data["citations"]
        )
    if data.get("guardrailAction") is not None:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["guardrail_action"] = (
            capo_bedrock_agent_runtime.types.guadrail_action.deserialize_json(
                data["guardrailAction"]
            )
        )
    return out


def redact_sensitive(value: RetrieveAndGenerateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output" in value:
        out["output"] = "*** Sensitive Data Redacted ***"
    if "citations" in value:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.redact_sensitive(
            value["citations"]
        )
    return out
