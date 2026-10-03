"""Generated from Smithy shape ``com.amazonaws.pinpoint#VoiceTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.template_type


class VoiceTemplateResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The text of the script that's used in messages that are based on the message template, in plain text format.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was created.</p>"""
    default_substitutions: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable.</p>"""
    language_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The code for the language that's used when synthesizing the text of the script in messages that are based on the message template. For a list of supported languages and the code for each one, see the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly Developer Guide</a>.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the message template was last modified.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the message template.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the message template.</p>"""
    template_type: NotRequired["capo_pinpoint.types.template_type.TemplateType"]
    """<p>The type of channel that the message template is designed for. For a voice template, this value is VOICE.</p>"""
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the version parameter in your request.</p>"""
    voice_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the voice that's used when delivering messages that are based on the message template. For a list of supported voices, see the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceTemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "body" in value:
        out["Body"] = value["body"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
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
    if "version" in value:
        out["Version"] = value["version"]
    if "voice_id" in value:
        out["VoiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> VoiceTemplateResponse:
    out: VoiceTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("DefaultSubstitutions") is not None:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
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
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("VoiceId") is not None:
        out["voice_id"] = data["VoiceId"]
    return out
