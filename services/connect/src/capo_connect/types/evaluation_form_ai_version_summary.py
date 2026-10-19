"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormAIVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_ai_version
    import capo_connect.types.evaluation_form_ai_version_lifecycle


class EvaluationFormAIVersionSummary(TypedDict, closed=True):
    ai_version_name: (
        "capo_connect.types.evaluation_form_ai_version.EvaluationFormAIVersion"
    )
    """<p>The name of the AI version.</p>"""
    ai_version_lifecycle: "capo_connect.types.evaluation_form_ai_version_lifecycle.EvaluationFormAIVersionLifecycle"
    """<p>The lifecycle information for this AI version, including its status and availability dates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormAIVersionSummary) -> dict:
    out: dict = {}
    out["AIVersionName"] = value["ai_version_name"]
    import capo_connect.types.evaluation_form_ai_version_lifecycle

    out["AIVersionLifecycle"] = (
        capo_connect.types.evaluation_form_ai_version_lifecycle.serialize_json(
            value["ai_version_lifecycle"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormAIVersionSummary:
    out: EvaluationFormAIVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("AIVersionName") is not None:
        out["ai_version_name"] = data["AIVersionName"]
    else:
        out["ai_version_name"] = ""
    if data.get("AIVersionLifecycle") is not None:
        import capo_connect.types.evaluation_form_ai_version_lifecycle

        out["ai_version_lifecycle"] = (
            capo_connect.types.evaluation_form_ai_version_lifecycle.deserialize_json(
                data["AIVersionLifecycle"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormAIVersionSummary.ai_version_lifecycle required"
        )
    return out
