"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.visibility_status


class CreateAIAgentRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Agent.</p>"""
    type: "capo_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent.</p>"""
    configuration: "capo_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    """<p>The configuration of the AI Agent.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Agent.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_qconnect.types.ai_agent_configuration

    out["configuration"] = capo_qconnect.types.ai_agent_configuration.serialize_json(
        value["configuration"]
    )
    out["visibilityStatus"] = value["visibility_status"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateAIAgentRequest:
    out: CreateAIAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAIAgentRequest.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAIAgentRequest.type required")
    if data.get("configuration") is not None:
        import capo_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAIAgentRequest.configuration required")
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("CreateAIAgentRequest.visibility_status required")
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
