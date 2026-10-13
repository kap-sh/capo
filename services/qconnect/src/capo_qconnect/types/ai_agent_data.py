"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.ai_agent_configuration
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.arn
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.origin
    import capo_qconnect.types.status
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid
    import capo_qconnect.types.visibility_status


class AIAgentData(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_agent_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the AI Agent.</p>"""
    ai_agent_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI agent.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Agent.</p>"""
    type: "capo_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent.</p>"""
    configuration: "capo_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    """<p>Configuration for the AI Agent.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Agent was last modified.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the AI Agent.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Agent.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    origin: NotRequired["capo_qconnect.types.origin.Origin"]
    """<p>Specifies the origin of the AI Agent. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>"""
    status: NotRequired["capo_qconnect.types.status.Status"]
    """<p>The status of the AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiAgentId"] = value["ai_agent_id"]
    out["aiAgentArn"] = value["ai_agent_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_qconnect.types.ai_agent_configuration

    out["configuration"] = capo_qconnect.types.ai_agent_configuration.serialize_json(
        value["configuration"]
    )
    if "modified_time" in value:
        import capo_qconnect.types._prelude.timestamp

        out["modifiedTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    out["visibilityStatus"] = value["visibility_status"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "origin" in value:
        out["origin"] = value["origin"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AIAgentData:
    out: AIAgentData = {}  # type: ignore[typeddict-item]
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AIAgentData.assistant_id required")
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AIAgentData.assistant_arn required")
    if data.get("aiAgentId") is not None:
        out["ai_agent_id"] = data["aiAgentId"]
    else:
        raise DeserializationError("AIAgentData.ai_agent_id required")
    if data.get("aiAgentArn") is not None:
        out["ai_agent_arn"] = data["aiAgentArn"]
    else:
        raise DeserializationError("AIAgentData.ai_agent_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AIAgentData.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AIAgentData.type required")
    if data.get("configuration") is not None:
        import capo_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("AIAgentData.configuration required")
    if data.get("modifiedTime") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["modified_time"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["modifiedTime"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("AIAgentData.visibility_status required")
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("origin") is not None:
        out["origin"] = data["origin"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out


def redact_sensitive(value: AIAgentData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
