"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.template_id


class CaseSummary(TypedDict, closed=True):
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummary) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    out["templateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CaseSummary:
    out: CaseSummary = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        out["template_id"] = ""
    return out
