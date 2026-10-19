"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.arn_with_qualifier
    import capo_qconnect.types.channel
    import capo_qconnect.types.channel_subtype
    import capo_qconnect.types.description
    import capo_qconnect.types.generic_arn
    import capo_qconnect.types.grouping_configuration
    import capo_qconnect.types.language_code
    import capo_qconnect.types.message_template_attribute_type_list
    import capo_qconnect.types.message_template_attributes
    import capo_qconnect.types.message_template_content_provider
    import capo_qconnect.types.message_template_content_sha256
    import capo_qconnect.types.message_template_source_configuration_summary
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class MessageTemplateData(TypedDict, closed=True):
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
    created_time: "datetime.datetime"
    """<p>The timestamp when the message template was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the message template data was last modified.</p>"""
    last_modified_by: "capo_qconnect.types.generic_arn.GenericArn"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the message template data.</p>"""
    content: NotRequired[
        "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    language: NotRequired["capo_qconnect.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""
    source_configuration_summary: NotRequired[
        "capo_qconnect.types.message_template_source_configuration_summary.MessageTemplateSourceConfigurationSummary"
    ]
    """<p>The source configuration summary of the message template.</p>"""
    grouping_configuration: NotRequired[
        "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]
    default_attributes: NotRequired[
        "capo_qconnect.types.message_template_attributes.MessageTemplateAttributes"
    ]
    """<p>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</p>"""
    attribute_types: NotRequired[
        "capo_qconnect.types.message_template_attribute_type_list.MessageTemplateAttributeTypeList"
    ]
    """<p>The types of attributes that the message template contains.</p>"""
    message_template_content_sha256: "capo_qconnect.types.message_template_content_sha256.MessageTemplateContentSha256"
    """<p>The checksum value of the message template content that is referenced by the <code>$LATEST</code> qualifier. It can be returned in <code>MessageTemplateData</code> or <code>ExtendedMessageTemplateData</code>. It’s calculated by content, language, <code>defaultAttributes</code> and <code>Attachments</code> of the message template.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateData) -> dict:
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
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "language" in value:
        out["language"] = value["language"]
    if "source_configuration_summary" in value:
        import capo_qconnect.types.message_template_source_configuration_summary

        out["sourceConfigurationSummary"] = (
            capo_qconnect.types.message_template_source_configuration_summary.serialize_json(
                value["source_configuration_summary"]
            )
        )
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "default_attributes" in value:
        import capo_qconnect.types.message_template_attributes

        out["defaultAttributes"] = (
            capo_qconnect.types.message_template_attributes.serialize_json(
                value["default_attributes"]
            )
        )
    if "attribute_types" in value:
        import capo_qconnect.types.message_template_attribute_type_list

        out["attributeTypes"] = (
            capo_qconnect.types.message_template_attribute_type_list.serialize_json(
                value["attribute_types"]
            )
        )
    out["messageTemplateContentSha256"] = value["message_template_content_sha256"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MessageTemplateData:
    out: MessageTemplateData = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplateArn") is not None:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        out["message_template_arn"] = ""
    if data.get("messageTemplateId") is not None:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        out["message_template_id"] = ""
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    if data.get("channelSubtype") is not None:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        out["channel_subtype"] = ""
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromisoformat(
            data["createdTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromisoformat(
            data["lastModifiedTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        out["last_modified_by"] = ""
    if data.get("content") is not None:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("sourceConfigurationSummary") is not None:
        import capo_qconnect.types.message_template_source_configuration_summary

        out["source_configuration_summary"] = (
            capo_qconnect.types.message_template_source_configuration_summary.deserialize_json(
                data["sourceConfigurationSummary"]
            )
        )
    if data.get("groupingConfiguration") is not None:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if data.get("defaultAttributes") is not None:
        import capo_qconnect.types.message_template_attributes

        out["default_attributes"] = (
            capo_qconnect.types.message_template_attributes.deserialize_json(
                data["defaultAttributes"]
            )
        )
    if data.get("attributeTypes") is not None:
        import capo_qconnect.types.message_template_attribute_type_list

        out["attribute_types"] = (
            capo_qconnect.types.message_template_attribute_type_list.deserialize_json(
                data["attributeTypes"]
            )
        )
    if data.get("messageTemplateContentSha256") is not None:
        out["message_template_content_sha256"] = data["messageTemplateContentSha256"]
    else:
        out["message_template_content_sha256"] = ""
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: MessageTemplateData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel" in value:
        out["channel"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.redact_sensitive(
                value["content"]
            )
        )
    if "source_configuration_summary" in value:
        import capo_qconnect.types.message_template_source_configuration_summary

        out["source_configuration_summary"] = (
            capo_qconnect.types.message_template_source_configuration_summary.redact_sensitive(
                value["source_configuration_summary"]
            )
        )
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.redact_sensitive(
                value["grouping_configuration"]
            )
        )
    if "default_attributes" in value:
        import capo_qconnect.types.message_template_attributes

        out["default_attributes"] = (
            capo_qconnect.types.message_template_attributes.redact_sensitive(
                value["default_attributes"]
            )
        )
    return out
