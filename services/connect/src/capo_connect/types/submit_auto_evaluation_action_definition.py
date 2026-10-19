"""Generated from Smithy shape ``com.amazonaws.connect#SubmitAutoEvaluationActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_id


class SubmitAutoEvaluationActionDefinition(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.evaluation_form_id.EvaluationFormId"
    """<p>The identifier of the auto-evaluation enabled form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitAutoEvaluationActionDefinition) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    return out


def deserialize_json(data: dict) -> SubmitAutoEvaluationActionDefinition:
    out: SubmitAutoEvaluationActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    return out
