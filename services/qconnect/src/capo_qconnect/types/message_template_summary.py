"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.arn_with_qualifier
    import capo_qconnect.types.channel
    import capo_qconnect.types.channel_subtype
    import capo_qconnect.types.description
    import capo_qconnect.types.generic_arn
    import capo_qconnect.types.message_template_source_configuration
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid
    import capo_qconnect.types.version


class MessageTemplateSummary(TypedDict, closed=True):
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
    """<p>The channel this message template applies to.</p>"""
    channel_subtype: "capo_qconnect.types.channel_subtype.ChannelSubtype"
    """<p>The channel subtype this message template applies to.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the message template was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the message template data was last modified.</p>"""
    last_modified_by: "capo_qconnect.types.generic_arn.GenericArn"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the message template data.</p>"""
    source_configuration: NotRequired[
        "capo_qconnect.types.message_template_source_configuration.MessageTemplateSourceConfiguration"
    ]
    active_version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the message template version that is activated.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSummary) -> dict:
    out: dict = {}
    out["messageTemplateArn"] = value["message_template_arn"]
    out["messageTemplateId"] = value["message_template_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    if "channel" in value:
        out["channel"] = value["channel"]
    out["channelSubtype"] = value["channel_subtype"]
    import capo_qconnect._protocol.serialize

    out["createdTime"] = capo_qconnect._protocol.serialize.fmt_date_time(
        value["created_time"]
    )
    import capo_qconnect._protocol.serialize

    out["lastModifiedTime"] = capo_qconnect._protocol.serialize.fmt_date_time(
        value["last_modified_time"]
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    if "source_configuration" in value:
        import capo_qconnect.types.message_template_source_configuration

        out["sourceConfiguration"] = (
            capo_qconnect.types.message_template_source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "active_version_number" in value:
        out["activeVersionNumber"] = value["active_version_number"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MessageTemplateSummary:
    out: MessageTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplateArn") is not None:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        raise DeserializationError(
            "MessageTemplateSummary.message_template_arn required"
        )
    if data.get("messageTemplateId") is not None:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        raise DeserializationError(
            "MessageTemplateSummary.message_template_id required"
        )
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("MessageTemplateSummary.knowledge_base_arn required")
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("MessageTemplateSummary.knowledge_base_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateSummary.name required")
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    if data.get("channelSubtype") is not None:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError("MessageTemplateSummary.channel_subtype required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromisoformat(
            data["createdTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("MessageTemplateSummary.created_time required")
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromisoformat(
            data["lastModifiedTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("MessageTemplateSummary.last_modified_time required")
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("MessageTemplateSummary.last_modified_by required")
    if data.get("sourceConfiguration") is not None:
        import capo_qconnect.types.message_template_source_configuration

        out["source_configuration"] = (
            capo_qconnect.types.message_template_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if data.get("activeVersionNumber") is not None:
        out["active_version_number"] = data["activeVersionNumber"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: MessageTemplateSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel" in value:
        out["channel"] = "*** Sensitive Data Redacted ***"
    return out
