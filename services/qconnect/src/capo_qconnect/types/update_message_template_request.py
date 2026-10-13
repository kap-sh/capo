"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateMessageTemplateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.language_code
    import capo_qconnect.types.message_template_attributes
    import capo_qconnect.types.message_template_content_provider
    import capo_qconnect.types.message_template_source_configuration
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class UpdateMessageTemplateRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    content: NotRequired[
        "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMessageTemplateRequest) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> UpdateMessageTemplateRequest:
    out: UpdateMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
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
    return out


def redact_sensitive(value: UpdateMessageTemplateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_qconnect.types.message_template_content_provider

        out["content"] = (
            capo_qconnect.types.message_template_content_provider.redact_sensitive(
                value["content"]
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
