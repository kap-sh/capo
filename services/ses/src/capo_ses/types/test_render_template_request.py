"""Generated from Smithy shape ``com.amazonaws.ses#TestRenderTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.template_data
    import capo_ses.types.template_name


class TestRenderTemplateRequest(TypedDict, closed=True):
    template_name: "capo_ses.types.template_name.TemplateName"
    """<p>The name of the template to render.</p>"""
    template_data: "capo_ses.types.template_data.TemplateData"
    """<p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestRenderTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    pairs.append((f"{key_prefix}TemplateData", str(value["template_data"])))


def deserialize_query(el: Element) -> TestRenderTemplateRequest:
    out: TestRenderTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        out["template_name"] = ""
    child_template_data = el.find("TemplateData")
    if child_template_data is not None:
        out["template_data"] = str(child_template_data.text or "")
    else:
        out["template_data"] = ""
    return out
