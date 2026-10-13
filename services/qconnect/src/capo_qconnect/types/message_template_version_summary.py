"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateVersionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.arn_with_qualifier
    import capo_qconnect.types.channel
    import capo_qconnect.types.channel_subtype
    import capo_qconnect.types.name
    import capo_qconnect.types.uuid
    import capo_qconnect.types.version


class MessageTemplateVersionSummary(TypedDict, closed=True):
    message_template_arn: "capo_qconnect.types.arn_with_qualifier.ArnWithQualifier"
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    message_template_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the message template.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the message template.</p>"""
    channel: NotRequired["capo_qconnect.types.channel.Channel"]
    """<p>The channel of the message template.</p>"""
    channel_subtype: "capo_qconnect.types.channel_subtype.ChannelSubtype"
    """<p>The channel subtype this message template applies to.</p>"""
    is_active: "bool"
    """<p>Whether the version of the message template is activated.</p>"""
    version_number: "capo_qconnect.types.version.Version"
    """<p>The version number of the message template version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateVersionSummary) -> dict:
    out: dict = {}
    out["messageTemplateArn"] = value["message_template_arn"]
    out["messageTemplateId"] = value["message_template_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    if "channel" in value:
        out["channel"] = value["channel"]
    out["channelSubtype"] = value["channel_subtype"]
    out["isActive"] = value["is_active"]
    out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> MessageTemplateVersionSummary:
    out: MessageTemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplateArn") is not None:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.message_template_arn required"
        )
    if data.get("messageTemplateId") is not None:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.message_template_id required"
        )
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.knowledge_base_arn required"
        )
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.knowledge_base_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateVersionSummary.name required")
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    if data.get("channelSubtype") is not None:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.channel_subtype required"
        )
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    else:
        raise DeserializationError("MessageTemplateVersionSummary.is_active required")
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.version_number required"
        )
    return out


def redact_sensitive(value: MessageTemplateVersionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel" in value:
        out["channel"] = "*** Sensitive Data Redacted ***"
    return out
