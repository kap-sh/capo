"""Generated from Smithy shape ``com.amazonaws.ses#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.html_part
    import capo_ses.types.subject_part
    import capo_ses.types.template_name
    import capo_ses.types.text_part


class Template(TypedDict, closed=True):
    template_name: "capo_ses.types.template_name.TemplateName"
    """<p>The name of the template. You use this name when you send email using the <code>SendTemplatedEmail</code> or <code>SendBulkTemplatedEmail</code> operations.</p>"""
    subject_part: NotRequired["capo_ses.types.subject_part.SubjectPart"]
    """<p>The subject line of the email.</p>"""
    text_part: NotRequired["capo_ses.types.text_part.TextPart"]
    """<p>The email body that is visible to recipients whose email clients do not display HTML content.</p>"""
    html_part: NotRequired["capo_ses.types.html_part.HtmlPart"]
    """<p>The HTML body of the email.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Template, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "subject_part" in value:
        pairs.append((f"{key_prefix}SubjectPart", str(value["subject_part"])))
    if "text_part" in value:
        pairs.append((f"{key_prefix}TextPart", str(value["text_part"])))
    if "html_part" in value:
        pairs.append((f"{key_prefix}HtmlPart", str(value["html_part"])))


def deserialize_query(el: Element) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        out["template_name"] = ""
    child_subject_part = el.find("SubjectPart")
    if child_subject_part is not None:
        out["subject_part"] = str(child_subject_part.text or "")
    child_text_part = el.find("TextPart")
    if child_text_part is not None:
        out["text_part"] = str(child_text_part.text or "")
    child_html_part = el.find("HtmlPart")
    if child_html_part is not None:
        out["html_part"] = str(child_html_part.text or "")
    return out
