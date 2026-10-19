"""Generated from Smithy shape ``com.amazonaws.sesv2#TestRenderEmailTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.rendered_email_template


class TestRenderEmailTemplateResponse(TypedDict, closed=True):
    rendered_template: "capo_sesv2.types.rendered_email_template.RenderedEmailTemplate"
    """<p>The complete MIME message rendered by applying the data in the <code>TemplateData</code> parameter to the template specified in the TemplateName parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRenderEmailTemplateResponse) -> dict:
    out: dict = {}
    out["RenderedTemplate"] = value["rendered_template"]
    return out


def deserialize_json(data: dict) -> TestRenderEmailTemplateResponse:
    out: TestRenderEmailTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("RenderedTemplate") is not None:
        out["rendered_template"] = data["RenderedTemplate"]
    else:
        out["rendered_template"] = ""
    return out
