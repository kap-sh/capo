"""Generated from Smithy shape ``com.amazonaws.ses#DeleteCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.template_name


class DeleteCustomVerificationEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_ses.types.template_name.TemplateName"
    """<p>The name of the custom verification email template to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCustomVerificationEmailTemplateRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))


def deserialize_query(el: Element) -> DeleteCustomVerificationEmailTemplateRequest:
    out: DeleteCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        out["template_name"] = ""
    return out
