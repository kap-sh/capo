"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_content
    import capo_sesv2.types.email_template_name
    import capo_sesv2.types.tag_list


class CreateEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""
    template_content: "capo_sesv2.types.email_template_content.EmailTemplateContent"
    """<p>The content of the email template, composed of a subject line, an HTML part, and a text-only part.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the email template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailTemplateRequest) -> dict:
    out: dict = {}
    out["TemplateName"] = value["template_name"]
    import capo_sesv2.types.email_template_content

    out["TemplateContent"] = capo_sesv2.types.email_template_content.serialize_json(
        value["template_content"]
    )
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEmailTemplateRequest:
    out: CreateEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    else:
        out["template_name"] = ""
    if data.get("TemplateContent") is not None:
        import capo_sesv2.types.email_template_content

        out["template_content"] = (
            capo_sesv2.types.email_template_content.deserialize_json(
                data["TemplateContent"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEmailTemplateRequest.template_content required"
        )
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
