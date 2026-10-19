"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.template_arn
    import capo_connectcases.types.template_id


class CreateTemplateResponse(TypedDict, closed=True):
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    template_arn: "capo_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the newly created template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateResponse) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> CreateTemplateResponse:
    out: CreateTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        out["template_id"] = ""
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    else:
        out["template_arn"] = ""
    return out
