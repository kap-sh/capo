"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template


class CreateAnalysisTemplateOutput(TypedDict, closed=True):
    analysis_template: "capo_cleanrooms.types.analysis_template.AnalysisTemplate"
    """<p>The analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_template

    out["analysisTemplate"] = capo_cleanrooms.types.analysis_template.serialize_json(
        value["analysis_template"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnalysisTemplateOutput:
    out: CreateAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("analysisTemplate") is not None:
        import capo_cleanrooms.types.analysis_template

        out["analysis_template"] = (
            capo_cleanrooms.types.analysis_template.deserialize_json(
                data["analysisTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAnalysisTemplateOutput.analysis_template required"
        )
    return out


def redact_sensitive(value: CreateAnalysisTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "analysis_template" in value:
        import capo_cleanrooms.types.analysis_template

        out["analysis_template"] = (
            capo_cleanrooms.types.analysis_template.redact_sensitive(
                value["analysis_template"]
            )
        )
    return out
