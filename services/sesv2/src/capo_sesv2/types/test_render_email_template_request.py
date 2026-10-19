"""Generated from Smithy shape ``com.amazonaws.sesv2#TestRenderEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_data
    import capo_sesv2.types.email_template_name


class TestRenderEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""
    template_data: "capo_sesv2.types.email_template_data.EmailTemplateData"
    """<p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRenderEmailTemplateRequest) -> dict:
    out: dict = {}
    out["TemplateData"] = value["template_data"]
    return out


def deserialize_json(data: dict) -> TestRenderEmailTemplateRequest:
    out: TestRenderEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("TemplateData") is not None:
        out["template_data"] = data["TemplateData"]
    else:
        out["template_data"] = ""
    return out
