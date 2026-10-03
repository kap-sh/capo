"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_input
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.user_context


class RetrieveAndGenerateStreamRequest(TypedDict, closed=True):
    session_id: NotRequired["capo_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>"""
    input: "capo_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput"
    """<p>Contains the query to be made to the knowledge base.</p>"""
    retrieve_and_generate_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
    ]
    """<p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>"""
    session_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
    ]
    """<p>Contains details about the session with the knowledge base.</p>"""
    user_context: NotRequired[
        "capo_bedrock_agent_runtime.types.user_context.UserContext"
    ]
    """<p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateStreamRequest) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_input

    out["input"] = (
        capo_bedrock_agent_runtime.types.retrieve_and_generate_input.serialize_json(
            value["input"]
        )
    )
    if "retrieve_and_generate_configuration" in value:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration

        out["retrieveAndGenerateConfiguration"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.serialize_json(
                value["retrieve_and_generate_configuration"]
            )
        )
    if "session_configuration" in value:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration

        out["sessionConfiguration"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.serialize_json(
                value["session_configuration"]
            )
        )
    if "user_context" in value:
        import capo_bedrock_agent_runtime.types.user_context

        out["userContext"] = (
            capo_bedrock_agent_runtime.types.user_context.serialize_json(
                value["user_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateStreamRequest:
    out: RetrieveAndGenerateStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("input") is not None:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_input

        out["input"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_input.deserialize_json(
                data["input"]
            )
        )
    else:
        raise DeserializationError("RetrieveAndGenerateStreamRequest.input required")
    if data.get("retrieveAndGenerateConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration

        out["retrieve_and_generate_configuration"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.deserialize_json(
                data["retrieveAndGenerateConfiguration"]
            )
        )
    if data.get("sessionConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration

        out["session_configuration"] = (
            capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.deserialize_json(
                data["sessionConfiguration"]
            )
        )
    if data.get("userContext") is not None:
        import capo_bedrock_agent_runtime.types.user_context

        out["user_context"] = (
            capo_bedrock_agent_runtime.types.user_context.deserialize_json(
                data["userContext"]
            )
        )
    return out
