"""Generated from Smithy shape ``com.amazonaws.qconnect#SendMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.client_token
    import capo_qconnect.types.conversation_context
    import capo_qconnect.types.message_configuration
    import capo_qconnect.types.message_input
    import capo_qconnect.types.message_metadata
    import capo_qconnect.types.message_type
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class SendMessageRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect session.</p>"""
    type: "capo_qconnect.types.message_type.MessageType"
    """<p>The message type.</p>"""
    message: "capo_qconnect.types.message_input.MessageInput"
    """<p>The message data to submit to the Amazon Q in Connect session.</p>"""
    ai_agent_id: NotRequired[
        "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    ]
    """<p>The identifier of the AI Agent to use for processing the message.</p>"""
    conversation_context: NotRequired[
        "capo_qconnect.types.conversation_context.ConversationContext"
    ]
    """<p>The conversation context before the Amazon Q in Connect session.</p>"""
    configuration: NotRequired[
        "capo_qconnect.types.message_configuration.MessageConfiguration"
    ]
    """<p>The configuration of the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html">SendMessage</a> request.</p>"""
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field.For more information about idempotency, see Making retries safe with idempotent APIs.</p>"""
    orchestrator_use_case: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The orchestrator use case for message processing.</p>"""
    metadata: NotRequired["capo_qconnect.types.message_metadata.MessageMetadata"]
    """<p>Additional metadata for the message.</p>"""
    origin_request_id: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Request identifier from the origin system, used for end-to-end tracing across spans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_qconnect.types.message_input

    out["message"] = capo_qconnect.types.message_input.serialize_json(value["message"])
    if "ai_agent_id" in value:
        out["aiAgentId"] = value["ai_agent_id"]
    if "conversation_context" in value:
        import capo_qconnect.types.conversation_context

        out["conversationContext"] = (
            capo_qconnect.types.conversation_context.serialize_json(
                value["conversation_context"]
            )
        )
    if "configuration" in value:
        import capo_qconnect.types.message_configuration

        out["configuration"] = capo_qconnect.types.message_configuration.serialize_json(
            value["configuration"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "orchestrator_use_case" in value:
        out["orchestratorUseCase"] = value["orchestrator_use_case"]
    if "metadata" in value:
        import capo_qconnect.types.message_metadata

        out["metadata"] = capo_qconnect.types.message_metadata.serialize_json(
            value["metadata"]
        )
    if "origin_request_id" in value:
        out["originRequestId"] = value["origin_request_id"]
    return out


def deserialize_json(data: dict) -> SendMessageRequest:
    out: SendMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SendMessageRequest.type required")
    if data.get("message") is not None:
        import capo_qconnect.types.message_input

        out["message"] = capo_qconnect.types.message_input.deserialize_json(
            data["message"]
        )
    else:
        raise DeserializationError("SendMessageRequest.message required")
    if data.get("aiAgentId") is not None:
        out["ai_agent_id"] = data["aiAgentId"]
    if data.get("conversationContext") is not None:
        import capo_qconnect.types.conversation_context

        out["conversation_context"] = (
            capo_qconnect.types.conversation_context.deserialize_json(
                data["conversationContext"]
            )
        )
    if data.get("configuration") is not None:
        import capo_qconnect.types.message_configuration

        out["configuration"] = (
            capo_qconnect.types.message_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("orchestratorUseCase") is not None:
        out["orchestrator_use_case"] = data["orchestratorUseCase"]
    if data.get("metadata") is not None:
        import capo_qconnect.types.message_metadata

        out["metadata"] = capo_qconnect.types.message_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("originRequestId") is not None:
        out["origin_request_id"] = data["originRequestId"]
    return out
