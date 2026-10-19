"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkControl``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.uuid


class CreateAssessmentFrameworkControl(TypedDict, closed=True):
    id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier of the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkControl) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateAssessmentFrameworkControl:
    out: CreateAssessmentFrameworkControl = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
