"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.channel_subtype
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.grouping_configuration
    import capo_qconnect.types.language_code
    import capo_qconnect.types.message_template_attributes
    import capo_qconnect.types.message_template_content_provider
    import capo_qconnect.types.message_template_source_configuration
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid_or_arn


class CreateMessageTemplateRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: NotRequired["capo_qconnect.types.name.Name"]
    """<p>The name of the message template.</p>"""
    content: NotRequired[
        "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    channel_subtype: "capo_qconnect.types.channel_subtype.ChannelSubtype"
    """<p>The channel subtype this message template applies to.</p>"""
    language: NotRequired["capo_qconnect.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""
    source_configuration: NotRequired[
        "capo_qconnect.types.message_template_source_configuration.MessageTemplateSourceConfiguration"
    ]
    """<p>The source configuration of the message template. Only set this argument for WHATSAPP channel subtype.</p>"""
    default_attributes: NotRequired[
        "capo_qconnect.types.message_template_attributes.MessageTemplateAttributes"
    ]
    """<p>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</p>"""
    grouping_configuration: NotRequired[
        "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    out["channelSubtype"] = value["channel_subtype"]
    if "language" in value:
        out["language"] = value["language"]
    if "source_configuration" in value:
        import capo_qconnect.types.message_template_source_configuration

        out["sourceConfiguration"] = (
            capo_qconnect.types.message_template_source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "default_attributes" in value:
        import capo_qconnect.types.message_template_attributes

        out["defaultAttributes"] = (
            capo_qconnect.types.message_template_attributes.serialize_json(
                value["default_attributes"]
            )
        )
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateRequest:
    out: CreateMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("content") is not None:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("channelSubtype") is not None:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError(
            "CreateMessageTemplateRequest.channel_subtype required"
        )
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("sourceConfiguration") is not None:
        import capo_qconnect.types.message_template_source_configuration

        out["source_configuration"] = (
            capo_qconnect.types.message_template_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if data.get("defaultAttributes") is not None:
        import capo_qconnect.types.message_template_attributes

        out["default_attributes"] = (
            capo_qconnect.types.message_template_attributes.deserialize_json(
                data["defaultAttributes"]
            )
        )
    if data.get("groupingConfiguration") is not None:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
