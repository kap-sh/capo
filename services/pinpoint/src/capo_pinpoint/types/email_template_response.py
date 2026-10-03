"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of_message_header
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.template_type


class EmailTemplateResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was created.</p>"""
    default_substitutions: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable.</p>"""
    html_part: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message body, in HTML format, that's used in email messages that are based on the message template.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was last modified.</p>"""
    recommender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model that's used by the message template.</p>"""
    subject: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The subject line, or title, that's used in email messages that are based on the message template.</p>"""
    headers: NotRequired[
        "capo_pinpoint.types.list_of_message_header.ListOfMessageHeader"
    ]
    """<p>The list of <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#templates-template-name-email-model-messageheader">MessageHeaders</a> for the email. You can have up to 15 Headers.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the message template.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["capo_pinpoint.types.template_type.TemplateType"]
    """<p>The type of channel that the message template is designed for. For an email template, this value is EMAIL.</p>"""
    text_part: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message body, in plain text format, that's used in email messages that are based on the message template.</p>"""
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the version parameter in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailTemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "html_part" in value:
        out["HtmlPart"] = value["html_part"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "headers" in value:
        import capo_pinpoint.types.list_of_message_header

        out["Headers"] = capo_pinpoint.types.list_of_message_header.serialize_json(
            value["headers"]
        )
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_type" in value:
        import capo_pinpoint.types.template_type

        out["TemplateType"] = capo_pinpoint.types.template_type.serialize_json(
            value["template_type"]
        )
    if "text_part" in value:
        out["TextPart"] = value["text_part"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> EmailTemplateResponse:
    out: EmailTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("DefaultSubstitutions") is not None:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if data.get("HtmlPart") is not None:
        out["html_part"] = data["HtmlPart"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("RecommenderId") is not None:
        out["recommender_id"] = data["RecommenderId"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("Headers") is not None:
        import capo_pinpoint.types.list_of_message_header

        out["headers"] = capo_pinpoint.types.list_of_message_header.deserialize_json(
            data["Headers"]
        )
    if data.get("tags") is not None:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if data.get("TemplateDescription") is not None:
        out["template_description"] = data["TemplateDescription"]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("TemplateType") is not None:
        import capo_pinpoint.types.template_type

        out["template_type"] = capo_pinpoint.types.template_type.deserialize_json(
            data["TemplateType"]
        )
    if data.get("TextPart") is not None:
        out["text_part"] = data["TextPart"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
